num=int(input("enter no:\n"))

for i in range(0,num):
        for j in range(0,num):
            if i==0 or j==0 or j==num-1 or i==num-1:
                print("*",end="")
            else:
                print("",end="")
        print()
