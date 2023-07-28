import requests
import json

def search(link):
    url = f"https://pokeapi.co/api/v2/pokemon/{link}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Extracting relevant information
        name = data['name']
        url = data['sprites']['front_default']
        types = [t['type']['name'] for t in data['types']]
        extracted_data = {'name': name, 'url': url, 'types': types}
        
        with open(f"{link}.json", "w") as json_file:
            json.dump(extracted_data, json_file, indent=4)
        print(f"Data for {link} has been saved to {link}.json")
    else:
        print(f"Failed to fetch data for {link}. API returned status code {response.status_code}")

search('pikachu')

