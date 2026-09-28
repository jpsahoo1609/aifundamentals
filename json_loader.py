# Writing  a json data to file 
# json.dump(data, filename)
import json

data = {
    "persons": [
        {'name': 'John','age' : 30},
        {'name': 'Amy','age' : 25},
        {'name': 'Bob','age' : 35}
    ]
}

# json data to file - json.dump() method is used to write JSON data to a file
# response/file data to json - json.load() method is used to read JSON data from a file
with open('data.json','w') as f:
    json.dump(data,f)

# dump this dict data into the open file f as json 

# READING JSON DATA FROM FILE
with open('data.json', 'r') as f:
    loaded_data = json.load(f) # this method will read the json file and convert it into a python dict object

print(loaded_data) # printing the loaded data from the json file