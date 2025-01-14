#  probability basic

# conditional probability

def bayes_theorema(prior, likelihood,evidence):
    return (likelihood + prior) / evidence


# common probability distribution 

# gaussian distribution
import numpy as np
import matplotlib.pyplot as plt

mu , sigma = 0,1
x= np.linspace(-4,4,100)
y = (1 / (np.sqrt(2* np.pi * sigma**2))) * np.exp(-0.5 * ((x - mu) / sigma)**2)

plt.plot(x,y)
plt.title('gaussian distribution')
plt.show()

# bernouli ditribution

p = 0.6
plt.bar([0,1],[1-p,p],color='blue')
plt.title('bernouli ditribution')
plt.xticks( [0,1],labels = ["0 (failure)", "1 (success)"])
plt.show()

# binomial distribution

from scipy.stats import binom

n, p =10 ,0.5
x = np.arange(0,n+1)
y = binom.pmf(x,n,p)

plt.bar(x,y,color='green')
plt.title('binomial distribution')
plt.show()

# poisson distribution
from scipy.stats import poisson

lam = 3
x = np.arange(0,10)
y = poisson.pmf(x,lam)
plt.bar(x,y,color='black')
plt.title('poisson distribution')
plt.show()

