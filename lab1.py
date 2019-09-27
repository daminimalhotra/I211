#problem 1
##names = []
##ages = []
##towns = []
##for i in range(5):
##    name = input("Enter the name of person ")
##    names.append(name)
##    age = input("Enter the age of person ")
##    ages.append(age)
##    hometown = input("Enter the hometwon of person ")
##    towns.append(hometown)
##
##
##print(names)
##print(ages)
##print(towns)
##
##print("Name    Age    Hometown")
##print("-----------------------")

#problem 2
#algorithm
#create a empty list
#index through the list, and put the smallest number in the new list
numbers = [6,3,2,5,7,1,1,2]
sorted_list = []

while numbers:
    min = numbers[0]
    for x in numbers:
        if x < min:
            min = x
    sorted_list.append(min)
    numbers.remove(min)

print(sorted_list)
