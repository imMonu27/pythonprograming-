# recursion is a function which cals ists self it is used to directly use a
# mathematical formula as a function 
# factorial(n)=n x factorial(n-1)
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1) 
p=factorial(4)
print(p)