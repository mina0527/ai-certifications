import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 1. LOAD THE DATA
# We load the synthetic data you created earlier
path = r'C:\Users\Mina\ai-certifications\fraud-detection-genai\data\syntheticdata1.csv'
df = pd.read_csv(path)

# 2. TRAIN THE MACHINE LEARNING MODEL
# Features (X) = Amount. Target (y) = Is_Fraud.
X = df[['Amount']]
y = df['Is_Fraud']

# Split the data so the model can learn
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and Train the Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 3. MAKE PREDICTIONS
# The model now decides which transactions are fraud based on its training
df['ML_Predicted_Fraud'] = model.predict(X)

# 4. SAVE TO A NEW FILE
output_path = r'C:\Users\Mina\ai-certifications\fraud-detection-genai\results\ml_flagged_results.csv'
df.to_csv(output_path, index=False)

print(f"✅ SUCCESS: ML Model trained. Results saved to {output_path}")