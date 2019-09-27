#Question 1
#I have completed the "academic integrity & syllabus" quiz, and recieved a 100% (19/19)

#Question 2 - Pokemon Algorithm
import the random module
display a welcome message to the user (ex: 'Welcome to the Pokemon Game')

get user input to select either: fire, water, or grass
display error message if user inputs something other than: fire, water, or grass
assign the users input to variable "user_guess"

create a random function that picks from fire, water, or grass
assign the computers random choice to variable "comp_guess"

create a series of if/elif/else statements to determine the winner of the match

check if the value of user_guess is equal to the value of comp_guess
    if this is true, the fight is a draw
    print a statement indicating a draw between the user and computer
    
use a elif statement to check if user_guess is equal to 'fire' and comp_guess is equal to 'grass'
    if this is true, the user wins because fire is stronger than grass
    print a statment indicating the user won
    
use a elif statement to check if comp_guess is equal to 'fire' and user_guess is equal to 'grass'
    if this is true, the computer wins because fire is stronger than grass
    print a statment indicating the user lost
    
use a elif statement to check if user_guess is equal to 'grass' and comp_guess is equal to 'water'
    if this is true, the user wins because grass is stronger than water
    print a statment indicating the user won
    
use a elif statement to check if comp_guess is equal to 'grass' and user_guess is equal to 'water'
    if this is true, the computer wins because grass is stronger than water
    print a statment indicating the user lost

use a elif statement to check if user_guess is equal to 'water' and comp_guess is equal to 'fire'
    if this is true, the user wins because water is stronger than fire
    print a statment indicating the user won
    
use a elif statement to check if comp_guess is equal to 'water' and user_guess is equal to 'fire'
    if this is true, the computer wins because water is stronger than fire
    print a statment indicating the user lost


#Question 3 -- string duplicating program

user_in = str(input("Please a set of characters (letters/numbers) are allowed: ")) #getting the user inputted string
num = 2 #number of times I want each character to repeat in the final string output

for char in user_in: #created a loop to traverse through the user inputted string
    new_string = (''.join([char*num])) #used the .join method, to properly format the new string 
    print(new_string, end = '')

#Question 4 -
list_a = ['a', 'b', 'c', 'r', 4, 5]
list_b = ['d', 'a', 'm', 'r', 4, 9]

print('The values that occur in both lists are: ', end = '')

for value_X in list_a: #loop to go thorugh list a
    for value_Y in list_b: #loop to go thorugh list b
        if value_X == value_Y: #checking if any values are the same
            same_values = (value_X)
            print(same_values, end = " ") #printing the similar values

