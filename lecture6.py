#question 1 ~ finding vowels within a sentence (not singular words)
user_file = input("Please enter a file name: ")

line_lst = [line.strip() for line in open(user_file, "r")]
print("All words in the file: ", line_lst)


word_lst = [word for line in line_lst for word in line.split(" ")
            if len([char for char in word if char in "aeiou"]) >= 2]

print("The words in the file that contain 2 or more vowels: ", word_lst)

#question 2 ~ phrase translation using a dictionary
user_phrase = input("Please enter the phrase to translate: ")

trans_dict = {'1':"i", '3':"e", '4':"a":, '5':"s", '7':"t")

translate = [trans_dict[char] if char in trans_dict
             else char for char in user_phrase]

print("".join(translate))
