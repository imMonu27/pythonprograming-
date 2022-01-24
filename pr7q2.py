'''game function is a programme lets a uset play a game and return the 
    the score as an integer. you need to tead a file "hi-score.txt" which is
    either blank or contains the previous hi score you need to write a programme
    to update the hi-score wheather game() breaks the hi-score  '''

def game():
    return 30
score=game()
with open("hi-score.txt",'r') as f:
    hi_score=f.read()
if hi_score =='':
    with open("hi-score.txt",'w')as f:
        f.write(str(score))
elif int(hi_score)<score:
    with open("hi-score.txt",'w')as f:
        f.write