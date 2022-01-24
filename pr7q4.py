# replace a word in file is donkey to $#$$$$$ by updating

with open("words.txt","r")as f:
    content=f.read()
content=content.replace("donkey","#$$$$#")
with open("kutra.txt","w")as f:
    f.write(content)
    