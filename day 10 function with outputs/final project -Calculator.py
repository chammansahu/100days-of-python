from art import logo



def addition(op1,op2):
    return op1 + op2

def substraction(op1,op2):
    return op1 - op2

def multiplication(op1,op2):
    return op1 * op2

def division(op1,op2):
    return op1 / op2

operations={
    "+":addition,
    "-":substraction,
    "*":multiplication,
    "/":division,
}
def calculator():
    print(logo)  
    
    num1 = float(input("Enter Number One: "))
    for symbol in operations:
   
        print(f" {symbol}")
    should_continue = True
    
    while should_continue:
            
        user=input("pick a symbol : ")
        num2 = float(input("Enter Number Two: "))

        answer = operations[user](num1,num2)

        print(f"{num1} {user} {num2} = {answer}")
        
        moreOperation=input("Do you want to calculate another?Yes Or No  ")
        
        if(moreOperation=="yes"):
            num1=answer
            calculator()
        elif (moreOperation == "no"):
            print(f"{num1} {user} {num2} = {answer}")
            should_continue=False;
            
        else:
            print("you enterd wrong details")        
            
calculator()        
