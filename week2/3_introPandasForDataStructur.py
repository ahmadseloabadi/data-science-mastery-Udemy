# -> pandas
# *pandas is powerful python library for manupalation and analysis

# -> pandas data structures
# --> series 
# --> dataframes 

print('\n -----Pandas------\n')
print('\n -----Pandas data structur------\n')
import pandas as pd

pandas_series = pd.Series([10,20,30], index=['a','b','c'])

print('\ninitial pandas series :\n',pandas_series)

data={"Name":["sungep","luna"],"age":[20,25]}
df = pd.DataFrame(data)
print('\ninitial pandas dataframe :\n',df)

# loading data from csv,exel,and other source files
print('\n -----Pandas loading data------\n')

file_csv=pd.read_csv('week2/data/contoh_file.csv')

print('\n load data csv with pandas : \n',file_csv)

file_excel=pd.read_excel('week2/data/contoh_file.xlsx')

print('\n load data xlsx with pandas : \n',file_excel)

print('\n -----Pandas save data------\n')

# Membuat data
data2 = {
    'Nama': ['Andi', 'Budi', 'Citra', 'Dewi'],
    'Umur': [25, 30, 22, 27],
    'Pekerjaan': ['Programmer', 'Desainer', 'Dokter', 'Guru'],
    'Gaji': [7000000, 8000000, 10000000, 6000000]
}

# Membuat DataFrame
df2 = pd.DataFrame(data2)

print('\n intial data :\n',df2)

path_csv = 'week2/data/save_data_csv.csv'
path_excel = 'week2/data/save_data_excel.xlsx'

df2.to_csv(path_csv)
print('\n success save data to csv on ' + path_csv)
df2.to_excel(path_excel)
print('\n success save data to excel on ' + path_excel)

# view dataframe 

print('\n --view dataframe-- \n')

print('\n view first 2 data in dataframe with head() :\n',df2.head(2))
print('\n view last 2 data in dataframe with head() :\n',df2.tail(2))

print('\n view info of dataframe with info() :\n' )
print(df2.info())
print('\n view info of dataframe with describe() :\n')
print(df2.describe())

# data frame operation
print('\n--dataframe operation--\n')

# selecting columns from dataframe

print('\n select columns "Nama" and "Gaji"  from dataframe:\n',df2[['Nama', 'Gaji']])

# filtering columns from dataframe

print('\n filter values in the "Umur" column are less than 26:\n',df2[df2['Umur'] < 26])

# selecting by position

print('\n select first rows values by position with iloc[0]:\n',df2.iloc[0])
print('\n select first columns values by position with iloc[:,0]]:\n',df2.iloc[:,0])
print('\n select first rows values by position with iloc[0,:]]:\n',df2.iloc[0,:])
# iloc[rows,columns]

# selecting by label
print('\nselect first rows values by label with loc[0]\n',df2.loc[0])
print('\nselect all rows values and columns "Gaji" by label with loc[:,"Gaji"]\n',df2.loc[:,"Gaji"])
print('\nselect rows 2,3 and columns "Name" and "Gaji" by label with loc[[2,3],["Nama","Gaji"]]\n',df2.loc[[2,3],["Nama","Gaji"]])
# Filter rows using conditions
print("\nFilter rows using conditions where values in the 'Umur' column are less than 26 by label with loc[df2['Umur'] < 26]:\n",df2.loc[df2['Umur'] < 26])

# exercise

print('\n ---- exercise ----\n')

# load dataset
# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

data_exer= pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# explore structure
print('\n explore structure of dataset\n')

print('first 5 rows of dataset:\n', data_exer.head())
print('last 5 rows of dataset:\n', data_exer.tail())

print('\n view info of dataset with info() :\n' )
print(data_exer.info())
print('\n view info of dataset with describe() :\n' )
print(data_exer.describe())

# select spesific columns and filter rows

selected_columns = data_exer[['species','sepal_length']]

print("\nselected columns 'species' and 'sepal_length' :\n ",selected_columns)

# filter selected columns where sepal_length is greater than 5.0

filtered_columns = selected_columns[(selected_columns["sepal_length"]>5.0) & (selected_columns["species"]=="setosa")]

print("\nfiltered select columns where sepal_length is greater than 5.0 and species values is setosa:\n",filtered_columns)

filter_columns_loc =data_exer.loc[(data_exer['sepal_length']>5.0) & (data_exer['species']=='setosa'),['species','sepal_length']]
print("\n do all job before with loc[(data_exer['sepal_length']>5.0) & (data_exer['species']=='setosa'),['species','sepal_length']]:\n",filter_columns_loc)




