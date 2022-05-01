#Program to find the student with minimum CGPA
cgpa=[]
name=[]
n=int(input("The number of students="))
for i in range(n):
    student_name=input('Enter the student name-')
    name.append(student_name)
    CGPA=float(input('Enter the CGPA of the student='))
    cgpa.append(CGPA)
print()
for y in range(n):
    print("Name-",name[y],' ','CGPA=',cgpa[y])
print()
MIN=cgpa[0]
for x in cgpa:
    if (MIN>x):
        MIN=x
a=cgpa.index(MIN)
print("The student with minimum CGPA is-",name[a])