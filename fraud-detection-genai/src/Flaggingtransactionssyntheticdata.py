import pandas as pd
import random

# --- STEP 1: Load the data from a file ---
# Note: Using r'...' makes the path easier to read
file_path = r'C:\Users\Mina\ai-certifications\fraud-detection-genai\results\syntheticdata1.csv'
df = pd.read_csv(file_path)

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

# --- STEP 4: SAVE ONLY FLAGGED TRANSACTIONS TO A CSV ---
# We use the 'flagged' variable here because it only contains Amount > 1000
report_output_path = r'C:\Users\Mina\ai-certifications\fraud-detection-genai\results\flagged_report_only.csv'

flagged.to_csv(report_output_path, index=False)

print(f"\nSUCCESS: The report with ONLY flagged transactions has been saved to:\n{report_output_path}")