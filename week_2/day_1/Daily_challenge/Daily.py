'''
Instructions
Using the input function, ask the user for a string. The string must be 10 characters long.
If it’s less than 10 characters, print a message which states “string not long enough”.
If it’s more than 10 characters, print a message which states “string too long”.
If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

Then, print the first and last characters of the given text.

Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
The user enters "HelloWorld"
Then, you have to construct the string character by character
H
He
Hel
... etc
HelloWorld
'''
import random
user_input = input("Enter a string (10 characters): ")

if len(user_input) < 10:
    print("String not long enough.")
elif len(user_input) > 10:
    print("String too long.")
else:
    print("Perfect string.")

print("First character:", user_input[0])
print("Last character:", user_input[-1])

print("Constructing string character by character:")
for i in range(len(user_input)):
    print(user_input[0:i+1])

characters = list(user_input)
random.shuffle(characters)
shuffle = "".join(characters)
print("Shuffle character:", shuffle)

# print("Shuffled characters:", s_shuffle)
# shuffle="".join(random.sample(user_input,len(user_input)))
