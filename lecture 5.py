##def squares(num):
##    newlist = [i*i for i in range (num+1)]
##    return newlist
##print(squares(10))
    
##lower = int(input("Please enter a lower bound (int): "))
##upper = int(input("Please enter a upper bound (int): "))
##divisible = int(input("Please enter a number to divide by (int): "))
##
##num_list = [i for i in range (lower, upper) if i % divisible == 0]
##print("All of the numbers between ", lower , "and ", upper , "that are divisible by", divisible , ":", num_list) 
##
#print (num_list)

name = input("Please enter a file name: ")
vowels = ["a", "e", "i", "o", "u"]
fileContents = [line.strip() for line in open(name, "r")]
print("All words in the file: ", fileContents)
vowel_check = [vowels for vowels in fileContents]
print("The words in the file that contain 2 or more vowels: 
print(vowel_check)
#print(fileContents)


