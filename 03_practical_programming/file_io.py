import csv

with open('data/products.csv', 'r') as input_file:
    reader = csv.DictReader(input_file)
    for row in reader:
        print(f"{row['product_id']}: {row['name']} {row['description']} ${row['price']}")

scores = [
    {'home': 'CAN', 'away': 'FRA', 'score': '0-1'},
    {'home': 'GER', 'away': 'JPN', 'score': '0-0'},
]

with open('data/scores.csv', 'w') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=['home', 'away', 'score'])
    writer.writeheader()
    writer.writerows(scores)

# JSON 

import json

profile: dict = {
    "name": "Maya",
    "courses": ["CSCI 1030U", "MATH 1010U"],
    "active": True,
}

with open("data/profile.json", "w") as f:
    json.dump(profile, f, indent=2)

# Read it back
with open("data/profile.json") as f:
    data: dict = json.load(f)

print(data["name"]) # Maya
print(data["courses"][0]) # CSCI 1030U
