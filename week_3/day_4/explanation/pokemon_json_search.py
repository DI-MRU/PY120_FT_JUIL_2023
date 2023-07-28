import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(script_dir, 'pokemon_data.json')

# Open the JSON file and load data
# with open('pokemon_data.json', 'r') as f: # Does the same thing
with open (json_file_path, 'r') as f:
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
