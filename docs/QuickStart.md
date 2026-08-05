#  Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Manikanta-vem21/Adaptive-Traffic-Control-System.git
cd Adaptive-Traffic-Control-System
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download Model Weights

Download the pretrained **YOLOv11-S** weights from the link above and place them inside the `app/` directory.

### 4. Run the Application

```bash
python app/main.py
```

---

##  Usage

1. Upload a traffic video (`.mp4` or `.avi`).
2. Select the **Region of Interest (ROI)**.
3. Click **Start Detection**.
4. The system automatically detects vehicles and adjusts green signal timing.
5. Performance metrics are saved as `traffic_results.csv`.

To visualize the results:

```bash
python analytics/plot_results.py
```