import random         #importing a random module for taking a random values  from computer

def gamewin(comp,you): #creating a game functin to determine who win
    if comp==you:
        return None

    if comp=='r':
        if you=='s':
            return False
        elif you=='p':
            return True
        
    if comp=='p':
        if you=='r':
            return False
        elif you=='s':
            return True
        
    if comp=='s':
        if you=='p':
            return False
        elif you=='r':
            return True
    


print("computer's turn: rock(r),paper(p) or sizzer(s)")
randNo = random.randint(1,3)                         #assigning values roc paper sizzer to computer through  random module
                    
if randNo==1:
    comp='r'
elif randNo==2:
    comp='s'
else:
    comp='p'

you=input("your's turn: rock(r),paper(p) or sizzer(s):")  #taking input from you/player

a= gamewin(comp,you)
print(f"computer chooses {comp}")       #printing what computer has choosen
if a==None:
    print("the game is tie")                  #printing result whi wins the game

elif a:
    print("you win")

else:
    print("you lose")




