import matplotlib.pyplot as plt

# basic plot

# line plot 

x = [1,2,3,4]
y = [10,20,30,40]

plt.plot(x,y,label= 'trend')
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

