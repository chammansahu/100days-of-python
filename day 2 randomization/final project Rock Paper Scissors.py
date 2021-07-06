import random
art={"rock" :'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
,
"paper" : '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

,"scissors" : '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
}
vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

choices = ["rock", "paper", "scissors"]



def calculate(player, computer):
    if(player == computer):
        print('Draw')

    elif(player == 0 and computer == 1):
        print('You lose')

    elif(player == 1 and computer == 2):
        print('You lose')

    elif(player == 2 and computer == 0):
       print('You lose')

    else:
       print('You win')
       
def results(userChoice, generated):
   try:
       your_choice = choices[userChoice]
       computer_choice = choices[generated]
   
       print(art[your_choice])
       print(vs)
       print(art[computer_choice])
   
       calculate(userChoice, generated)
   
   except:
       print('Invalid input. You lose')


def startGame():
    try:
        userChoice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: '))
        
        computer_generated = random.randint(0, len(choices)-1)
        results(userChoice, computer_generated)


    except:
        print('Invalid input. You lose')

continuePlaying=True

while continuePlaying:
    startGame()
    continueGame = input("want to play again : ")
    if continueGame=="yes":
        startGame()
    else:
        continuePlaying=False
        print(f"Good Bye!!!")
