# introduction to derivatives(turunan) and their role in optimization
import sympy as sp

x = sp.Symbol('x')
f = x**2
derivative = sp.diff(f,x)

print('\n derivative:',derivative)

#  parcial derivative
x ,y= sp.symbols('x y')
f = x**2 + y**2
gradient_x = sp.diff(f,x)
gradient_y = sp.diff(f,y)

print('\n parcial derivative:',gradient_x,gradient_y)

# gradirent descent optimation algorithm

# exercise
print('\ncompute derivative of basic function\n ')

# define simple derivatives function

x = sp.Symbol('x')
f = x**3 - 5*x + 7

# compute derivatives
derivative_exer = sp.diff(f,x)

print('\n derivatives:',derivative_exer)

print('\ncompute gradient\n ')
# define derivatives a multivariable function

x,y = sp.symbols('x y')
f = x**2 + 3*y**2 - 4*x*y
grad_x=sp.diff(f,x)
grad_y=sp.diff(f,y)

print('\ngradient:')
print('\ngradient_x:',grad_x)
print('\ngradient_y:',grad_y)

print('\nimplement gradient descent for linear regression\n ')

import numpy as np

# define the gradient descent function

def gradient_descent(X,y,theta,learning_rate,iteration):
    m=len(y)
    for _ in range(iteration):
        predictions=np.dot(X,theta)
        errors=predictions - y
        gradient = (1/m) * np.dot(X.T,errors)
        theta -= learning_rate * gradient
    return theta

# sample data

X = np.array([[1,1],[1,2],[1,3]])

y = np.array([2,2.5,3.5])

theta = np.array([0.1,0.1])

learning_rate =0.1

itertion = 1000

# perform gradient descent

optimazed_theta = gradient_descent(X,y,theta,learning_rate,itertion)

print('\noptimized parameters:',optimazed_theta)



 