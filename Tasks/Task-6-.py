import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\Mohammad\Desktop\jupyter\Salaries.csv")

# Calculate correlation between 'TotalPay' and 'Year'
correlation = df[['TotalPay', 'Year']].corr().iloc[0, 1]

# Visualize the relationship with a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Year', y='TotalPay', data=df, alpha=0.5, color='skyblue')
plt.title(f'Scatter Plot: Salary vs. Year (Correlation: {correlation:.2f})')
plt.xlabel('Year')
plt.ylabel('Total Pay (Salary)')
plt.show()
