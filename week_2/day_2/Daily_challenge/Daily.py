'''
Challenge 1
Ask the user for a number and a length.
Create a program that prints a list of multiples of the number until the list length reaches length.
Examples

number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]
'''
user_input = int(input("Enter a number: "))
length = int(input("Enter the length: "))

numbers = []  # Create an empty list to store the generated numbers
count=1

for i in range(length):
    value = user_input * count
    count+=1
    numbers.append(value)  # Add the generated number to the list

print(numbers) 


'''
Challenge 2
Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
Examples

user's word : "ppoeemm" ➞ "poem"

user's word : "wiiiinnnnd" ➞ "wind"

user's word : "ttiiitllleeee" ➞ "title"

user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
Notes
Final strings won’t include words with double letters (e.g. “passing”, “lottery”).
'''
Word=input("Enter a Word: ")

Duplicates=[]

for i in range(len(Word)):
    if Word[i] not in Duplicates:
        Duplicates.append(Word[i])

Join=''.join(Duplicates)
print(Join)