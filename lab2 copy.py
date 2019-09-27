#question 1
##data = ['50 apples\n', '25 pears\n', '10 oranges\n']
##groceries = []
##
##for item in data:
##    new_item = item.strip()
##    new_item = item.split()
##    groceries.append(new_item)
##
###print(data)
##print(groceries)
##print(groceries[2][0])

#question 2
data = ['50 apples\n', '25 pears\n', '10 oranges\n']
groceries = []

for item in data:
    num, fruit = item.strip().split(" ")
    groceries[fruit] = num
    
print(groceries["oranges"])
