# Program-1 Calculate the simple interest
p = 1000
t = 5
r = 0.5
si = (p*r*t)/100
print("Simple Interest", si)

"""Pogram-2 Convert temperture from farenheit to celcius"""

f = 100
c = (f-32)*5/9
print("Temperature in celcius", round(c, 2))

"""Program to swap(interchange) the value of two variables(X,Y) using a third variable temp """

X = 10
Y = 15
print("Before Swapping X=", X)
print("Before Swapping Y=", Y)
temp = X
X = Y
Y = temp
print("After Swapping X=", X)
print("After Swapping Y=", Y)

"""Program to interchange the values of two variables (A,B) without using a third variable"""

A = 20
B = 30
print("Before Swapping A=", A)
print("Before Swapping B=", B)
A = A+B
B = A-B
A = A-B
print("After Swapping A=", A)
print("After Swapping B=", B)

"""Use of input function"""

A = int(input('Enter the value of A='))
Sqr = A**2
print("Square of A=", Sqr)

"""Program to add two numbers using input"""

A = eval(input('Enter the value of A='))
B = eval(input('Enter the value of B='))
C = A+B
print("The sum of A and B is C=", round(C, 3))

"""To calculate the average and percentage"""

S1 = eval(input('Enter the value of S1='))
S2 = eval(input('Enter the value of S2='))
S3 = eval(input('Enter the value of S3='))
S4 = eval(input('Enter the value of S4='))
S5 = eval(input('Enter the value of S5='))
Total = S1+S2+S3+S4+S5
A = (S1+S2+S3+S4+S5)/5
P = (S1+S2+S3+S4+S5)*100/500
print("Total Marks=", Total)
print("Average Marks=", round(A, 1))
print("Percentage=", round(P, 2))
