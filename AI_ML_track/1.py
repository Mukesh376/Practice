from sympy import symbols, Eq

# Define the variables
W, T, X, W0 = symbols('W T X W0')

# Create the equation
equation = Eq(W * T * X + W0, 0)

print(equation)