import pandas as pd
import numpy as np

df = pd.read_csv('mesy.csv')
df = df.drop_duplicates(subset=['Name','Email'],keep=False)

age = df['Age'].median()
df['Age'] = df['Age'].fillna(age).astype(int)

df['Email'] = df['Email'].str.strip().str.replace('@@','@')
df['Email'] = df['Email'].str.replace('#','@')
df['Email'] = df['Email'].apply(lambda x:x if x.endswith('mail.com') else x + '.com')

df.loc[df['Salary']>95000,'Salary'] = 95000

df['Bonus'] = df['Bonus'].abs()
df.loc[df['Bonus']> 9500,'Bonus'] = 9500

df.loc[df['Department'] == 'Human Resources','Department'] = "HR"

df['JoinDate'] = pd.to_datetime(df['JoinDate'],errors='coerce').dt.date
df['JoinDate'] = df['JoinDate'].fillna(pd.Timestamp.today().date())

score = df['Score'].mean()
df['Score'] = np.ceil(df['Score'].fillna(score)).astype(int)
df.loc[df['Score']>95,"Score"] = 95
print(df)