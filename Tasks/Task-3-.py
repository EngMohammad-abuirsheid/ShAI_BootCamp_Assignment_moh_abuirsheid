import pandas as pd


df = pd.read_csv(r"C:\Users\Mohammad\Desktop\jupyter\Salaries.csv")

# Check for missing values in each column
missing_values = df.isnull().sum()
print("\nMissing Values:")
print(missing_values)

# Handle missing data for numerical columns by filling with mean
numerical_columns = ['BasePay', 'OvertimePay', 'OtherPay', 'Benefits', 'TotalPay', 'TotalPayBenefits']
df[numerical_columns] = df[numerical_columns].fillna(df[numerical_columns].mean())

# Handle missing data for categorical columns by filling with mode
categorical_columns = ['EmployeeName', 'JobTitle', 'Year', 'Notes', 'Agency', 'Status']
df[categorical_columns] = df[categorical_columns].fillna(df[categorical_columns].mode().iloc[0])

# Verify that missing values have been filled
missing_values_after_fill = df.isnull().sum()
print("\nNumber of Missing Values after handling:")
print(missing_values_after_fill)
