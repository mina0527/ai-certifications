import pandas as pd
import random

# --- STEP 1: DEFINE THE DATA (Creating 'df') ---
data = {
    'Transaction_ID': [f'TXN_{i}' for i in range(1001, 1011)],
    'User_ID': [f'U_{random.randint(100, 999)}' for _ in range(10)],
    'Amount': [45.20, 12.99, 850.00, 23.50, 1200.00, 945.80, 5.25, 155.00, 62.10, 2500.00],
    'Location': ['NY', 'TX', 'CA', 'IL', 'FL', 'UA', 'WA', 'CO', 'TX', 'Unknown']
}

# This line is where 'df' is defined!
df = pd.DataFrame(data)

# --- STEP 2: CHECK TRANSACTIONS OVER 1000 ---
THRESHOLD = 1000

# Now 'df' exists, so this won't cause an error
df['Needs_Review'] = df['Amount'] > THRESHOLD

# Add a reason column
df.loc[df['Amount'] > THRESHOLD, 'Review_Reason'] = f"Transaction exceeds ${THRESHOLD}"

# --- STEP 3: SHOW RESULTS ---
print("--- ALL TRANSACTIONS ---")
print(df)

print("\n--- FLAGGED FOR REVIEW ---")
flagged = df[df['Needs_Review'] == True]
print(flagged)