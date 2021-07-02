
    
def primeCheck(number):
    primes=[]
    isPrime=True
    for item in range(2,number):
        if(number%2==0):
            isPrime=False
    return isPrime
        
print(primeCheck(5))        
                
        
        