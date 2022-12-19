import random
 
name = input("What is your name? ")
 
 
print("Good Luck ! ", name)
def guessed():
 
    words = ['c++', 'python', 'java', 'react','html','css','bootstrap',]
    
    word = random.choice(words)
    
    
    print("Guess the characters of  the name of programming languages")
    
    guesses = ""
    
    turns = 12

    
    
    while turns > 0:
    
        failed = 0
    
        for char in word:
    
            if char in guesses:
                print(char )
    
            else:
                print("_")
    
                failed += 1
    
        if failed == 0:
            print("You Win")
    
            print("The word is: ", word)
            break
    
        print()
        guess = input("guess a character:")
        if len(guess)<len(word):
    
         guesses += guess
        
        else :
            print ("Enter  only ",len(word)," number of inputs")


    
        if guess not in word:
    
            turns -= 1
    
            print("Wrong")
    
            print("You have", +turns, 'more guesses')
    
        if turns == 0:
                print("You Loose")
    again = int (input("do you want to play again '0' for no and any other for play again"))
    while  again==0:
            print ("Thank you")
            break
    else:
    
     guessed()
guessed()