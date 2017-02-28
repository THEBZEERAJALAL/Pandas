import pandas as pd
from pandas import DataFrame,read_csv
import matplotlib

names = ['thebz','shakkz','thasni']
birth = [23,56,89]
name_birth=list(zip(names,birth))


df = pd.DataFrame(data=name_birth, columns=['names','birth'])

df.to_csv('birth.csv',index=False,header=False)

df = pd.read_csv(r'/home/thebzeera/PycharmProjects/Pandas/birth.csv',names=['name','number'])

print(df)
print("**********************************************************************")
print(df.dtypes)
print("**********************************************************************")
sort = df.sort_values(['number'],ascending=False)
print(sort)

print("**********************************************************************")
p=sort.head(1)
print(p)
print("**********************************************************************")

c=df['number'].max()
print(c)
print("**********************************************************************")

