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