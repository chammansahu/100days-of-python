#who will pay the bill
import random
def randomChoice(min,max):
    return random.randint(min,max)

def whoWillPay():
    names=input("Enter Names separated by comma")
    namesList = names.split(',')
    numberOfPayer = len(namesList)
    randomName = randomChoice(0,numberOfPayer-1)
    print(randomName)
    paidBy = namesList[randomName]
    print(paidBy)
    print("Today is meal brought by"+paidBy)
whoWillPay()    
