import pprint
menu={
    "expresso":{
        "ingredients":{
            "water":50,
            "coffe":18,
        },
        "cost":1.50,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "coffe":24,
            "milk":150
        },
        "cost":2.50,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "coffe":24,
            "milk":100
        },
        "cost":3.00,
    },
    
}
profit=0
resources = {
    "water": 1000,
    "coffe": 250,
    "milk": 1000
}
def isSuffcientResources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True
    
def insertCoins():
    print("Please insert Coins!!!")
    quarter=int(input("How Many Quarters?: "))
    dimes=int(input("How Many Dimes?: "))
    nickles=int(input("How Many nickles?: "))
    peny=int(input("How Many pennies?: "))
    total=quarter*.25+dimes*.1+nickles*.05+peny*.01
    return total

def isTransactionSuccess(recieved_money,drink_cost):
    if recieved_money>=drink_cost:
        change = round(recieved_money-drink_cost,2)
        global profit
        profit+=drink_cost
        print(f"change due {change}")
        return True
    else: 
        print("Sorry!!! you need More Money ")
        return False


def makeCoffe(drinkName, order_ingredient):
    for item in order_ingredient:
        resources[item]-=order_ingredient[item]
    print(f"Here is Your {drinkName}")    
        
        

is_on=True

while is_on:
    choice = input("'What would you like?' (espresso/latte/cappuccino):")
    if choice =="off":
        is_on=False 
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee:{resources['coffe']}g")
        print(f"Money: {profit} Rs.")
    else:
        drink = menu[choice]
        if  isSuffcientResources(drink["ingredients"]):
            payment = insertCoins()
            if isTransactionSuccess(payment,drink["cost"]):
                makeCoffe(choice, drink["ingredients"])
            
