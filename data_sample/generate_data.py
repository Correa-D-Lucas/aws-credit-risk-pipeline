import pandas as pd
import pyarrow  

data = {
    "person_id": [1, 2, 3, 4, 5],
    "age": [25, 45, 35, 29, 50],
    "income": [50000, 80000, 40000, 30000, 90000],
    "loan_amount": [10000, 20000, 15000, 12000, 25000],
    "credit_score": [650, 720, 600, 580, 750],
    "default": [0, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

# força engine pyarrow
df.to_parquet("data_sample/credit_data.parquet", index=False, engine='pyarrow')

print("Parquet file created!")