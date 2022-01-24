# edit the format 
letter='''DEAR <|NAME|>
        YOUR HIRED FOR THIS JOB
        CONGRAGULATIONS!
        DATE:<|DATE|>'''
NAME=input("enter your name:\n")
date=input("enter date:\n")
letter=letter.replace("<|NAME|>",NAME)
letter=letter.replace("<|DATE|>",date)
print(letter)