# keys in dictionay 
mydict={'name':'john',
'fast':'in a quick manner',
'mohit':'a coder',
'anotherdict':{'harry':'player'},
'mark':[1,2,3]
}
print(mydict.keys())
# update dictionar 
updatedict={'lovish':'friend',
'diva':'a mad'}
mydict.update(updatedict)
print(mydict)

# values in dictionary
print(mydict.values())

#iteams print the key, value for all contents of all dictionary
print(mydict.items())

# get func is find keys value
print(mydict.get('mohit'))
'''we can print the key simply like print(mydict[mohit])but
    there is a problame what we write in square braket is our 
     responsibility  and if you write key then program shows an error
     but if we use get func then it show not error it print simply none 
     if key is not available '''