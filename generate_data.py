import pandas as pd
import numpy as np

print("Generating Server Telemetry Data...")

# Create 30 days of hourly data (720 hours)
hours = np.arange(720)
days = (hours // 24) % 7 # 0=Monday, 6=Sunday

# Simulate server CPU load
# Base load is 20%. Peaks happen in the middle of the day. 
# Weekends have lower traffic. Add random noise to make it realistic.
base_load = 20
daily_spike = np.sin(hours * (2 * np.pi / 24)) * 30 # Spikes up and down daily
weekend_drop = np.where(days >= 5, -15, 0) # Drops 15% on sat/sun
noise = np.random.normal(0, 5, 720) # Random server spikes

cpu_utilization = base_load + daily_spike + weekend_drop + noise
cpu_utilization = np.clip(cpu_utilization, 5, 100) # CPU can't go below 5% or above 100%

# Build dataframe
df = pd.DataFrame({
    "Hour_of_Day": hours % 24,
    "Day_of_Week": days,
    "CPU_Utilization": cpu_utilization
})

df.to_csv("server_logs.csv", index=False)
print("Saved 720 hours of data to 'server_logs.csv'")