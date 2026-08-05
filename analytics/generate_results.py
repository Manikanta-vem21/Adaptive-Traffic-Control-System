import pandas as pd
import matplotlib.pyplot as plt

# Load your model results
data = pd.read_csv("traffic_results.csv")

# ----------------------------
# 1️⃣ Vehicle Count vs Cycle
# ----------------------------
plt.figure()
plt.plot(data["Cycle"], data["Vehicle_Count"], marker='o')
plt.xlabel("Cycle Number")
plt.ylabel("Vehicle Count in ROI")
plt.title("Vehicle Count per Signal Cycle")
plt.show()


# ----------------------------
# 2️⃣ Green Time Adaptation
# ----------------------------
plt.figure()
plt.plot(data["Cycle"], data["Green_Time"], marker='o')
plt.xlabel("Cycle Number")
plt.ylabel("Green Signal Duration (seconds)")
plt.title("Adaptive Green Signal Duration")
plt.show()


# ----------------------------
# 3️⃣ Vehicle Count vs Green Time
# ----------------------------
plt.figure()
plt.scatter(data["Vehicle_Count"], data["Green_Time"])
plt.xlabel("Vehicle Count")
plt.ylabel("Green Time (seconds)")
plt.title("Correlation Between Traffic Density and Green Allocation")
plt.show()


# ----------------------------
# 4️⃣ Processing Time Analysis
# ----------------------------
plt.figure()
plt.plot(data["Cycle"], data["Processing_Time"], marker='o')
plt.xlabel("Cycle Number")
plt.ylabel("Processing Time (seconds)")
plt.title("System Processing Time Per Cycle")
plt.show()