# find number is prime or not 

'''num=int(input("enter no\n"))
if(num/num or num/1):
    print("number is  prime ")
else:
    print("number is not prime")'''

# code with harry 

num=int(input("enter no\n"))
prime=True
for i in range(2,num):
    if (num%i==0):
        prime=False
        break
    if prime:
        print("this number is prime")
    else:
        print("this is not prime number")