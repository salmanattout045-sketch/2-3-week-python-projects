#1.that was how to write from a 4 minute video
import csv

names=[
    {"first_name":"salman","last_name":"attout"},
    {"first_name":"john","last_name":"wick"},
    {"first_name":"salman","last_name":"attout"},
    {   "first_name":"salman","last_name":"attout"}
]
with open("names.csv","w")as f:
    field_name=names[0].keys()
    writer= csv.DictWriter(f,fieldnames=field_name)
    for row in names:
        writer.writerow(row) # you can also do another way but only pick one so the program dosent get confused
        #writer.writerows(names)
    #writer= csv.DictWriter(f,fieldnames=field_name)#Uses dictionary keys as column headers
    #writer.writeheader()# writer.writeheader() writes the column names (fieldnames) as the first row of the CSV

#2. now we'll start with corey Schaffer how to read
with open("my_name.csv","r")as f:
    csv_reader= csv.DictReader(f)

    next(csv_reader) # next is when we want to skip first line which is mostly a header
    for line in csv_reader:
        print(line)

#3. doing it with writing dilimiter
with open("my_name.csv","r")as f:
    csv_reader= csv.DictReader(f)
    with open("new_name.csv","w")as f:
        csv_writing= csv.writer(f,delimiter='\t')
        for line in csv_reader:
            csv_writing.writerow(line)

#4 what happens if you read csv file in wrong dilimiter
with open("my_name.csv","r")as f:
    csv_reader= csv.DictReader(f,delimiter='\t')
    for line in csv_reader:
        print(line)


import requests
import csv

def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/jokes/random")
    data = response.json()
    return {
        "setup": data["setup"],
        "punchline": data["punchline"]
    }

results = []

for i in range(3):
    joke = get_joke()

    print(f"joke {i+1}:")
    print(joke["setup"])
    print(joke["punchline"])
    print("---")

    results.append(joke)

# Write jokes to CSV
with open("joke.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["joke_number", "setup", "punchline"])

    for index, joke in enumerate(results, start=1):
        writer.writerow([
            index,
            joke["setup"],
            joke["punchline"]
        ])
