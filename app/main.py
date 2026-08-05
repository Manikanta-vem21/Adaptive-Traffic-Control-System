import webview
import threading
import cv2
import time
import base64
from ultralytics import YOLO
import csv
import os

# ==============================
# GLOBAL ROI & FRAME DATA
# ==============================
roi_coords = None
frame_width = None
frame_height = None

# ==============================
# CSV SETUP
# ==============================
RESULTS_FILE = "traffic_results.csv"

if not os.path.exists(RESULTS_FILE):
    with open(RESULTS_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            "Cycle",
            "Avg_Vehicle_Count",
            "Traffic_Density",
            "Adaptive_Green_Time",
            "Fixed_Green_Time",
            "Avg_Waiting_Time",
            "Throughput",
            "Processing_Time"
        ])

# ==============================
# YOLO MODEL
# ==============================
model = YOLO("UVH-26-MV-YOLOv11-S.pt")

# ==============================
# PARAMETERS
# ==============================
OBSERVATION_TIME = 10
MIN_GREEN = 20
MAX_GREEN = 60
FIXED_GREEN = 30
FIXED_YELLOW = 3
FIXED_RED = 5
SATURATION_FLOW = 0.5

cycle_number = 0


class TrafficSystem:

    def select_video(self):
        file_types = ('Video Files (*.mp4;*.avi;*.mov)',)
        result = window.create_file_dialog(
            webview.OPEN_DIALOG,
            allow_multiple=False,
            file_types=file_types
        )
        return result[0] if result else None

    def show_first_frame(self, video_path):
        cap = cv2.VideoCapture(video_path)
        ret, frame = cap.read()
        cap.release()

        if ret:
            global frame_width, frame_height
            frame_height, frame_width, _ = frame.shape
            _, buffer = cv2.imencode(".jpg", frame)
            jpg = base64.b64encode(buffer).decode("utf-8")
            window.evaluate_js(f"updateFrame('{jpg}');")

    def set_roi(self, roi):
        global roi_coords
        roi_coords = roi

    def start(self, video_path):
        threading.Thread(
            target=self.run_system,
            args=(video_path,),
            daemon=True
        ).start()

    def run_system(self, video_path):
        global cycle_number

        cap = cv2.VideoCapture(video_path)

        while True:
            if roi_coords is None:
                time.sleep(1)
                continue

            cycle_start = time.time()
            counts = []

            obs_start = time.time()
            while time.time() - obs_start < OBSERVATION_TIME:

                ret, frame = cap.read()
                if not ret:
                    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue

                results = model(frame, conf=0.4, verbose=False)

                h, w, _ = frame.shape

                roi_left = int(roi_coords["x1"] * w / 800)
                roi_top = int(roi_coords["y1"] * h / 450)
                roi_right = int(roi_coords["x2"] * w / 800)
                roi_bottom = int(roi_coords["y2"] * h / 450)

                roi_area = max((roi_right - roi_left) * (roi_bottom - roi_top), 1)
                vehicle_count = 0

                for box in results[0].boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cx = (x1 + x2) // 2
                    cy = (y1 + y2) // 2

                    if roi_left < cx < roi_right and roi_top < cy < roi_bottom:
                        vehicle_count += 1
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

                counts.append(vehicle_count)

                _, buffer = cv2.imencode(".jpg", frame)
                jpg = base64.b64encode(buffer).decode("utf-8")

                remaining = int(OBSERVATION_TIME - (time.time() - obs_start))
                window.evaluate_js(f"updateFrame('{jpg}');")
                window.evaluate_js(
                    f"updateMetrics({vehicle_count}, 'OBSERVING', {remaining});"
                )

                time.sleep(0.03)

            avg_count = sum(counts) / len(counts)
            density = avg_count / roi_area

            arrival_rate = avg_count / OBSERVATION_TIME
            flow_ratio = min(arrival_rate / SATURATION_FLOW, 0.9)

            optimal_cycle = (1.5 * (FIXED_YELLOW + 2) + 5) / (1 - flow_ratio)
            adaptive_green = int(max(MIN_GREEN, min(optimal_cycle * flow_ratio, MAX_GREEN)))

            # ==============================
            # SIGNAL PHASES
            # ==============================
            for t in range(adaptive_green):
                window.evaluate_js(
                    f"updateMetrics({int(avg_count)}, 'GREEN', {adaptive_green-t});"
                )
                time.sleep(1)

            for t in range(FIXED_YELLOW):
                window.evaluate_js(
                    f"updateMetrics({int(avg_count)}, 'YELLOW', {FIXED_YELLOW-t});"
                )
                time.sleep(1)

            for t in range(FIXED_RED):
                window.evaluate_js(
                    f"updateMetrics({int(avg_count)}, 'RED', {FIXED_RED-t});"
                )
                time.sleep(1)

            # ==============================
            # RESEARCH METRICS
            # ==============================
            avg_waiting_time = FIXED_RED * (avg_count / 10)
            throughput = avg_count * (adaptive_green / optimal_cycle)
            processing_time = time.time() - cycle_start

            cycle_number += 1

            with open(RESULTS_FILE, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    cycle_number,
                    round(avg_count, 2),
                    round(density, 8),
                    adaptive_green,
                    FIXED_GREEN,
                    round(avg_waiting_time, 2),
                    round(throughput, 2),
                    round(processing_time, 2)
                ])


# ==============================
# WEBVIEW WINDOW
# ==============================
traffic = TrafficSystem()

window = webview.create_window(
    "AI Adaptive Traffic Signal",
    "index.html",
    js_api=traffic,
    width=1300,
    height=800
)

webview.start()
