#Damini Malhotra
#Group 6

#Section 1 - On Idle, there is a tab of "Help". Python doc is in that tab. Also, a user simply press the F1 button for same feature. Also you can go to python.org

#Section 2. Algorithm 
#first you need to import os, and datetime

##then you need to ask user's input for directory

#create a line of code indicating the home directory

#change path to new one that user had input

#use a for loop to traverse through the data
    #find if a file that contains name of 'draft'
    #rename that to final, using the .replace function
    #print "edited on ~the date~"

##Section 3. 
import os, datetime #import os, and datetime modules

date_now = datetime.date.today()

user_input = input("Please enter a directory: ") #get user input

home = os.getcwd() #indicates home directory

new_home = os.path.join(home, user_input) #creates a path from home to the user input

os.chdir(new_home)

data = os.listdir(new_home)

for file in data:
    if "draft" in file: #find draft in the file
        new_data = os.rename(file, file.replace("draft", "final")) #replacing draft with final 
        print(file.replace("draft", "final"))
        #Section 4 - Bonus
        print("Edited on: ", date_now) #uses real time date from from beginning of code
