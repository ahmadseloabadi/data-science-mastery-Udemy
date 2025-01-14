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

# Gaussian Distribution (Normal Distribution)
# - Used in Gaussian Naive Bayes: Assumes features follow a Gaussian distribution.
# - Used in Kernel Density Estimation: For non-parametric density estimation.
# Example: Classifying continuous features like age, height, etc., in Gaussian Naive Bayes.

# Bernoulli Distribution
# - Used for binary classification problems.
# - Example: Spam detection (spam or not spam), churn prediction (yes or no).
# - Model: Bernoulli Naive Bayes is specifically designed for binary data.

# Binomial Distribution
# - Used in Logistic Regression to model binary outcomes (success/failure).
# - Example: Predicting whether a customer will make a purchase (yes or no).

# Poisson Distribution
# - Models count data or events that occur within a fixed interval.
# - Example: Predicting the number of website clicks, the number of customer arrivals in a store.
# - Applications: Poisson regression is often used for such tasks.

# Exponential Distribution
# - Used to model the time until an event occurs (e.g., failure rates in reliability analysis).
# - Example: Predicting the time between user interactions on a website.

# Uniform Distribution
# - Used to model a distribution where all outcomes are equally likely.
# - Example: Random search in hyperparameter tuning (randomly sampling values within a range).

# General Notes:
# These distributions form the foundation for many machine learning algorithms and models.
# Understanding their use cases helps in selecting the right model or approach for a given problem.


