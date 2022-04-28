import numpy as np
np.random.seed(101)

a = np.arange(0,10)
print(a)

a = np.arange(0,10,2)
print(a)

a = np.zeros((5,5))
print(a)

a = np.ones((5,5))
print(a)

# Create matrix of random integers.
a = np.random.randint(0,100, (5,5))
print(a)

# evenly spaced numbers within a range (start, end, number of numbers to generate)
a = np.linspace(0,100, 21)
print(a)


arr = np.random.randint(0,100,10)
print(arr)


