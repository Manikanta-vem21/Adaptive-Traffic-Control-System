import pandas as pd
import matplotlib.pyplot as plt

# Load real experiment data
df = pd.read_csv("traffic_results.csv")

# ==============================
# 1. Vehicle Count vs Adaptive Green Time
# ==============================
plt.figure()
plt.plot(df["Avg_Vehicle_Count"], df["Adaptive_Green_Time"], marker='o')
plt.xlabel("Average Vehicle Count")
plt.ylabel("Adaptive Green Time (s)")
plt.title("Vehicle Count vs Adaptive Green Time")
plt.grid(True)
plt.show()

# ==============================
# 2. Adaptive vs Fixed Green Time
# ==============================
plt.figure()
plt.plot(df["Adaptive_Green_Time"], label="Adaptive Green Time")
plt.plot(df["Fixed_Green_Time"], label="Fixed Green Time", linestyle='--')
plt.xlabel("Cycle Number")
plt.ylabel("Green Time (s)")
plt.title("Adaptive vs Fixed Signal Timing")
plt.legend()
plt.grid(True)
plt.show()

# ==============================
# 3. Waiting Time Comparison
# ==============================
plt.figure()
plt.plot(df["Avg_Waiting_Time"], color='orange')
plt.xlabel("Cycle Number")
plt.ylabel("Average Waiting Time (s)")
plt.title("Average Waiting Time per Cycle")
plt.grid(True)
plt.show()

# ==============================
# 4. Throughput Performance
# ==============================
plt.figure()
plt.plot(df["Throughput"], color='green')
plt.xlabel("Cycle Number")
plt.ylabel("Throughput (vehicles)")
plt.title("System Throughput per Cycle")
plt.grid(True)
plt.show()

# ==============================
# 5. Processing Time Feasibility
# ==============================
plt.figure()
plt.plot(df["Processing_Time"], color='red')
plt.xlabel("Cycle Number")
plt.ylabel("Processing Time (s)")
plt.title("Processing Time per Cycle")
plt.grid(True)
plt.show()
