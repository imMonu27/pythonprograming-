# replace words in words to ###### to be censored

words=["donkey","kaddu","mote","chote"]
with open('example.txt')as f:
    content=f.read()
for words in words:
    content=content.replace(words,"######")
with open("example.txt","w")as f:
    f.write(content)
    f.close()