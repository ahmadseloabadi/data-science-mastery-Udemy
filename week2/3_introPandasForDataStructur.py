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







