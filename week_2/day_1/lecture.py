# x = 10
# y = -1239085902350

# print("The addition of x(" + str(x) + ") and y(" + str(y) + ") is: " + str(x + y) + ".")

# greeting = "Hello guys, good morning to you"
# print(f"The addition of x({x}) and y({y}) is: {x + y}.")

# print(greeting)
# print(greeting.upper())
# print(greeting.lower())
# print(greeting.capitalize())
# print(greeting.replace("Hello", "Hi"))

# thirst_name = "Borel"
# last_name = "Jevin"
# print(thirst_name + " " + last_name)

# print("Hello world\n\n\tMy name is Rick")
# print("---------------------------------")
# print("Hello world\\tMy name is Rick")

# If my age is less than 18, we will print "You are a child"
# If my age is more than 18, we will print "You are an adult"

# my_age = 9432

# if my_age < 18:
#     print(f"You are a child")
# # elif my_age >= 18:
# #     print(f"You are an adult")
# else:
#     print(f"You are an adult")

# print(" ~~ Menu for DI studebts ~~ ")
# print(" 1. Add item")
# print(f" 2. Remove item")
# print(f" 3. Edit item")
# print(f" 4. Update stock")
# print(f" 5. Exit")
# print(f"")
# my_choice = int(input("Please select an option: "))
# print(f"Your choice was {my_choice} of type {type(my_choice)}")
# if my_choice == 1:
#     print(" ~~ Add Item ~~")
# elif my_choice == 2:
#     print(" ~~ Remove Item ~~")
# elif my_choice == 3:
#     print(" ~~ Edit Item ~~")
# elif my_choice == 4:
#     print(" ~~ Update Item ~~")
# else:
#     print(" ~~ Goodbye ~~")

# my_choice = 0
# while my_choice != 5:
#     print(" ~~ Menu for DI studebts ~~ ")
#     print(" 1. Add item")
#     print(f" 2. Remove item")
#     print(f" 3. Edit item")
#     print(f" 4. Update stock")
#     print(f" 5. Exit")
#     print(f"")
#     my_choice = int(input("Please select an option: "))
#     print(f"Your choice was {my_choice} of type {type(my_choice)}")

#     if my_choice == 1:
#         print(" ~~ Add Item ~~")
#     elif my_choice == 2:
#         print(" ~~ Remove Item ~~")
#     elif my_choice == 3:
#         print(" ~~ Edit Item ~~")
#     elif my_choice == 4:
#         print(" ~~ Update Item ~~")
#     elif my_choice == 5:
#         print(" ~~ Goodbye ~~")

# age = 9

# if not (age == 10 and age >= 18):
#     print("You are not ten years old and you are a child")

# if True:
#     print("This is true")
# print(not True)
# print(True)

# print(not False)
# print(False)

# if not not not not not not True:
#     print("This is false")

# print("Enter a number between 1 and 100:")
# number = input()
# if number.isdecimal():
#     number = int(number)
#     print(f"The number is {number}")

#     if number < 1 or number > 100:
#         print("Error: The number is not between 1 and 100.")
#     else:
#         if number % 3 == 0:
#             print(f"{number}: Fizz")
#         if number % 5 == 0:
#             print(f"{number}: Buzz")
# else:
#     print("The input was not a number")


# TODO: What's wrong with this code?
number = int(input("Please enter your number between 1 and 100: "))
if not (number % 3 and number % 5):
    print("FizzBuzz")
elif number % 3 != True:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
