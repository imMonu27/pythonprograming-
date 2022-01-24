# username contain less than 10 character or not write program

a = input("enter your username\n")
b = len(a)
print(b)
if(len(a)<10):
    print("its less than 10 character")
else:
    print("its not less than 10 character")