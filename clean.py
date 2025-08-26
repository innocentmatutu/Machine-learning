import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\Windows 10 Pro\Desktop\Machine learning\dirty_data_large.csv')
df['Name'] = df['Name'].str.title()

age = df['Age'].mean()
df['Age'] = df['Age'].fillna(age)
df['Age'] = np.ceil(df['Age']).astype(int)


df['Email'] = df['Email'].str.lower().str.replace('@@','@')
df['Email'] = df['Email'].str.replace('#','@')
df['Email'] = df['Email'].apply(lambda x:x if x.endswith('.com') else x + '.com')
df = df.drop_duplicates(subset=['Name','Email'],keep=False)
df = df.drop_duplicates(subset=['Name'],keep='first')

df['Salary'] = pd.to_numeric(df['Salary'],errors='coerce')
salary = df['Salary'].median()
df['Salary'] = df['Salary'].fillna(salary).astype(int).abs()

df.loc[10,'Salary'] = salary

df['Bonus'] = pd.to_numeric(df['Bonus'],errors='coerce')
bonus = df['Bonus'].median()
df['Bonus'] = df['Bonus'].fillna(bonus).astype(int).abs()
df.loc[df['Bonus'] < 3000,'Bonus'] = bonus

df['JoinDate'] = pd.to_datetime(df['JoinDate'],errors='coerce').dt.date
df['JoinDate'] = df['JoinDate'].fillna(pd.Timestamp.today().date())

df['Score'] = pd.to_numeric(df['Score'],errors='coerce')
score = df['Score'].mean()
df['Score'] =np.ceil(df['Score'].fillna(score)).astype(int)
df.loc[df['Score']< 85,'Score'] = 85 
print(df.to_string())
#it helps identifing outliers
print(df['Salary'].describe())
print(df['Bonus'].describe())
print(df['Score'].describe())