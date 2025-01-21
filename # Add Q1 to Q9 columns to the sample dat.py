# Add Q1 to Q9 columns to the sample data
import numpy as np
import pandas as pd 
df = pd.read_csv('updated_sample_data.csv')

np.random.seed(42)
for i in range(1, 10):
    df[f"Q{i}"] = np.random.randint(1, 4, size=len(df))  # Random scores between 1 and 3

# Save updated data to CSV
file_path = "/mnt/data/updated_sample_data.csv"
df.to_csv(file_path, index=False)
file_path
