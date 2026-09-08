"""
Assignment: Create at least four NumPy‑arrays:
a 1D‑array with arbitrary integers
a 2D‑array (3x3) with integers
a sequence with np.arange
a 2D‑array with random integers (np.random.randint)
Calculate:
sum of all elements in an array
sum per row and per column för the 2d-arrays
Mean value for at least two of the arrays
Filter:
All values greater tha a number (>5 or >20)
All even numbers in an array
All values in a interval (f.ex. 10–30)
"""

import numpy as np

a = np.array([0,1,5,8,9,6,5,3])
print(a)
b = np.array([[5,6,9,0],[3,1,4,7]])
print(b)
c = np.arange(8).reshape(2,4)
print(c)
d = np.random.randint(0,10, size = (2,4))
print(d)

print(f"the sum of a is: {np.sum(a)}")
print(f"the sum of b is: {np.sum(b)}")
print(f"the sum of c is: {np.sum(c)}")
print(f"the sum of d is: {np.sum(d)}")
print(f"the row sum of a is: {a.sum(axis=0)}")
print(f"the column sum of b is: {b.sum(axis=0)}")
print(f"the row sum of b is: {b.sum(axis=1)}")
print(f"the column sum of c is: {c.sum(axis=0)}")
print(f"the row sum of c is: {c.sum(axis=1)}")
print (f"the column sum of d is: {d.sum(axis=0)}")
print (f"the row sum of d is: {d.sum(axis=1)}")
print(f"the mean value of a is: {np.average(a)} ")
print(f"the mean value of d is: {np.average(d)}")
print(f"in a, these numbers are greater than 5: {a[a > 5]}")
print(f"in b, these är the even numbers: {b[b % 2 == 0]}")
print(f"in c these are numbers between 2 and 5: {c[(c >= 2) & (c <= 5)]}")
"""
combine:
calculate the sum and mean of the filtered values
count how many values that meets every condition
(Extra) Filter rows in a 2D‑array based on row sum
"""
print(np.sum(a[a > 5]))
print(np.average(a[a > 5]))
count = np.sum(a > 5)
print(count)
print ((c[c.sum(axis=1) > 20]).sum())
