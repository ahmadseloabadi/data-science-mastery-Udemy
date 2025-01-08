import pandas as pd

# Membuat dataset contoh
data = {
    "EmployeeID": [1, 2, 3, 4, 5, 6],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Department": ["HR", "IT", "HR", "Finance", "IT", "Finance"],
    "Salary": [5000, 7000, 6000, 8000, 7500, 8200]
}

df = pd.DataFrame(data)
print("\nintial Dataset:\n",df)

# Grouping berdasarkan kolom 'Department'
grouped = df.groupby("Department")

for name,group in grouped:
    print('\n name: \n',name)
    print('\n group:\n',group)


print('\n mean group Department:\n',grouped.mean())

print('\n sum group Department:\n',grouped.sum())

#  melihat rata-rata gaji pada setiap department
print('\n mean group Department by salary:\n',df.groupby('Department')['Salary'].mean())
# aggregate functions

print('\n mean,max,min,std,count,sum group of department by salary with aggregate:\n')
print(df.groupby('Department').agg({'Salary':['mean','max','min','std','count','sum']}))


