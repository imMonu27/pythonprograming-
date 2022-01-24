# mine a log file and find out wheather it contain python

with open("log.txt")as f:
    content=f.read()
if 'python' in content:
    print("yes python is available in log")
else:
    print("python is not available in log ")