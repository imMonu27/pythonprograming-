# create a dictionary of hindi words with values as their english translation provide user with option
mydict={'tv':'durdarshan',
'radio':'aakashvani',
'mobile':'durdvani',
}
print("options are",mydict.keys())
a=input("enter the word you want know meaning:\n")
print(mydict.get(a))
