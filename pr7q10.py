# wipe out containts of a file using python

with open("wipe.txt")as f:
    content=f.read()
with open("wipe.txt","w")as f:
    f.write(" ")
    f.close()