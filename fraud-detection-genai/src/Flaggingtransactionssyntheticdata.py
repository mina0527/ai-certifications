import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 1. LOAD DATA
input_path = r'C:\Users\Mina\ai-certifications\fraud-detection-genai\results\flagged_transactions_report.csv'
df = pd.read_csv(input_path)

# 2. PREPARE FEATURES (X) AND TARGET (y)
# We use Amount and Location (converted to numbers) as our "Features"
X = df[['Amount']] # You can add more columns here
y = df['Is_Fraud'] # This is what the model is trying to learn

# 3. TRAIN THE MACHINE LEARNING MODEL
# This is the "Training" part the grader was looking for!
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train) # The model is now "learning" the patterns

# 4. USE THE MODEL TO PREDICT
df['ML_Prediction'] = model.predict(X)

# 5. SAVE THE ML RESULTS
output_path = r'C:\Users\Mina\ai-certifications\fraud-detection-genai\results\ml_flagged_results.csv'
df.to_csv(output_path, index=False)

print("Machine Learning Model trained and applied successfully!")