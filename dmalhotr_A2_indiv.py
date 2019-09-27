#Damini Malhotra
#We never got group numbers in lectures, i do not remember my group number from lab! sorry !
#question 1 -- i based this code off the algorithm from lecture 2

print("Welcome to the Hangman Word Guessing Game!") #welcome statement

word = "hoosiers" #secret word  
guesses = [] #empty list where the users letter guess goes
gameover = False #used this line of code from the lab assignment word guess game   
wrong_guess = 0 #counts the number of times a user guesses the wrong letter

while (gameover == False):
    for char in word:  
        if char in guesses:  
            print(char, end = "" )
            guesses.append(guess)
        else:  
            print("_", end = "")   
            wrong_guess += 1
            #print("This letter is not in the secret word")
    if word in guesses:  
        print("You Win")  
        print("The secret word is: ", word)
        gameover = True #meant to end the game 
        break
    print()
    guess = str(input("Guess a letter: ")).lower()
    #every input character will be stored in guesses
    guesses.append(guess)

#I was not able to figure out the problem with this. The game does not end when the user fully guesses the letter.

#question 2 - pokemon game
import random
print("Welcome to the Pokemon Game")
print()

attack_methods = ['fire', 'water', 'grass'] #list of possible attack methods

user_guess = str(input("Please select your attack method (fire/water/or grass) : ")) #user input

#below i was trying to verfiy the user input it was not working properly
##if user_guess != 'fire' or 'water' or 'grass':
##    print("Incorrect attack method, Please choose again!")
##    user_guess = str(input("Please select your attack method (fire/water/or grass) : "))

computer_guess = random.choice(attack_methods) # computer guess
print("The computer selected: ", computer_guess) #i printed it out to verify the answer was correct
print()

# below is how i determined the winner of the match
if user_guess == computer_guess:
    print("It is a draw!")
elif user_guess == 'fire' and computer_guess == 'grass':
    print("You won!!")
elif user_guess == 'grass' and computer_guess == 'fire':
    print("You Lost :(")
elif user_guess == 'grass' and computer_guess == 'water':
    print("You won!!")
elif user_guess == 'water' and computer_guess == 'grass':
    print("You Lost :(")
elif user_guess == 'water' and computer_guess == 'fire':
    print("You won!!")
elif user_guess == 'fire' and computer_guess == 'water':
    print("You Lost :(")


    
