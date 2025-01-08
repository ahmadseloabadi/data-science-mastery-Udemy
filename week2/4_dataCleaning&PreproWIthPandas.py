# handling missing values
# method for handling missing values
# --> drop missing values
# --> fill missing values
# --> interpolation

print('\n--- Handling missing values----\n')

import pandas as pd

# Membuat DataFrame dengan nilai kosong (NaN)
data = {
    "Tanggal": ["2025-01-01", "2025-02-15", "2025-03-20", "2025-04-25"],
    "Nama": ["Alice", "Bob", "lukas", "Charlie"],
    "Usia": [25, 23, None, 35],
    "Kota": ["Jakarta", "Bandung", None, "Surabaya"],
    "Pendapatan": [5000000, None,4500000, None]
}

df = pd.DataFrame(data)

print('\n initial dataframe :\n',df)

print('\n --drop missing values dataframe--\n')


print('\n drop missing values :\n',df.dropna())
print('\n drop columns that have missing values :\n',df.dropna(axis=1))
print('\n drop rows that have missing values :\n',df.dropna(axis=0))

print('\n --fill missing values dataframe--\n')

print('\n fill missing values with fillna(method="ffill") :\n',df.fillna(method='ffill'))
print('\n fill missing values with fillna(method="bfill") :\n',df.fillna(method='bfill'))

df['Usia']=df['Usia'].fillna(0)

print('\n fill missing values in columns "Usia" with 0 :\n',df)

# interpolation
print('\n --interpolation--\n')
df['Pendapatan']=df['Pendapatan'].interpolate(method='linear')

print('\n fill missing values in columns "Pendapatan" with interpolation(method="linear") :\n',df)

# data transformations
print('\n ------data transformations-----\n')

# renaming columns
print('\n --rename columns--\n')
df=df.rename(columns={'Usia':'Age'})
print('\n rename columns "Usia" to "Age":\n',df)

# changing types
print('\n --changing types--\n')
print('\n dataframe info :\n')
print(df.info())
df['Pendapatan']=df['Pendapatan'].astype(int)
print('\n dataframe info after change type column "pendapatan" from float to int :\n')
print(df.info())

df['Tanggal'] = pd.to_datetime(df['Tanggal'])

print('\n change type column "Tanggal" from object(because string in info read as object) to datetime :\n')
print(df.info())

# create and modify columns
print('\n --create and modify columns--\n')

df['Pajak'] = (df['Pendapatan'] * 10) / 100 # pajak = 10%

print('\n create columns "Pajak" where the values from column "Pendapatan" devided by 10:\n',df)

# combine and merge DataFrame 
print('\n ------combine and merge DataFrame -----\n')

data1 = {
    'id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 40]
}

df1 = pd.DataFrame(data1)

data2 = {
    'id': [3, 4, 5, 6],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'salary': [70000, 80000, 60000, 75000]
}

df2 = pd.DataFrame(data2)

print('\n initial dataframe df1 :\n',df1)
print('\n initial dataframe df2 :\n',df2)

print('\n --concat--\n')
combine_df1 = pd.concat([df1,df2],axis=0)
combine_df2 = pd.concat([df1,df2],axis=1)
print('\n combine df1 and df2 with concat with axis=0:\n',combine_df1)
print('\n combine df1 and df2 with concat with axis=1:\n',combine_df2)

print('\n --merge--\n')

merge_df1 = pd.merge(df1,df2,on='id')

print('\nmerge dataframe with on="id":\n',merge_df1)

merge_df2 = pd.merge(df1,df2,on='id',how='left')

print('\nmerge dataframe with how="left" on="id":\n',merge_df2)

merge_df2 = pd.merge(df1,df2,on='id',how='right')

print('\nmerge dataframe with how="right" on="id":\n',merge_df2)

merge_df3 = pd.merge(df1,df2,on='id',how='outer')

print('\nmerge dataframe with how="outer" on="id":\n',merge_df3)

