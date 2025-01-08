import pandas as pd

# Membuat dataset contoh
data = {
    "EmployeeID": [1, 2, 3, 4, 5, 6],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Department": ["HR", "IT", "HR", "Finance", "IT", "Finance"],
    "Salary": [5000, 7000, 6000, 8000, 7500, 8200],
    "Age": [25,34,45,56,23,43]
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
print(df.groupby('Department').agg({'Salary':['mean','max','min','std','count','sum'],'Age':['mean','max','min','std','count','sum']}))


# practice

# Membuat dataset penjualan
data = {
    "Region": ["North", "South", "East", "West", "North", "South", "East", "West"],
    "Product Category": ["Electronics", "Electronics", "Furniture", "Furniture", "Clothing", "Clothing", "Electronics", "Furniture"],
    "Year": [2020, 2020, 2020, 2020, 2021, 2021, 2021, 2021],
    "Sales": [2000, 3000, 1500, 4000, 2500, 3500, 2000, 4500]
}

df = pd.DataFrame(data)
print(df)

# Group by Region
grouped_by_region = df.groupby("Region")["Sales"].sum()
print("Total Penjualan Berdasarkan Region:")
print(grouped_by_region)

# Group by Product Category
grouped_by_category = df.groupby("Product Category")["Sales"].sum()
print("\nTotal Penjualan Berdasarkan Product Category:")
print(grouped_by_category)

# Pivot table: Total sales per region and per year
pivot_sales = df.pivot_table(values="Sales", index="Region", columns="Year", aggfunc="sum")
print("\nPivot Table (Total Sales per Region and Year):")
print(pivot_sales)

# Custom aggregation function for variance
def calculate_variance(series):
    return series.var()

# Group by Region and calculate variance
variance_by_region = df.groupby("Region")["Sales"].apply(calculate_variance)
print("\nVariansi Penjualan Berdasarkan Region:")
print(variance_by_region)

# Group by Product Category and calculate variance
variance_by_category = df.groupby("Product Category")["Sales"].apply(calculate_variance)
print("\nVariansi Penjualan Berdasarkan Product Category:")
print(variance_by_category)
