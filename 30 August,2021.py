#Program to check if the given input is positive or negative
print("Program to check if the given input is positive or negative")
a=int(input('Enter value='))
if(a>=0):
    print("Value is positive")
if(a<=0):
    print("Value is negative")

#Program to check if the given input is even or odd
print("Program to check if the given input is even or odd")
b=int(input('Enter value='))
if(b%2==0):
    print("Value is even")
else:
    print("Value is odd")

#Program to check the largest value from the given value
print("Program to check the largest value from the given value")
c=int(input('Enter value of A='))
d=int(input('Enter value of B='))
e=int(input('Enter value of C='))
if(c>d and c>e):
    print("A is largest")
elif(d>e):
    print("B is largest")
else:
    print("C is largest")

#Program to check if the year is leap year or not
print("Program to check if the year is leap year or not")
f=int(input('Enter year='))
if(f%100==0 and f%400==0):
    print(f,"is laep year")
else:
    print(f,"is not a leap year")

#Program to check if the given input is even or not withoutusing modulus operator
print("Program to check if the given input is even or not withoutusing modulus operator")
g=int(input('Enter value='))
if(g&1==1):
    print("The value is odd")
else:
    print("The value is odd")

#Program to print the sum of series from 1...N
print("Program to print the sum of series from 1...N")
h=int(input('Enter the value of N='))
sum=0
for x in range(1,h+1):
    sum=sum+x
print("Sum of series from 1...N=",sum)