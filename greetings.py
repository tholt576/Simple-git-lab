# greetings.py
#
# A simple program to greet people using plain text data.
#
# Usage:
# $ python greetings.py peopledata

# Tell Python we want to talk directly to the computer's operating system (OS)
import os, sys

# Configure where the program will look for data.
# Capitalize variable name to hint that it is a "constant" (doesn't change)
DATA_DIRECTORY = sys.argv[1]

# Look in the data folder and get all the file names
for each_file in os.listdir(DATA_DIRECTORY):

    # Change "max.txt" -> "data/max.txt" so Python can find the file
    file_path = os.path.join(DATA_DIRECTORY, each_file)

    # If there was an issue with our path and the file can't be found...
    if not os.path.isfile(file_path):
        # Then skip the rest of this loop and move to the next file
        continue

    # Open the file in read-only mode and attach a "handle" to interact with it
    with open(file_path, 'r') as file_handle:

        # Split the file up from one giant string into a list
        lines = file_handle.readlines()

        # Extract the person's name, remove surrounding whitespace
        first_name = lines[0].strip()

        # Extract their favorite foods, remove surrounding whitespace
        fave_foods = lines[1].strip()

        # Use commas to split the foods up into a list
        # "salad, chocolate" becomes ["salad", "chocolate"]
        fave_foods = [ food.strip() for food in fave_foods.split(",") ]

        # Count the amount of favorite foods in the list
        amount_of_fave_foods = len(fave_foods)

        # Print a greeting using a Python f-string and a variable reference
        print(f"Hello {first_name}!")

        # Show that we know how many favorite foods are in the list
        print(f"{first_name} has {amount_of_fave_foods} favorite foods: {fave_foods}")
