# understanding integral in ml app
# to compute area under curva ,representing accumulation
# application in ml :
# - probability distribution
# - cost function 

import sympy as sp

x=sp.Symbol('x')

f=x**2

definite_integral = sp.integrate(f,(x,0,2))

indefinite_integral = sp.integrate(f,x)

print('\n definite integral:\n',definite_integral)
print('\n indefinite integral:\n',indefinite_integral)

# ---Optimization Concepts

# 1. Local vs. Global Minima
#    - Local Minimum:
#      Sebuah titik pada fungsi di mana nilai fungsi lebih rendah daripada 
#      titik-titik di sekitarnya, tetapi belum tentu merupakan nilai terendah global.
#    - Global Minimum:
#      Titik pada fungsi di mana nilai fungsi adalah yang terendah secara keseluruhan 
#      di seluruh domain fungsi.

# 2. Convex Functions
#    - Definisi:
#      Fungsi f(x) disebut convex jika memenuhi:
#      f(λx1 + (1−λ)x2) ≤ λf(x1) + (1−λ)f(x2) untuk semua λ ∈ [0, 1].
#    - Karakteristik:
#      Pada fungsi convex, setiap local minimum juga merupakan global minimum.
#      Hal ini mempermudah proses optimisasi.

# 3. Non-Convex Functions in ML
#    - Dalam machine learning, kebanyakan fungsi loss pada neural network 
#      adalah non-convex.
#    - Fungsi non-convex memiliki banyak local minima, yang membuat proses optimisasi 
#      menjadi lebih sulit dan bergantung pada teknik-teknik khusus untuk menemukan 
#      solusi yang baik.


# ----Stochastic Gradient Descent (SGD) and Its Variants

# 1. Apa itu Stochastic Gradient Descent (SGD)?
#    - SGD adalah algoritma optimasi yang menggunakan subset acak (mini-batches)
#      dari data untuk menghitung gradien dan memperbarui parameter model.
#    - Berbeda dengan batch gradient descent yang menggunakan seluruh dataset,
#      SGD bekerja pada subset kecil data untuk efisiensi.

# 2. Mengapa menggunakan SGD?
#    - SGD memungkinkan konvergensi yang lebih cepat untuk dataset besar.
#    - Dibandingkan dengan batch gradient descent, SGD lebih efisien dalam
#      menangani data skala besar.

# 3. Varian SGD:
#    - **Mini-Batch SGD**:
#      - Memperbarui parameter menggunakan mini-batches (batch kecil) 
#        daripada menggunakan satu contoh data.
#    - **Momentum**:
#      - Menambahkan sebagian kecil dari pembaruan sebelumnya ke pembaruan saat ini.
#      - Membantu mempercepat konvergensi dan menghindari osilasi.
#    - **Adam Optimizer**:
#      - Kombinasi momentum dengan kecepatan pembelajaran adaptif.
#      - Banyak digunakan karena mempercepat konvergensi secara signifikan 
#        dan cocok untuk berbagai

print('\n -- calculate integrals of simple function---\n')
# define function

x = sp.Symbol('x')
f = sp.exp(-x)

# compute indefinite integral

indefinite_integral = sp.integrate(f,x)

print('\n indefinite integral:',indefinite_integral)

# compute definite integral

definite_integral = sp.integrate(f,(x,0,sp.oo))

print('\n definite integral:',definite_integral)

print('\n -- implement stochastic gradient descent for a linear model---\n')

import numpy as np

# generate synthetic data

np.random.seed(42)

X = 2*np.random.rand(100,1)
y = 4 + 3 * X + np.random.rand(100,1)

# add bias term to X

X_b = np.c_[np.ones((100,1)),X]

# SGD implementation

def stochastic_gradient_descent(X,y,theta,learning_rate,n_epoch):
    m=len(y)
    for epoch in range(n_epoch):
        for i in range(m):
            random_index=np.random.randint(m)
            xi = X[random_index:random_index+1]
            yi = y[random_index:random_index+1]
            gradients = 2* xi.T @ (xi @ theta - yi)
            theta -= learning_rate * gradients 
    return theta

