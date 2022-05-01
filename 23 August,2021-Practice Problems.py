"""
Print the volume of a cylinder
"""

print("Calculate the volume of cylinder-")
a=eval(input('Radius='))
b=eval(input('Height='))
c=a**2*b*3.14
print("volume of cylinder =",round(c,2))

"""Print the volume of a cone"""

print("Calculate the volume of cone-")
d=eval(input('Radius='))
e=eval(input('Height='))
f=(d**2*e*3.14)/3
print("Volume of cone =",round(f,2))

"""Convert the distance given in kms to miles"""

print("Convert kilometers to miles")
g=eval(input('value in kms='))
h=g/1.609
print("Value in miles=",round(h,2))

"""Convert the weight given in kilograms to pound and vice versa"""

print("Convert kg to lbs-")
i=eval(input('Value in kgs='))
j=i*2.205
print("Value in lbs=",round(j,2))

print("Convert lbs to kg-")
k=eval(input('Value in kg='))
l=k/2.205
print("Value in kg=",round(l,2))

"""Print the types of variables after taking values from use at run time"""

m=eval(input('Enter value='))
n=eval(input('Enter value='))
o=eval(input('Enter value='))
p=eval(input('Enter value='))
print(type(m))
print(type(n))
print(type(o))
print(type(p))