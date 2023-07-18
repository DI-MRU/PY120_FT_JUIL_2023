'''
Exercise 4 : How Many Characters In A Sentence ?
Instructions
Use python to find out how many characters are in the following text, use a single line of code (beyond the establishment of your my_text variable).
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum.
'''
my_text='''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum.'''

print(len(my_text))


'''
Exercise 5: Longest Word Without A Specific Character
Instructions
Keep asking the user to input the longest sentence they can without the character “A”.
Each time a user successfully sets a new longest sentence, print a congratulations message.
'''
longest_sentence = ""

print("Welcome to the Longest Sentence Game!")
print("Enter the longest sentence you can without using the letter 'A'.")
print("Type 'quit' to exit.")

while True:
    user_input = input("Enter your sentence: ")
    
    if user_input.lower() == "quit":
        break
    
    if "a" in user_input.lower():
        print("Sorry, the sentence cannot contain the letter 'A'. Try again.")
        continue
    
    if len(user_input) > len(longest_sentence):
        longest_sentence = user_input
        print("Congratulations! You set a new record with the longest sentence without the letter 'A'.")
    
    print("Current longest sentence without 'A':", longest_sentence)

print("Thanks for playing!")


    

