# Task 3

import pandas as pd

# Load the CSV file
df = pd.read_csv("./csv/employees.csv")

# Make a list of names
full_names = []
for index, row in df.iterrows():
    first = row["first_name"]
    last = row["last_name"]
    name = first + " " + last
    full_names.append(name)

print("All employee names:")
print(full_names)

# Now find names that have the letter "e" in them
names_with_e = []
for name in full_names:
    if "e" in name.lower():
        names_with_e.append(name)

print("\nNames with the letter 'e':")
print(names_with_e)