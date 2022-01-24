# this program is write by mohit
'''a=int(input("enter your marks:\n"))
b=int(input("enter your marks:\n"))
c=int(input("enter your marks:\n"))

markssum = a+b+c/3*100
if(markssum>=40):
    print("your pass")
if(a>=35):
    print("pass in subject")
else:
    print("fail in subject")
if(b>=35):
    print("pass in subject")
else:
    print("fail in subject")
if(c>=35):
    print("pass in subject")
else:
    print("fail in subject")'''
# this is code with harry code
a=int(input("enter your marks:\n"))
b=int(input("enter your marks:\n"))
c=int(input("enter your marks:\n"))
if(a<35 or b<35 or c<35):
    print("your are fail in subject")
elif(a+b+c)/3<40:
    print("your are fail in exam")
else:
    print("you pass exam")