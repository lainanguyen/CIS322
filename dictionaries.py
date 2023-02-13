# Python Dictionaries
# {}, key: value pairings, no order
# keys have to be unique

d1 = {"Johnny": 21, "Michelle": 35, "Tom": 4}

# Add a pairing

d1["Renee"] = 15

# Loop through all data in dictionary

for key, value in d1.items():
    print(f"{key} is {value} years old.")