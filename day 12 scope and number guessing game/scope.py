import random
level = input("Enter:easy,medium,hald,veryHard")


levels = {"easy": 10, "medium": 30, "hard": 60, "veryHard": 100}
num = levels[level]           
def guessGame(maxLevel):
    number = random.random.randint(1,maxLevel)
 
life=3    
while(life>0){ 
    user = int(input("enter any number"))
    if(user == guessGame(num)):
         "You win"
}
