# variable are declared directly without any keyword
#global variable scope
name="chamamn"
age=29

def printAges():
    #local scope
    #using global keyword
    localName="chamamn"
    LocalAge=29
    
    #casting of variable
    x=str("some value")
    y=int(100)
    #get the type 
    print(type(x))
    print(type(y))
    
printAges()    
    