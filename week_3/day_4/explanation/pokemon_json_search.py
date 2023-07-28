import json

# Open the JSON file and load data
with open('pokemon_data.json', 'r') as f:
    data = json.load(f)

# Access the list of pokemons
pokemons = data['pokemons']

# Prompt the user to enter the name of the Pokémon they want to search for
pokemon_name = input("Enter the name of the Pokémon you want to search for: ")

# Check if the Pokémon exists in the database
found_pokemon = None
for pokemon in pokemons:
    if pokemon['name'].lower() == pokemon_name.lower():
        found_pokemon = pokemon
        break

# Print the details if the Pokémon is found
if found_pokemon:
    print("Name:", found_pokemon['name'])
    print("Type:", found_pokemon['type'])
    print("Power:", found_pokemon['power'])
    print("Evolves from:", found_pokemon['evolves_from'])
else:
    print("Pokémon not found in the database.")
