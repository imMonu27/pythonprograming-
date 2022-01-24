#  read the text form a given file 'poem.txt' where contains the word twinkle.

f=open('poem.txt')
t=f.read()
if 'twinkle' in t:
    print('twinkle is present')
else:
    print("twinkle is not present")