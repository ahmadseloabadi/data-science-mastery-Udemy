# handling missing values
# method for handling missing values
# --> drop missing values
# --> fill missing values
# --> interpolation

print('\n--- Handling missing values----\n')

import pandas as pd

# Membuat DataFrame dengan nilai kosong (NaN)
data = {
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

df['Usia']=df['Usia'].fillna(0,inplace=False)

print('\n fill missing values in columns "Usia" with 0 :\n',df)

# interpolation
print('\n --interpolation--\n')
df['Pendapatan']=df['Pendapatan'].interpolate(method='linear')

print('\n fill missing values in columns "Pendapatan" with interpolation(method="linear") :\n',df)




