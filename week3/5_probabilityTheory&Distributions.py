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
plt.bar(x,y,color='orange')
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

# exercise
# calculate probability using bayes theorema
# Problem
# - A disease affects 1% of a population
# - A test is 95% accurate for diseased individuals and 90% accurate for non-diseased individuals 
# - Find the probability of having the disease given a positive test result

def bayes_theorema(prior, sensitivity,specificity):
    evidence = (sensitivity * prior) + ((1 - specificity) * (1 - prior))
    posterior = (sensitivity * prior) / evidence
    return posterior


prior = 0.01 # 1% prevalence
sensitivity = 0.95 # True positive rate
specificity = 0.90 # True negative rate

posterior = bayes_theorema(prior, sensitivity,specificity)
print('\nprobability of disease given positive test :',posterior)

# exercise 2

# plot end explore different probability distribution
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson
# Gausian Distribution
x = np.linspace (-4, 4, 100)
y = norm.pdf(x, loc=0, scale=1)
plt.plot(x, y, label="Gaussian")
plt.title("Gaussian Distribution")
plt.show()

# Binomial Distribution
n, p = 10, 0.5
x = np.arange(0, n+1)
y = binom.pmf(x, n, p)
plt.bar(x, y, label="Binomial")
plt.title("Binomial Distribution")
plt.show()

# Poisson Distribution
lam =3
x = np.arange(0, 10)
y = poisson.pmf(x, lam)
plt.bar(x, y, label="Poisson")
plt.title("Poisson Distribution")
plt.show()

# practice

print('\n Create and visualize a multinomial distribution for multi-class data\n')
import numpy as np
import matplotlib.pyplot as plt

# Parameters for the multinomial distribution
n = 100  # Number of trials
p = [0.2, 0.3, 0.5]  # Probabilities for each class (must sum to 1)

# Generate random samples from multinomial distribution
samples = np.random.multinomial(n, p, size=500)

# Visualize the distribution
class_labels = ['Class A', 'Class B', 'Class C']
averages = np.mean(samples, axis=0)

plt.bar(class_labels, averages, color=['blue', 'green', 'red'])
plt.title("Multinomial Distribution - Average Class Frequencies")
plt.xlabel("Classes")
plt.ylabel("Average Frequency")
plt.show()

print('\nCompare Gaussian and uniform distributions for continuous data\n')

# Generate Gaussian data
mu, sigma = 0, 1  # Mean and standard deviation
gaussian_data = np.random.normal(mu, sigma, 1000)

# Generate Uniform data
low, high = -3, 3  # Range for uniform distribution
uniform_data = np.random.uniform(low, high, 1000)

# Plot both distributions
plt.figure(figsize=(10, 5))

# Gaussian Distribution
plt.hist(gaussian_data, bins=30, alpha=0.7, label='Gaussian (Normal)', color='blue', density=True)

# Uniform Distribution
plt.hist(uniform_data, bins=30, alpha=0.7, label='Uniform', color='orange', density=True)

plt.title("Comparison of Gaussian and Uniform Distributions")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.show()

print('\nUse probability distributions to simulate and analyze real-world datasets\n')
# Simulate website clicks using Poisson distribution
lambda_ = 5  # Average number of clicks per minute
poisson_data = np.random.poisson(lambda_, 1000)

# Analyze the data
mean_clicks = np.mean(poisson_data)
std_clicks = np.std(poisson_data)

# Visualize the distribution
plt.hist(poisson_data, bins=15, alpha=0.7, color='green', density=True)
plt.title("Simulated Website Clicks - Poisson Distribution")
plt.xlabel("Number of Clicks")
plt.ylabel("Probability Density")
plt.axvline(mean_clicks, color='red', linestyle='dashed', linewidth=1, label=f"Mean = {mean_clicks:.2f}")
plt.legend()
plt.show()
