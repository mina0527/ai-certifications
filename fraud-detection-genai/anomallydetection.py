import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import time

# --- STEP 1: PREPARE TRAINING DATA ---
# Let's create a "History" of 1000 normal transactions
np.random.seed(42)
normal_amounts = np.random.normal(50, 20, 1000) # Most transactions around $50
normal_hours = np.random.randint(8, 22, 1000)   # Most happen during the day

train_df = pd.DataFrame({
    'Amount': normal_amounts,
    'Hour': normal_hours})

# --- STEP 2: TRAIN THE ANOMALY DETECTOR ---
# contamination=0.01 means we expect about 1% of data to be outliers
model = IsolationForest(contamination=0.01, random_state=42)
model.fit(train_df)

print("System Initialized. Monitoring real-time stream...")

# --- STEP 3: SIMULATE REAL-TIME MONITORING ---
# This list simulates transactions hitting your server one by one
live_stream = [
    {'Amount': 45.00, 'Hour': 14},   # Normal
    {'Amount': 12.50, 'Hour': 10},   # Normal
    {'Amount': 9000.00, 'Hour': 2},  # ANOMALY: Huge amount at 2 AM
    {'Amount': 55.20, 'Hour': 16},   # Normal
    {'Amount': 15.00, 'Hour': 3},    # ANOMALY: Unusual time for a small buy
]

for txn in live_stream:
    # Convert transaction to format the model understands
    current_txn = pd.DataFrame([txn])
    
    # Predict: 1 = Normal, -1 = Anomaly
    prediction = model.predict(current_txn)[0]
    
    # Get the anomaly score (lower means more suspicious)
    score = model.decision_function(current_txn)[0]
    
    status = "OK" if prediction == 1 else "!!! ALERT: ANOMALY DETECTED !!!"
    
    print(f"Checking Transaction: ${txn['Amount']} at {txn['Hour']}:00 -> {status} (Score: {round(score, 3)})")
    
    # Small pause to simulate real-time processing
    time.sleep(1)
