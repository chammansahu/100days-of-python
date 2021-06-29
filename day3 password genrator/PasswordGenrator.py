import random
from typing import Generator;

letters = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.upper().split(',')
numbers = '1,2,3,4,5,6,7,8,9,0'.split(',')
symbols = '!,@,#,$,%,^,&,*,(,),'.split(',')


print("Welcome to password generator")
letterLength = int(input("how many letters do you want in password: "))
numberLength = int(input("how many numbers do you want in password: "))
symbolLength = int(input("how many symbols do you want in password: "))

password_list = []

for item in range(letterLength):
    # print(letters[item])
    password_list.append(random.choice(letters))
for item in range(numberLength):
    # print(numbers[item])
    password_list.append(random.choice(numbers))
for item in range(symbolLength):
    # print(symbols[item])
    password_list.append(random.choice(symbols))
print(password_list)    

# suffle order of letter numbers and sybols

random.shuffle(password_list)

password2 = ""

for item in password_list:
    
    password2+=item

print(password2)    
    
    

