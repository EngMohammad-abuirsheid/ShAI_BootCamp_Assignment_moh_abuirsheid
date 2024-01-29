import pandas as pd

# Load the dataset
file_path = r"C:\Users\Mohammad\Desktop\jupyter\Salaries.csv"
df = pd.read_csv(file_path)

# Group the data by 'JobTitle' and 'Year' and calculate summary statistics
grouped_data = df.groupby(['JobTitle', 'Year'])['TotalPay'].agg(['count', 'mean', 'min', 'max', 'std']).reset_index()

# Display the grouped data
print(grouped_data.head())