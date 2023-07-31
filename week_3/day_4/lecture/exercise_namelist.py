count_dict = {}
f = open('nameslist.txt','r')
for line in f: # Reads the full file and splits it into lines
    line = line.strip() # Removes any leading or trailing spaces, including `\n`
    if line in count_dict:
        count_dict[line] += 1 # Increment the count of the word by 1 if it already exists
    else:
        count_dict[line] = 1 # Create a new entry in the dictionary
f.close() # Close the file asap as some other process may need it

for key in count_dict:
    print(f"Number of {key} = {count_dict[key]}")