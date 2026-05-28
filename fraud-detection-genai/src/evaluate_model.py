import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score

# 1. LOAD THE NEW ML RESULTS
# Make sure this matches the filename from your ML script!
file_path = r'C:\Users\Mina\ai-certifications\fraud-detection-genai\results\flagged_transactions_report.csv'

try:
    df = pd.read_csv(file_path)
    
    # 2. DEFINE ACTUAL VS PREDICTED
    # Actual is the ground truth from the data generation
    actual = df['Is_Fraud'] 
    
    # Predicted is the result from the Random Forest ML model
    predicted = df['ML_Predicted_Fraud']

    # 3. CALCULATE THE NEW METRICS
    accuracy = accuracy_score(actual, predicted)
    recall = recall_score(actual, predicted)
    precision = precision_score(actual, predicted)
    conf_matrix = confusion_matrix(actual, predicted)
    tn, fp, fn, tp = conf_matrix.ravel()

    # 4. PRINT EVERYTHING TO THE TERMINAL
    print("\n" + "="*40)
    print("🚀 MACHINE LEARNING MODEL RESULTS")
    print("="*40)
    print(f"Overall Accuracy:  {accuracy:.2%}")
    print(f"Recall (Fraud % Caught): {recall:.2%}")
    print(f"Precision:         {precision:.2%}")
    print("-" * 40)
    print(f"True Positives (Fraud Caught): {tp}")
    print(f"False Positives (Mistakes):    {fp}")
    print(f"False Negatives (Missed):      {fn}")
    print(f"True Negatives (Correct Legit): {tn}")
    print("="*40 + "\n")

except Exception as e:
    print(f"❌ ERROR: {e}")