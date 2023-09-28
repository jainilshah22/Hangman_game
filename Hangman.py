import random
from collections import Counter
  
someWords = ["apple", "banana", "mango", "strawberry", 
"orange", "grape", "pineapple", "apricot", "lemon", "coconut", "watermelon",
"cherry", "papaya", "berry", "peach", "lychee", "muskmelon"]

name = input("What is your name? ")
print ("Hello, " + name, "Time to play hangman!")
print ("Start guessing...\n")
word = random.choice(someWords)
guesses = ''
turns = 5
while turns > 0:         
    failed = 0             
    for char in word:      
        if char in guesses:    
            print (char,end="")   
        else:
            print ("_",end=""),     
            failed += 1    
    if failed == 0:        
        print ("\nYou WON!! You have guessed it Right") 
        break              
    guess = input("\nguess a character:") 
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
        print("\nYou have guessed it Wrong",guess)   
        print("\nYou have", + turns, 'more guesses') 
        if turns == 0:           
            print ("\nYou Lose!!",word+" is the word") 