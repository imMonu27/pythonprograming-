# remove a given word from a string and stop it at the time 
# a = ['amol','bappi','rahul','karan']

a = ["amol","bappi","rahul","karan"]
def word():
    for i in range(a):
        return a
b = a.remove("bappi")
print ("word is romove ")
print(a)

# or

# using strip function this function clear the blank spaces.

def remove (string,word):
    newstr=string.replace(word,"  ")
    return newstr.strip()
this="   harry is a good boy  "
n=remove(this,"harry")
print(n)