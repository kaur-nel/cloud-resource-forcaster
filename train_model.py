import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

# LOAD DATA
df = pd.read_csv("server_logs.csv")

# PREP DATA
# X = What the AI looks at (Hour and Day)
# y = What the AI tries to predict (CPU Load)
X = df[["Hour_of_Day", "Day_of_Week"]]
y = df["CPU_Utilization"]

# Split data: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TRAIN 
print("Training the Random Forest AI...")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train) 

# PREDICT 
predictions = model.predict(X_test)

# VISUALIZE ACCURACY 
plt.figure(figsize=(10, 5))
# Plot actual server load
plt.plot(y_test.values[:50], label="Actual CPU Load", color="blue", marker="o")
# Plot what the AI predicted
plt.plot(predictions[:50], label="AI Prediction", color="red", linestyle="--", marker="x")

plt.title("Server CPU Load: Actual vs. AI Prediction (First 50 Hours)")
plt.xlabel("Hours")
plt.ylabel("CPU Utilization (%)")
plt.legend()
plt.grid(True)
plt.show()