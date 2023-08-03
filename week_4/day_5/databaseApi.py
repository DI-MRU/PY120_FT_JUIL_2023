import requests
import psycopg2

# Function to fetch data from the API
def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to connect to the PostgreSQL database
def connect_to_database():
    try:
        conn = psycopg2.connect(
            dbname="your_database_name", #postgres
            user="your_database_user",#postgres
            password="your_database_password",#PASS
            host="your_database_host",#localhost
            port="your_database_port",#5432
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

# Function to insert data into the PostgreSQL database
def insert_pokemon_data(conn, data):
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO pokemon (name, height, weight)
                VALUES (%s, %s, %s)
                """,
                (data["name"], data["height"], data["weight"]),
            )
        conn.commit()
        print("Data inserted successfully!")
    except psycopg2.Error as e:
        print(f"Error inserting data: {e}")

def main():
    # Replace 'your_pokemon_name' with the actual name of the Pokemon you want to fetch
    pokemon_name = "your_pokemon_name"
    
    # Fetch data from the API
    pokemon_data = get_pokemon_data(pokemon_name)
    
    if pokemon_data:
        # Connect to the PostgreSQL database
        connection = connect_to_database()
        if connection:
            # Insert data into the database
            insert_pokemon_data(connection, pokemon_data)
            connection.close()
    else:
        print(f"Failed to fetch data for Pokemon: {pokemon_name}")

if __name__ == "__main__":
    main()
