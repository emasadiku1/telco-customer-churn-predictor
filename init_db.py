import os
import pandas as pd
from sqlalchemy import create_engine

# 1. Define paths
csv_path = os.path.join('data', 'Telco-Customer-Churn.csv')
db_path = 'sqlite:///telco_churn.db'

print("Checking for dataset...")
if not os.path.exists(csv_path):
    print(f"❌ Error: Could not find the CSV file at '{csv_path}'.")
    print("Please make sure you created a 'data' folder and placed the CSV inside it.")
else:
    print(" can read CSV. Initializing database...")
    
    # 2. Read the raw CSV
    df = pd.read_csv(csv_path)
    
    # 3. Create connection to SQLite database
    engine = create_engine(db_path)
    
    # 4. Write data to a SQL table named 'raw_churn'
    df.to_sql('raw_churn', engine, if_exists='replace', index=False)
    
    print("✅ Success! 'telco_churn.db' has been created.")
    print("The raw data is now safely stored inside the 'raw_churn' SQL table.")