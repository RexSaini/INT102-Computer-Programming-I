#Find the even values from a given array
import numpy 
a=int(input('Enter number of rows-'))
b=int(input('Enter number of columns-'))
c=numpy.arange(a*b).reshape(a,b)
for x in range(a):
    for y in range(b):
        c[x][y]=int(input('Enter input values-'))
print(c)
print("Even values from given array-")
for x in range(a):
    for y in range(b):
        if c[x][y]%2==0:           
            print(c[x][y], end=' ')