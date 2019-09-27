#list comprehension practice
##result_list = [x**2 for x in range(10)]
##print(result_list)
##
##
##doubles = [x*2 for x in range(10)]
##print(doubles)
##
##numbers = [x for x in range(100) if x%10 ==0]
##print(numbers)
##
##words = ['apple', 'ball', 'candle', 'dog', 'egg', 'frog']
##words = [words[i].upper() if len(word) < 4 else word for word in words]
##print(words)
##words2 = [word.upper() for word in words if len(word) < 4]
##print(words2)

#censorship problem - replacing all letters with a dash
secret = input("Please enter the secret: ")

redacted = ["-" if char.isalpha() == True or char.isdigit() == True
            else char for char in secret]

print("".join(redacted))




