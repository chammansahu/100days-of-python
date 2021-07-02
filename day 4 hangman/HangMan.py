# build hangman game  steps
import random
word_list = ["ardvik","baboon","camel","small"];

chosen_word = random.choice(word_list)

print(chosen_word) 
dispay= []
word_length = len(chosen_word)
for _ in range(word_length):
    dispay+="_"
print(dispay)    
    
game_over=True

guess = input("guess a letter ").lower()
while(not game_over):
    for i in range(word_length):
        letter = chosen_word[i]
        if(letter==guess):
            dispay[i]=letter
    print(dispay)        
      
    
if "_" not in dispay:
    game_over=True