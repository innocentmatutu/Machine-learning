import numpy as np
import pandas as pd

df = pd.read_csv(r'C:\Users\Windows 10 Pro\Downloads\dirty_dataset (1).csv')

df = df.drop_duplicates(subset=['Name'],keep='first')

df.loc[df['Age'] < 30,'Age'] = 30
df.loc[df['Age'] > 60, 'Age'] = 45

df['Email'] = df['Email'].str.replace('mailcom','mail')
df['Email'] = df['Email'].str.replace('yahoo','mail')
df['Email'] = df['Email'].str.replace('gmail','mail')

df['Salary'] = df['Salary'].abs()
salary = df['Salary'].mean()
df['Salary'] = np.floor(df['Salary'].fillna(salary)).astype(int)
df.loc[df['Salary']<380000,'Salary'] = 380000

df.loc[df['Bonus']<3977,'Bonus'] = 5962

df['Department'] = df['Department'].str.replace('H.R','HR')
df['Department'] = df['Department'].str.replace('Sale','Sales')
df['Department'] = df['Department'].str.replace('I.T','IT')
df['Department'] = df['Department'].str.replace('Saless','Sales')
print(df.to_string())

