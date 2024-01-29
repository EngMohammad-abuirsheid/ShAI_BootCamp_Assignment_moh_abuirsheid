import pandas as pd

# Load the dataset
file_path = r"C:\Users\Mohammad\Desktop\jupyter\Salaries.csv"
df = pd.read_csv(file_path)

# Basic Data Exploration
num_rows, num_columns = df.shape
print(f"Number of Rows: {num_rows}")
print(f"Number of Columns: {num_columns}")

# Data Types of Each Column
data_types = df.dtypes
print("\nData Types:")
print(data_types)

# Check for Missing Values in Each Column
missing_values = df.isnull().sum()
print("\nMissing Values:")
print(missing_values)
