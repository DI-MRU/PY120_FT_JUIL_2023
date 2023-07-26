''' Exercise 1 : Set
Instructions
Create a set called my_fav_numbers with all your favorites numbers.
Add two new numbers to the set.
Remove the last number.
Create a set called friend_fav_numbers with your friend’s favorites numbers.
Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
'''

my_fav_numbers = {1,2,18,28}

my_fav_numbers.add(12)

my_fav_numbers.add(22)
# print(my_fav_numbers)

# my_fav_numbers.remove(28)

my_fav_numbers=set(list(my_fav_numbers)[:-1])
print(my_fav_numbers)

friend_fav_numbers = {1,2,3,4,5,6}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)


# 🌟 Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
# NO

'''
🌟 Exercise 3: List
Instructions
Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

Remove “Banana” from the list.
Remove “Blueberries” from the list.
Add “Kiwi” to the end of the list.
Add “Apples” to the beginning of the list.
Count how many apples are in the basket.
Empty the basket.
Print(basket)
'''

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.pop(0)
# basket.pop(-1) removes the last item in the list
print(basket)

basket.remove("Blueberries")
print(basket)

basket.append("Kiwi")
print(basket)

basket.insert(0,"Apples")
print(basket)

print(basket.count("Apples"))

basket.clear()
print(basket)

'''
Exercise 4: Floats
Instructions
Recap – What is a float? What is the difference between an integer and a float?
Can you think of another way to generate a sequence of floats?Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
'''
# method1
# sequence = [x/2 for x in range(3,11)]
# print(sequence) Do not hard code it!

start = 1.5
step=0.5
count=8
sequence=[start + (step * i) for i in range(count)]
print(*sequence,sep=", ")
# print(sequence)

'''
Exercise 5: For Loop
Instructions
Use a for loop to print all numbers from 1 to 20, inclusive.
Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
'''
# 1
for num in range (1,21):
    print(num)

# 2
for nums in range (0,21,2): #start, stop, step
    # if nums % 2 == 0: # 100% works fine
        print(nums)

'''Exercise 6 : While Loop
Instructions
Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
'''
your_name = "hemlesh"

user_input = ""

while user_input.lower() != your_name.lower():
    user_input = input("What is your name? ") 

print("Thank you!")


'''
Exercise 7: Favorite Fruits
Instructions
Ask the user to input their favorite fruit(s) (one or several fruits).
Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
Store the favorite fruit(s) in a list (convert the string of words into a list of words).
Now that we have a list of fruits, ask the user to input a name of any fruit.
If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
'''
favorite_fruits = input("Enter your favorite fruit(s), separated by a single space: ").split()
print(favorite_fruits)
chosen_fruit = input("Enter a fruit name: ")

if chosen_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")

else:
    print("You chose a new fruit. I hope you enjoy")

'''
Exercise 8: Who Ordered A Pizza ?
Instructions
Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
As they enter each topping, print a message saying you’ll add that topping to their pizza.
Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
'''
toppings =[]

total_price = 10

while True:
    topping = input("Enter a topping (or type 'quit' to finish): ")
    if topping.lower() == "quit":
        break
    toppings.append(topping)
    total_price += 2.5
    print(f"Adding {topping} to your pizza.")

print("The Toppings on your pizza is: ")
for topping in toppings:
    print("• "+topping)

print(f"Total price: ${total_price}")
# same as
# print("Total price: $" , total_price)

'''
Exercise 9: Cinemax
Instructions
A movie theater charges different ticket prices depending on a person’s age.
if a person is under the age of 3, the ticket is free.
if they are between 3 and 12, the ticket is $10.
if they are over the age of 12, the ticket is $15.Ask a family the age of each person who wants a ticket.Store the total cost of all the family’s tickets and print it out.A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
At the end, print the final list.
'''
# part 1

total_cost = []

while True:
    age = int(input("Enter your age (then type '0' to exit): "))
    if age == 0:
        break
    if age < 3:
        total_cost.append(0)
    elif age >= 3 and age <= 12:
        total_cost.append(10)
    else:
        total_cost.append(15)

print (f" Total cost of all tickets: ${sum(total_cost)}")

# Method 2
# total_cost = 0

# while True:
#     age = int(input("Enter your age (then type '0' to exit): "))
#     if age == 0:
#         break
#     if age < 3:
#         total_cost += 0
#     elif 3 <= age <= 12:
#         total_cost += 10
#     else:
#         total_cost += 15
# print(f"Total cost of all tickets: ${total_cost}")


# part 2 teanagers restricted movie
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

allowed_names = []
not_allowed_names = []
for name in names:
    age = int(input(f"Enter {name}'s age: "))
    if 16 <= age <= 21:
        allowed_names.append(name)
    else:
        not_allowed_names.append(name)

print("Persons who can watch the movie:")
print(allowed_names)
print("Teenagers who can't watch the movie:")
print(not_allowed_names)

'''
10 Sandwich Orders
Instructions
Using the list below :

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
We need to prepare the orders of the clients:
Create an empty list called finished_sandwiches.
One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
I made your tuna sandwich
I made your avocado sandwich
I made your egg sandwich
I made your chicken sandwich
'''

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich.lower()}")

# Print the sandwiches that were made
print("Sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)