merge_df3 = pd.merge(df1,df2,on='id',how='inner')

print('\nmerge dataframe with how="inner" on="id":\n',merge_df3)


# join dataframe
print('\n --join--\n')
# join combine dataframe with indexing so we must set index for each dataframe
df1.set_index('id', inplace=True)
df2.set_index('id', inplace=True)

join_df1 = df1.join(df2,how='inner')
print('\njoin dataframe with how="inner":\n',join_df1)
join_df2 = df1.join(df2,how='outer')
print('\njoin dataframe with how="outer":\n',join_df2)
join_df3 = df1.join(df2,how='left')
print('\njoin dataframe with how="left":\n',join_df3)
join_df4 = df1.join(df2,how='right')
print('\njoin dataframe with how="right":\n',join_df4)

#  exercise

print('\n ---- exercise ----\n')
print('\n -- handling missing values and renaming columns --\n')


import pandas as pd
import numpy as np 

data_exer = {
    "Name": ['Alice', 'Bob',np.nan,'David'],
    "Age": [25,np.nan,30,35],
    "Score":[85,90,np.nan,88]
}

df_exer = pd.DataFrame(data_exer)

print('\n initial originall dataframe:\n', df_exer)

df_exer['Age'] = df_exer['Age'].fillna(df_exer['Age'].mean())
df_exer['Score'] = df_exer['Score'].interpolate()

print('\n fill "Age" column with mean values and "Score" column with interpolate:\n',df_exer)

df_rename = df_exer.rename(columns={'Name':'Student_Name','Score':'Exam:Score'})

print('\n rename columns in dataframe :\n',df_rename)


print('\n -- merge two dataset and perform data transformation --\n')

df1_exer = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
})

df2_exer = pd.DataFrame({
    "ID": [1, 2, 3],
    "Score": [85, 90, 88],
})

print('\n initial dataset 1:\n', df1_exer)
print('\n initial dataset 2:\n', df2_exer)

merge_df_exer = pd.merge(df1_exer, df2_exer,how='inner',on='ID')

print('\nmerge dataframe with how="inner" on="ID":\n',merge_df_exer)

merge_df_exer['Score_percentage'] = (merge_df_exer['Score'] * 100) / 100

print('\n transform dataset :\n',merge_df_exer)

print('\n ---- practice ----\n')

# Contoh dataset
df1 = pd.DataFrame({
    "ID": [1, 2, 3,4],
    "Name": ["Alice", "Bob", "Charlie",'lukas'],
    "Age": [25, 30, 35,20],
    "Gender":['female',np.nan,np.nan,np.nan]
})

df2 = pd.DataFrame({
    "ID": [1, 2, 3,4],
    "Score": [85, 90, 88,99]
})

df3 = pd.DataFrame({
    "ID": [1, 2, 3,4],
    "City": ["New York", "Los Angeles", "Chicago","New York"]
})

print('\n initial dataset 1:\n', df1)
print('\n initial dataset 2:\n', df2)
print('\n initial dataset 3:\n', df3)

# Drop columns dengan lebih dari 50% nilai yang hilang
threshold = 0.5 * len(df1)
df_cleaned = df1.dropna(thresh=threshold, axis=1,inplace=True)
print("Data setelah drop kolom dengan lebih dari 50% nilai yang hilang:")
print(df_cleaned)

# Merge ketiga dataset
merge_df1df2= pd.merge(df1, df2, on="ID",how='inner')
merged_df = pd.merge(merge_df1df2, df3, on="ID",how='inner')

# Analisis hubungan sederhana
print("Data hasil penggabungan:")
print(merged_df)
print("\nRata-rata skor berdasarkan kota:")
print(merged_df.groupby("City")["Score"].mean())

# One-hot encoding
df_Onehot = pd.get_dummies(merged_df, columns=["City"], prefix="City")
print("\nData setelah one-hot encoding:")
print(df_Onehot)
