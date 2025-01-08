import matplotlib.pyplot as plt

# basic plot

# line plot 

x = [1,2,3,4]
y = [10,25,15,30]

plt.plot(x,y,label= 'trend',color='orange',linestyle='--',marker='o')
plt.title('line plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()

# bar chart
categories = ['A','B','C','D']
values = [10,20,7,15]

plt.bar(categories,values,color='blue')
plt.title('bar chart')
plt.show()

# histrogram 

data = [1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5]
plt.hist(data,bins=4,color='red',edgecolor='black')
plt.title('histogram')
plt.show()

# scatter plot

x1 = [1,2,3,4,5,6]
y1 = [10,11,14,20,34,45]

plt.scatter(x1,y1,color='green')
plt.title('scatter plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(['dataset 1'])
plt.show()

import seaborn as sns
import numpy as np
import pandas as pd

data_sns = np.random.rand(5,5)
sns.heatmap(data_sns,cmap='coolwarm',annot=True)
plt.title('heatmap')
plt.show()

data = {
    "Age": [25, 30, 35, 40, 22, 28, 45, 38, 33, 26],
    "Income": [50000, 60000, 75000, 90000, 48000, 58000, 100000, 85000, 72000, 52000],
    "Score": [80, 70, 85, 95, 60, 75, 90, 88, 82, 78],
    "Gender": ["Male", "Female", "Female", "Male", "Female", "Male", "Male", "Female", "Male", "Female"]
}

df = pd.DataFrame(data)

print(df)

# Membuat pair plot
sns.pairplot(df, hue="Gender", diag_kind="kde", palette="Set2")

# Menampilkan plot
plt.show()


# exercise

data_exer= pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

print('first 5 rows of dataset:\n', data_exer.head())

del data_exer['species'] # delete species because type is not numbers

# calculate correlation
corr_matrix = data_exer.corr()

# plot heatmap correlation

sns.heatmap(corr_matrix,annot=True,cmap='coolwarm')
plt.title('Heatmap correlation')
plt.show()







