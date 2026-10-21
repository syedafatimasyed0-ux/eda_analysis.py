import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Cleaned Data from Task 1
df = pd.read_csv('cleaned_data.csv')

print("--- Data Summary ---")
print(df.info())
print(df.describe())

# 2. Calculate Important Statistics
avg_salary = df['Salary'].mean()
median_age = df['Age'].median()
total_employees = df['ID'].count()

print(f"\nTotal Employees: {total_employees}")
print(f"Average Salary: {avg_salary}")
print(f"Median Age: {median_age}")

# 3. Generate Charts for Visualization
plt.figure(figsize=(8, 5))
sns.barplot(x='Department', y='Salary', data=df, ci=None, palette='viridis')
plt.title('Average Salary by Department')
plt.savefig('salary_by_department.png')
plt.close()

plt.figure(figsize=(6, 6))
df['Department'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['#ff9999','#66b3ff'])
plt.title('Department Distribution')
plt.savefig('department_distribution.png')
plt.close()

print("\nEDA Completed & Charts Saved Successfully!")
