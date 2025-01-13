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

# define simple derivatives function

x = sp.Symbol('x')
f = x**3 - 5*x + 7

# compute derivatives
derivative_exer = sp.diff(f,x)

print('\n derivatives:',derivative_exer)

# define derivatives a multivariable function

x,y = sp.symbols('x y')
f = x**2 + 3*y**2 - 4*x*y
grad_x=sp.diff(f,x)
grad_y=sp.diff(f,y)

print('\ngradient:')
print('\ngradient_x:',grad_x)
print('\ngradient_y:',grad_y)