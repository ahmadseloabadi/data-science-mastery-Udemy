import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

print('\n initial dataset:\n',df.head())

print('\n dataset info with info():\n')
print(df.info())

print('\n dataset info with describe():\n')
print(df.describe())

# handle missing values
df['Age'] = df['Age'].fillna(df['Age'].median())

print('\n fill Age column with median values:\n',df['Age'])

df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0]) # mode() digunakan untuk menghitung modus, yaitu nilai yang paling sering muncul dalam kolom Embarked dan [0] adalah nilai pertama dari hasil mode(), yang merupakan nilai modus utama

print('\n fill Embarked column with .mode()[0] :\n',df['Embarked'])

# remove duplicates

df = df.drop_duplicates()

print('\n remove duplicates in dataset :\n',df)

print('\n info dataset after removing duplicates:\n')
print(df.info())

# filter data :  passanger in first class

first_class= df[df['Pclass'] == 1]

print('\n filter passanger in first class:\n', first_class)

# visualing data 

# bar chart : survival rate by class

survival_by_class = df.groupby('Pclass')['Survived'].mean()

survival_by_class.plot(kind='bar',color='blue')
plt.title('survival rate by class')
plt.ylabel('survival rate')
plt.show()

# histogram : age distribution

sns.histplot(df['Age'],kde=True,bins=20,color='purple')
plt.title('Age distribution')
plt.xlabel('Age')
plt.ylabel('frequency')
plt.show()

# scatter plot : age vs fare
plt.scatter(df['Age'],df['Fare'],alpha=0.5,color='green')
plt.title('Age vs fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()

# Titanic Dataset EDA Report
# 1. Overview
    # - Dataset contains 891 rows and 12 columns.
    # - Missing values handled for 'Age' (filled with median) and 'Embarked' (filled with
    # mode).
# 2. Key Insights:
    # - Survival rates are highest for first-class passengers (62%) and lowesr for
    # third-class customers (24%)
    # - Majority of passengers are aged between 20-40 years
    # A positive correlation exists between fare and survival
# 3. Visual Insights:
    # - Screenshots