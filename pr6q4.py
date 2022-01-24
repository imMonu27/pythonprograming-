# print recursive function to calculate the sum of first n natural number 

def sum(n):
    if n<=1:
        return n
    else:
        return n + sum(n-1)
    
n=16
if n<0:
    print("enter a positive number ")
else:
    print("the sum is ",sum(n))
# n! = (n-1)! * n 
# sum(n) = sum(n-1) + n