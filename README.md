# AI-Driven Adaptive Traffic Control System (IISc-AIM Optimized)

###  Project Overview
This project implements an intelligent traffic management system specifically designed for **Indian urban environments**. It replaces traditional fixed-timer signals with a dynamic computer-vision-based system that adjusts "Green" light durations in real-time based on actual vehicle density.

###  Key Highlights
*   **IISc-AIM UVH-26 Integration:** Utilizes the specialized YOLOv11-S model trained by the **Indian Institute of Science (IISc)** for high-accuracy detection of Indian vehicle classes (Auto-rickshaws, bikes, etc.).
*   **Manual ROI Calibration:** A custom-built interface allows traffic operators to manually define lanes for analysis.
*   **Dynamic Decision Logic:** Implements mathematical flow-ratio algorithms to optimize signal cycles.

### 🛠 Tech Stack
*   **Language:** Python 3.x
*   **Model:** YOLOv11-S (UVH-26 weights)
*   **Frontend:** HTML5, CSS3, JavaScript (via PyWebView)
*   **Analytics:** Pandas, Matplotlib, OpenCV

###  Model Weights
Due to file size constraints, the weights are not hosted in this repo.
**Source:** [IISc-AIM UVH-26 Weights](https://huggingface.co/iisc-aim/UVH-26/tree/main/weights/YOLOv11-S)
*   Please download `UVH-26-MV-YOLOv11-S.pt` and place it in the root directory before running `main.py`.

###  Performance Analytics
The system automatically generates a `traffic_results.csv` file, which is then processed to visualize:
1. Vehicle Density vs. Green Time Allocation.
2. System Throughput Performance.
3. Computational Latency per Cycle.