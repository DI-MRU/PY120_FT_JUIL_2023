import http.server
import socketserver
import json
import os

PORT = 8000

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative file path to the JSON file
json_file_path = os.path.join(script_dir, 'pokemon_data.json')

# Open the JSON file and load data
with open(json_file_path, 'r') as f:
    data = json.load(f)

# Access the list of pokemons
pokemons = data['pokemons']

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Return the search form to the user
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            form_html = """
            <html>
            <body>
                <form action="/search" method="get">
                    <label for="pokemon_name">Enter the name of the Pokémon you want to search for:</label><br>
                    <input type="text" id="pokemon_name" name="pokemon_name"><br>
                    <input type="submit" value="Search">
                </form>
            </body>
            </html>
            """
            self.wfile.write(form_html.encode())
        elif self.path.startswith('/search'):
            # Extract the query parameter 'pokemon_name'
            query = self.path.split('?')[1]
            pokemon_name = query.split('=')[1].lower()

            # Search for the Pokémon in the database
            found_pokemon = None
            for pokemon in pokemons:
                if pokemon['name'].lower() == pokemon_name.lower():
                    found_pokemon = pokemon
                    break

            # Prepare the response
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            if found_pokemon:
                # Return the details of the Pokémon
                response_html = f"""
                <html>
                <body>
                    <h2>Name: {found_pokemon['name']}</h2>
                    <p>Type: {found_pokemon['type']}</p>
                    <p>Power: {found_pokemon['power']}</p>
                    <p>Evolves from: {found_pokemon['evolves_from']}</p>
                </body>
                </html>
                """
            else:
                # Return a message if the Pokémon is not found
                response_html = "<html><body>Pokémon not found in the database.</body></html>"

            self.wfile.write(response_html.encode())
        else:
            # Return a 404 error for any other paths
            self.send_error(404)

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
        print(f"Server running on http://localhost:{PORT}")
        httpd.serve_forever()
