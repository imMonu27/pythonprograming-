def percent(marks):
    p = (( marks [0] + marks [1] + marks [2] + marks [3] ) / 400)*100
    return p 

marks1=[45,55,66,88]

percent1=percent(marks1)

marks2=[42,58,67,85]

percent2=percent(marks2)

print(percent1,percent2)

# function call:
# when ever we want to call a function we put the name of the function follows by paranthesis as follow  
# func 1() this is function call

# function defination:
# the part containing the exact set of instruction which are executed during the function call