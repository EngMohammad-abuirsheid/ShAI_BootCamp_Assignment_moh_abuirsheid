import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\Mohammad\Desktop\jupyter\Salaries.csv")

# Create histogram for the distribution of salaries
plt.figure(figsize=(12, 6))
sns.histplot(df['TotalPay'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Salaries')
plt.xlabel('Total Pay')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(80, 80))
department_proportions = df['JobTitle'].value_counts()
colors = sns.color_palette('pastel', len(department_proportions))
plt.pie(department_proportions, labels=department_proportions.index, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Proportion of Employees in Different Departments', fontsize=16)
plt.show()
