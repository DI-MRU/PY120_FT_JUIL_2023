import os
import pickle

from pathlib import Path
from classes.watch import Watch

# Global constants
WORKING_DIR = Path().cwd()
DATA_DIR = WORKING_DIR / "data/vincent/"

# Check for missing directories and create them or raise errors
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
if not os.path.exists(DATA_DIR / "input/greeting.csv"):
    raise ImportError("Missing greeting.csv file.")
if not os.path.exists(DATA_DIR / "output/"):
    os.makedirs(DATA_DIR / "output/")
if not os.path.exists(DATA_DIR / "pickle/"):
    os.makedirs(DATA_DIR / "pickle/")


def greet_user(greeting):
    """
    Print a greeting to the user on the console.

    Keyword Arguments:
    greeting : str - The greeting to be used.
    """

    # List of names
    name_set = {"Anas", "Laeticia", "Onyeka", "Vincent"}
    name_list = ["Anas", "Laeticia", "Onyeka", "Vincent"]

    # name_set.add("Jeremy")
    # name_set.add("Jeremy")
    # name_set.add("Jeremy")
    # name_list.append("Himanish")
    # name_list.append("Himanish")
    # name_list.append("Himanish")

    # print(name_list)

    # Write the greeting to the file
    f = open(DATA_DIR / "output/greeting.txt", "w")
    for name in name_set:
        greeting_str = f"{greeting.capitalize()} {name}"
        f.write(f"{greeting_str}\n")
        print(f"Wrote `{greeting_str}` to file `greeting.txt`.")
    f.close()


if __name__ == "__main__":
    # Open the file `greeting.csv` in the read mode only
    with open(DATA_DIR / "input/greeting.csv", "r") as input_file:
        # read the file and store the content in a variable
        content = input_file.read()
        # print the content
        print(content)

    greet_user(content)

    # Intiialize a watch object from the Watch class
    onyeka_watch = Watch("Nixon", 487589347, 3187, "Gold")
    print(onyeka_watch)

    # Save the pickled object to a file/disk
    with open(DATA_DIR / "pickle/watch.dat", "wb") as output_file:
        pickle.dump(onyeka_watch, output_file)

    # Load the pickled object from the file/disk
    with open(DATA_DIR / "pickle/watch.dat", "rb") as input_file:
        input_watch = pickle.load(input_file)
        print(input_watch)
