import pandas as pd
from pandas import DataFrame

d={'one':pd.Series([1.,11.,111.,22223,2222]),
   'two':pd.Series([2.,22.,222.,11121,111]),'three':pd.Series([1.,11.,111.,111,444]),
   'four':pd.Series([2.,22.,222.,11212,444])}


df=pd.DataFrame(d)
print(df)
#printing without index
print(df.to_string(index=False))





# from item

c=df.from_items([('two', [1, 2, 3])])
print(c)

#deleting one column
del df['two']
print(df)

# adding one column
df['five'  ]=df['one']*df['two']
print(df)


# inserting a scalar value

df['four']='foo'
print(df)

#assign

df.assign(ratio=df['one']/df['two'])
print(df)

# #selecting column
print(df['one'])
#
# # Select row by label
print(df.loc['a'])


# Select row by integer location
 df.iloc[1]

# Slice rows
print(df[2:5])

