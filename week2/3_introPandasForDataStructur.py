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










