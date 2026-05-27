import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# 1. Load the data
file_path = r'C:\Users\Mina\ai-certifications\fraud-detection-genai\results\flagged_transactions_report.csv'

try:
    df = pd.read_csv(file_path)

    # 2. Check if 'Is_Fraud' exists (The "Ground Truth")
    if 'Is_Fraud' not in df.columns:
        print("Error: The CSV doesn't have an 'Is_Fraud' column to compare against.")
        print("To get metrics, your synthetic data needs to have the actual fraud answers.")
    else:
        # 3. Define Actual (Ground Truth) vs Predicted (Your Rule)
        actual = df['Is_Fraud'] 
        predicted = df['Needs_Review'].astype(int) 

        # 4. Calculate Metrics
        accuracy = accuracy_score(actual, predicted)
        conf_matrix = confusion_matrix(actual, predicted)
        tn, fp, fn, tp = conf_matrix.ravel()

        # 5. Output the Results
        print("="*30)
        print("  FRAUD MODEL PERFORMANCE")
        print("="*30)
        print(f"Overall Accuracy: {accuracy:.2%}")
        print("-" * 30)
        print(f"True Positives  (Caught Fraud): {tp}")
        print(f"False Positives (False Alarms): {fp}")
        print(f"False Negatives (Missed Fraud): {fn}")
        print(f"True Negatives  (Correct Legit): {tn}")
        print("-" * 30)
        
        # Precision and Recall
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        
        print(f"Precision: {precision:.2%} (How reliable are your alerts?)")
        print(f"Recall:    {recall:.2%} (How much total fraud did you catch?)")
        print("="*30)

except FileNotFoundError:
    print(f"Could not find the file at {file_path}")