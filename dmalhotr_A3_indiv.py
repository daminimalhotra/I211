#Damini Malhotra
#Group 6 

# Part 1 - Algorithm
#Use list comprehension to load the data from a file  “teams.txt”
    #load a text file, and it read line by line
    #strip each  line
    #split line by a " "
# Create a for loop to go through the data and print it out in the required format ("The [name] have won [number] games")

#Use list comprehension to create a list of the names of teams with less than 5 letters

#Use a list comprehension to create a list of the names of the three teams with the highest number of wins (greater than or equal to 7)

#Part 2
file_data = [line.strip().split(" ") for line in open("teams.txt", "r")] #loads in all file contents, and splits/strips the data

for i in file_data:
    print("The",i[0],"have won", i[1], "games") #formatting data to indicate teams and number of wins
print()

five_letters = [word[0] for word in file_data if len(word[0]) < 5] #checks the length of each word, and prints the ones with less than 5 characters

print("Teams with names shorter than 5 letters:", five_letters)
print()

#finding top 3 scoring teams
wins= [word[0] for word in file_data if int(word[1]) > 6] #here i hardcoded in 6 wins after looking at the data
print("The three teams with the most wins are: ", sorted(wins))

#finding top 3 scoring teams - method 2
#team_stats = sorted([[int(word[1]),word[0]] for word in file_data], reverse = True) #learned this method online (reverse = True) makes the outcome to be descending order
#winning_teams = [team_stats[i][1] for i in range(3)] #this is to find the top 3 scoring teams, double indexing I learned in I210
#print("The three teams with the most wins are:", winning_teams)

