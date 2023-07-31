import requests
import json
import os

def search_and_append(pokemon_name):
    # API call to fetch Pokemon data based on the given name
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Extracting relevant information from the fetched data
        name = data['name']
        types = [t['type']['name'] for t in data['types']]
        power = data['stats'][0]['base_stat']
        
        # Handling 'evolves_from_species' information by making another API call
        species_url = data['species']['url']
        species_response = requests.get(species_url)
        if species_response.status_code == 200:
            species_data = species_response.json()
            evolves_from = "None"
            if 'evolves_from_species' in species_data and species_data['evolves_from_species'] is not None:
                evolves_from = species_data['evolves_from_species']['name']
        else:
            evolves_from = "None"
        
        # Creating a dictionary with relevant Pokemon data
        new_pokemon = {
            'name': name,
            'type': "/".join(types),
            'power': power,
            'evolves_from': evolves_from
        }
        
        # Set the relative file path for the JSON file in the same folder as the script
        script_directory = os.path.dirname(os.path.abspath(__file__))
        file_name = "pokemon_data.json"
        file_path = os.path.join(script_directory, file_name)
        
        # Check if the JSON file already exists
        if os.path.exists(file_path):
            with open(file_path, "r") as json_file:
                existing_data = json.load(json_file)
                pokemons = existing_data.get('pokemons', [])
                # Check if the new_pokemon is already in the JSON data to avoid duplicates
                if not any(p['name'] == name for p in pokemons):
                    pokemons.append(new_pokemon)
            # Write the updated data back to the JSON file
            with open(file_path, "w") as json_file:
                json.dump(existing_data, json_file, indent=4)
        else:
            # If the JSON file does not exist, create it and save the data
            data_to_save = {'pokemons': [new_pokemon]}
            with open(file_path, "w") as json_file:
                json.dump(data_to_save, json_file, indent=4)
        
        print(f"Data for {pokemon_name} has been appended to {file_path}")
    else:
        # Print an error message if the API call was not successful
        print(f"Failed to fetch data for {pokemon_name}. API returned status code {response.status_code}")

# Example usage:
try:
    # Search and append data for four different Pokemon
    search_and_append('pikachu')
    search_and_append('charizard')
    search_and_append('bulbasaur')
    search_and_append('ditto') 
except Exception as e:
    # Catch and print any exceptions that occur during the process
    print("An error occurred:", e)
