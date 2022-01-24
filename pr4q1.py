# find greatest no of 4 enter by user
a=int(input("enter no 1:\n"))
b=int(input("enter no 2:\n"))
c=int(input("enter no 3:\n"))
d=int(input("enter no 4:\n"))
if(a>d):
    f1=a
else:
    f1=d
if(b>c):
    f2=b
else:
    f2=c
if(f1>f2):
    print("greatest no is",f1)
else:
    print("greatest no is",f2)