#create a loop that adds up the user input, until the user types "STOP"
total_sum = 0
user_in = ""

user_in = input("Please enter a number or STOP: ")

while user_in != "STOP":

    total_sum += int(user_in)
    user_in = input("Please enter a number or STOP: ")

print("The total sum is" , (total_sum))



#create a loop that sorts 10 numbers into 3 lists
count = 0
even = []
odd = []
other = []

while count <= 9:
    number = eval(input("Please enter a number: "))
    count += 1
    if number % 2 == 0:
        even.append(number)
    elif number % 2 == 1:
        odd.append(number)
    else:
        other.append(number)

print(even)
print(odd)
print(other)

#dictionary practice
scores = {"Dave":125, "Abby":100, "Carrie":275, "Ben":150}

print("Current Players: ")
names = sorted(scores.keys())
               
for name in names:
    print(name, end = " ")
print()

name = input("Please enter a name: ")
print(scores.get(name))

