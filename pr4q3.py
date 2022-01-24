# find spam comment following words
# make a lot of money, buy this, subscribe this, click this, detect this all words as a spam.

text= input("enter text \n")
if("make a lot of money"in text):
    spam= True
elif("click this"in text):
    spam=True
elif("subscribe this"in text):
    spam=True
else:
    False
if(spam):
    print("this text is spam")
else:
    print("this text is not spam")