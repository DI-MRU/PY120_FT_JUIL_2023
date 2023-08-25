from datetime import datetime
import requests
import sys

start_time = datetime.now()

# Set a default value
number_of_facts = 1
# Check that the cli argument is valid and assign it
if len(sys.argv) > 1 and sys.argv[1].isnumeric():
    number_of_facts = int(sys.argv[1])

# Get cat facts from an API and save it to a file
with open("cat_facts.txt", "a") as cat_fact_file:
    for i in range(number_of_facts):
        cat_fact = requests.get("https://catfact.ninja/fact").json()
        print(cat_fact["fact"])
        cat_fact_file.write(f"{cat_fact['fact']}\n")
        cat_fact_file.flush()

end_time = datetime.now()

print(f"The script completed in {end_time - start_time}.")
