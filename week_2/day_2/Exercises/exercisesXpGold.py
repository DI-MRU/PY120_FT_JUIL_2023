'''
Exercise 1: Concatenate Lists
Instructions
Write code that concatenates two lists together without using the + sign.
'''
List1=[1,2,3]
List2=[4,5,6]

concatenate_List=[]

for item in List1:
    concatenate_List.append(item)

for item in List2:
    concatenate_List.append(item)

print(concatenate_List)

'''
Exercise 2: Range Of Numbers
Instructions
Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
'''
for num in range(1500 , 2501):
    if num %5 == 0 and num %7 == 0:
        print(num)

'''
Exercise 3: Check The Index
Instructions
Using this variable

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
Example: if input is 'Cortana' we should be printing the index 1
'''

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("Enter your name: ")

if user_name in names:
    index = names.index(user_name)
    print("Index: ", index)
else:
    print("Name not found in the list.")

'''
Exercise 4: Greatest Number
Instructions
Ask the user for 3 numbers and print the greatest number.
    Test Data
    Input the 1st number: 25
    Input the 2nd number: 78
    Input the 3rd number: 87

    The greatest number is: 87
'''
num1 = int(input("Input the 1st number: "))
num2 = int(input("Input the 2nd number: "))
num3 = int(input("Input the 3rd number: "))

greatest_number = max(num1, num2, num3)

print("The greatest number is:", greatest_number)

'''
Exercise 5: The Alphabet
Instructions
Create a string of all the letters in the alphabet
Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.
'''
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Loop over each letter
for letter in alphabet:
    if letter in 'aeiou':
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")

'''
Exercise 6: Words And Letters
Instructions
Ask a user for 7 words, store them in a list named words.
Ask the user for a single character, store it in a variable called letter.
Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.
'''
# Ask the user for 7 words and store them in a list
words = []
for i in range(7):
    word = input("Enter a word: ")
    words.append(word)


letter = input("Enter a single character: ")

for word in words:
    if letter in word:
        index = word.index(letter)
        print(f"The index of the first appearance of '{letter}' in '{word}' is: {index}")
    else:
        print(f"'{letter}' does not exist in '{word}'")

'''
Exercise 7:
Instructions
Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.
'''
numbers = list(range(1, 1000001))

# Verify the range using min() and max()
print("Minimum number:", min(numbers))
print("Maximum number:", max(numbers))

# Calculate the sum using sum()
total_sum = sum(numbers)
print("Sum of the numbers:", total_sum)

'''
Exercise 8 : List And Tuple
Instructions
Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
Suppose the following input is supplied to the program: 34,67,55,33,12,98

Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''
input_numbers = input("Enter comma-separated numbers: ")

# Generate list and tuple
number_list = input_numbers.split(',')
number_tuple = tuple(number_list)

print(number_list)
print(number_tuple)


'''
Exercise 9 : Random Number
Instructions
Ask the user to input a number from 1 to 9 (including).
Get a random number between 1 and 9. Hint: random module.
If the user guesses the correct number print a message that says Winner.
If the user guesses the wrong number print a message that says better luck next time.
Bonus: use a loop that allows the user to keep guessing until they want to quit.
Bonus 2: on exiting the loop tally up and display total games won and lost.
'''
import random

total_wins = 0
total_losses = 0

play_again = True

while play_again:
    user_guess = int(input("Guess a number from 1 to 9: "))
    random_number = random.randint(1, 9)

    if user_guess == random_number:
        print("Winner!")
        total_wins += 1
    else:
        print("Better luck next time!")
        total_losses += 1

    play_again_input = input("Do you want to play again? (yes/no): ")
    if play_again_input.lower() == 'no':
        play_again = False

print("Total games won:", total_wins)
print("Total games lost:", total_losses)

