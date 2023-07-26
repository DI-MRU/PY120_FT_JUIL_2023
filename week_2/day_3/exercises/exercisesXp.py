# Exercise 1 : Convert Lists Into Dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict(zip(keys, values))
print(result)



# Exercise 2 : Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Given the following object:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# How much does each family member have to pay ?

# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).


family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

ticket_prices = {'free': 0, 'child': 10, 'adult': 15}
total_cost = 0

for member, age in family.items():
    if age < 3:
        cost = ticket_prices['free']
    elif 3 <= age <= 12:
        cost = ticket_prices['child']
    else:
        cost = ticket_prices['adult']
    total_cost += cost
    print(f"{member} has to pay ${cost}")


print(f"\nTotal cost for the family: ${total_cost}")


#  Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color:
#     France: blue,
#     Spain: red,
#     US: pink, green


# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# 3. Change the number of stores to 2.
# 4. Print a sentence that explains who Zaras clients are.
# 5. Add a key called country_creation with a value of Spain.
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# 7. Delete the information about the date of creation.
# 8. Print the last international competitor.
# 9. Print the major clothes colors in the US.
# 10. Print the amount of key value pairs (ie. length of the dictionary).
# 11. Print the keys of the dictionary.
# 12. Create another dictionary called more_on_zara with the following details:

# creation_date: 1975
# number_stores: 10 000


# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# 14. Print the value of the key number_stores. What just happened ?

brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': ['blue'],
        'Spain': ['red'],
        'US': ['pink', 'green']
    }
}

# Step 3: Change the number of stores to 2
brand['number_stores'] = 2

# Step 4: Print a sentence that explains who Zara's clients are
clients = ', '.join(brand['type_of_clothes'])
print(f"Zara's clients are {clients}.")

# Step 5: Add a key called 'country_creation' with a value of 'Spain'
brand['country_creation'] = 'Spain'

# Step 6: Check if the key 'international_competitors' is in the dictionary. If it is, add the store 'Desigual'
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')

# Step 7: Delete the information about the date of creation
del brand['creation_date']


# Step 8: Print the last international competitor
last_competitor = brand['international_competitors'][-1]
print(f"The last international competitor is: {last_competitor}")


# Step 9: Print the major clothes colors in the US
us_colors = brand['major_color']['US']
print("The major clothes colors in the US are:", ', '.join(us_colors))


# Step 10: Print the amount of key-value pairs (i.e., length of the dictionary)
num_pairs = len(brand)
print("The number of key-value pairs in the dictionary is:", num_pairs)

# Step 11: Print the keys of the dictionary
print("Keys of the dictionary:", list(brand.keys()))

# Step 12: Create another dictionary called 'more_on_zara'
more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}

# Step 13: Use a method to add the information from the dictionary 'more_on_zara' to the dictionary 'brand'
brand.update(more_on_zara)

# Step 14: Print the value of the key 'number_stores'. What just happened?
print("The value of the key 'number_stores' is:", brand['number_stores'])



# Exercise 4 : Disney Characters
# Instructions
# Use this list :

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analyse these results :

# #1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# #2/

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# #3/

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# Recreate the 1st result using a for loop
disney_users_A = {}
for i, user in enumerate(users):
    disney_users_A[user] = i
print(disney_users_A)

# Recreate the 2nd result using a for loop
disney_users_B = {}
for i, user in enumerate(users):
    disney_users_B[i] = user
print(disney_users_B)


# Recreate the 3rd result using a method (sorted alphabetically)
disney_users_C = dict(enumerate(sorted(users)))
print(disney_users_C)

# Recreate the 1st result for characters with names containing the letter "i"
disney_users_D = {}
for i, user in enumerate(users):
    if 'i' in user:
        disney_users_D[user] = i
print(disney_users_D)

# Recreate the 1st result for characters with names starting with "m" or "p"
disney_users_E = {}
for i, user in enumerate(users):
    if user[0] in ['m', 'p']:
        disney_users_E[user] = i
print(disney_users_E)