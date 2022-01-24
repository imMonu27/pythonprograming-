# there is two types of file
# test file(txt,.c etc)
# binary file(jpg,.dot etc)
# opening a file
f=open('sample.txt','r')
data=f.read()
print(data)
f.close()

# we can also specify the number of character in read() fun: f.read(2)....reads first two caharachter

# We can also use f.readline () function to read on full line at time.

f=open('sample.txt')
# read first line 
data = f.readline()
print(data)

# read second line 
data = f.readline()
print(data)

# read third line 
data=f.readline()
print(data)

# read fourth line
data=f.readline()
print(data)
f.close()

# modes for opening file
# r - open for reading
# w - open for writting
# a - open for appending 
# + - open for updating

# "rb" will open for read in binary mode 
# "rt" will open for read in text mode

# writing file in python 
f=open('another.txt','w')
f.write("please write this to the file  ")
f.close( )
# if yol want to open  in file end mode text
f=open('another.txt','a')
f.write("and go to the compute and play games")
# with statement
with open("this.txt",'w')as f:
    a=f.write("me and my pc")
    print(a)