# initialize parameters

theta = np.random.randn(2,1)
learning_rate = 0.1
n_epochs =50

# perform SGD 
theta_opt = stochastic_gradient_descent(X_b,y,theta,learning_rate,n_epochs)

print('\n optimized parameters: ',theta_opt)

# practice
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Visualize the Loss Function's Surface and SGD Optimization Path
def loss_function(x, y):
    return x**2 + y**2  # Simple quadratic loss

def gradient(x, y):
    return 2 * x, 2 * y  # Gradient of the function

# Initialize variables for SGD
x, y = 5, 5  # Starting point
learning_rate = 0.1
steps = 20
path = [(x, y)]

# SGD Optimization Path
for _ in range(steps):
    grad_x, grad_y = gradient(x, y)
    x -= learning_rate * grad_x
    y -= learning_rate * grad_y
    path.append((x, y))

# Create grid for surface plot
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = loss_function(X, Y)

# Plot the surface and the optimization path
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
path = np.array(path)
ax.plot(path[:, 0], path[:, 1], loss_function(path[:, 0], path[:, 1]), color='red', marker='o')
ax.set_title("Loss Surface and SGD Optimization Path")
plt.show()

# 2. Implement Mini-Batch SGD and Compare it with Vanilla SGD
# Dataset
data_X = np.linspace(-5, 5, 100)
data_Y = 3 * data_X + 2 + np.random.normal(0, 1, 100)  # Linear data with noise

# Mini-Batch SGD
def mini_batch_sgd(X, Y, batch_size, learning_rate, epochs):
    w, b = 0, 0  # Initialize parameters
    n = len(X)
    for _ in range(epochs):
        indices = np.random.permutation(n)
        X, Y = X[indices], Y[indices]
        for i in range(0, n, batch_size):
            X_batch = X[i:i + batch_size]
            Y_batch = Y[i:i + batch_size]
            grad_w = -2 * np.mean(X_batch * (Y_batch - (w * X_batch + b)))
            grad_b = -2 * np.mean(Y_batch - (w * X_batch + b))
            w -= learning_rate * grad_w
            b -= learning_rate * grad_b
    return w, b

# Vanilla SGD
def vanilla_sgd(X, Y, learning_rate, epochs):
    w, b = 0, 0  # Initialize parameters
    for _ in range(epochs):
        for i in range(len(X)):
            grad_w = -2 * X[i] * (Y[i] - (w * X[i] + b))
            grad_b = -2 * (Y[i] - (w * X[i] + b))
            w -= learning_rate * grad_w
            b -= learning_rate * grad_b
    return w, b

# Compare both methods
mini_batch_result = mini_batch_sgd(data_X, data_Y, batch_size=10, learning_rate=0.01, epochs=100)
vanilla_result = vanilla_sgd(data_X, data_Y, learning_rate=0.01, epochs=100)

print("Mini-Batch SGD Results (w, b):", mini_batch_result)
print("Vanilla SGD Results (w, b):", vanilla_result)

# 3. Use Adam Optimizer for a More Complex Dataset
from keras.optimizers import Adam
import tensorflow as tf

# Synthetic non-linear dataset
X = np.linspace(-1, 1, 100)
Y = X**3 + 0.1 * np.random.normal(0, 1, 100)  # Non-linear data with noise

# Build a simple model in TensorFlow
model = tf.keras.Sequential([tf.keras.layers.Dense(1, input_dim=1)])
model.compile(optimizer=Adam(learning_rate=0.01), loss='mse')

# Train the model
model.fit(X, Y, epochs=100, verbose=0)

# Predict and visualize
Y_pred = model.predict(X)
plt.scatter(X, Y, label="Data")
plt.plot(X, Y_pred, color="red", label="Adam Optimizer")
plt.legend()
plt.title("Adam Optimizer on Non-Linear Data")
plt.show()
