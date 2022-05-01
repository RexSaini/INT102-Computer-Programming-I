#Program to calculate the sum of first N natural numbers
print("Calculate the sum of first N natural numbers")
a=int(input("Enter value of N="))
sum=0
b=1
while(b<=a):
    sum=sum+b
    b=b+1
print("Sum of first N natural numbers is=",sum)

#Pogram to calculate the factorial of a given number
print("Calculate the factorial of a given number") 
c=int(input("Enter a number="))    
factorial=1    
if c<0:    
   print(" Factorial does not exist for negative numbers")    
elif c==0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,c+1):    
       factorial=factorial*i    
   print("The factorial of",c,"is",factorial)

#Program to reverse a given number
print("Revrese the given number")
d=eval(input("Enter a number="))
e=d
f=0
while d>0:
    g=d%10
    d=d//10
    f=f*10+g
print("Reverse of a number",e,"is =",f)
