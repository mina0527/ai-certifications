import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_transaction_data(n=1000):
    np.random.seed(42)
    
    cities = ['New York, NY', 'Los Angeles, CA', 'Chicago, IL', 'Houston, TX', 
              'Phoenix, AZ', 'Philadelphia, PA', 'San Antonio, TX', 'San Diego, CA']
    
    data = []
    start_date = datetime(2023, 1, 1)

    for i in range(n):
        tx_id = f"TXN_{1000 + i}"
        user_id = f"U_{np.random.randint(100, 999)}"
        
        # Generate random time within a 30-day window
        seconds_offset = np.random.randint(0, 30 * 24 * 60 * 60)
        timestamp = start_date + timedelta(seconds=seconds_offset)
        
        # Base amount logic: Most transactions are small-medium
        amount = round(np.random.exponential(scale=1000) + 5, 2)
        
        # Location
        location = random.choice(cities)
        
        # Fraud Logic: 
        # 1. Higher chance if amount is very high
        # 2. Higher chance if it's late at night (00:00 - 05:00)
        # 3. Overall rare (approx 5%)
        is_fraud = 0
        fraud_chance = 0.02
        
        #change the amount threshold for fraud to 1000 to create more fraudulent transactions
        if amount > 1000:
            fraud_chance += 0.15
        if timestamp.hour < 5:
            fraud_chance += 0.10
            
        if random.random() < fraud_chance:
            is_fraud = 1
            # Fraudulent transactions often have higher amounts
            if is_fraud: amount += np.random.randint(100, 1000)

        data.append([tx_id, user_id, timestamp, round(amount, 2), location, is_fraud])

    columns = ['Transaction_ID', 'User_ID', 'Timestamp', 'Amount', 'Location', 'Is_Fraud']
    return pd.DataFrame(data, columns=columns)

# Generate 1,000 rows
df = generate_transaction_data(1000)

# Display first few rows
print(df.head())

# Save to CSV
df.to_csv('syntheticdata1.csv', index=False)