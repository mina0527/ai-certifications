import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from datetime import timedelta

# --- STEP 1: SETUP SYNTHETIC DATA ---
# Let's assume User_101 usually spends \$20-\$100 near home (Distance 0-10)
data = {
    'User_ID': ['U101']*10 + ['U101'],
    'Timestamp': pd.to_datetime(['2023-10-01 10:00:00', '2023-10-01 12:00:00', '2023-10-02 09:00:00', 
                                 '2023-10-03 15:00:00', '2023-10-04 11:00:00', '2023-10-05 10:00:00',
                                 '2023-10-06 14:00:00', '2023-10-07 12:00:00', '2023-10-08 09:00:00',
                                 '2023-10-09 11:00:00', '2023-10-09 11:05:00']), # Note: 2 txns in 5 mins
    'Amount': [50, 45, 60, 30, 55, 40, 52, 48, 55, 2000, 1800], # Note: \$2000 & \$1800 are high
    'Dist_From_Home': [2, 5, 1, 8, 3, 4, 2, 6, 3, 500, 505]      # Note: 500 miles is far
}
df = pd.DataFrame(data)

# --- STEP 2: PARAMETER CALCULATION (Feature Engineering) ---

# A. Frequency: Calculate transactions in the last 24 hours
df = df.sort_values(['User_ID', 'Timestamp'])
df['Frequency_24h'] = df.groupby('User_ID')['Timestamp'].diff().dt.total_seconds()
# Fill NaN (first transaction) with a large number and convert to a frequency score
df['Frequency_24h'] = df['Frequency_24h'].fillna(86400) 
df['Frequency_Score'] = 1 / (df['Frequency_24h'] + 1) # Higher score = more frequent

# B. Select our features for the model
features = ['Amount', 'Frequency_Score', 'Dist_From_Home']
X = df[features]

# --- STEP 3: CONFIGURE ANOMALY DETECTION PARAMETERS ---

model = IsolationForest(
    n_estimators=100,      # Number of trees (100 is standard)
    contamination=0.1,     # We expect 10% of this specific test data to be "bad"
    max_samples='auto',    # Use all available data for training
    random_state=42
)

# --- STEP 4: TRAIN AND PREDICT ---
df['Anomaly_Score'] = model.fit_predict(X)
# IsolationForest returns -1 for anomalies and 1 for normal

# --- STEP 5: VIEW RESULTS ---
# Flag transactions where Anomaly_Score is -1
anomalies = df[df['Anomaly_Score'] == -1]

print("--- ANOMALOUS TRANSACTIONS DETECTED ---")
print(anomalies[['Timestamp', 'Amount', 'Dist_From_Home', 'Frequency_Score']])