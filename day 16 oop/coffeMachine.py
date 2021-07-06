class CoffeMaker:
    def __init__(self):
        self.resources={
            "water": 1000,
            "coffe": 250,
            "milk": 1000
        }
    def report(self):    
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.esources['milk']}ml")
        print(f"Coffee:{self.resources['coffe']}g")
        print(f"Money: {self.profit} Rs.")
        
    def isSuffcientResources(self,drink):
        can_make=true;
        for item in drink.ingredients:
            if drink.ingredients >= self.resources[item]:
                print(f"Sorry there is not enough {item}")
                return False
                can_make=False
        return True
    def makeCoffe(self ,order):
        for item in order.ingredient:
            self.resources[item]-=order.ingredient[item]
        print(f"Here is Your {order.name} 🍵")  
         