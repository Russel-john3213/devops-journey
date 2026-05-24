# Line 1: We import the "json" library. This gives Python special powers to read JSON files.
import json

# Line 2: We open the file "config.json". We give it a temporary nickname called "my_file".
with open(r"c:\Users\Awjaypogi\Desktop\devops-journey\projects\Project 1 (The Configuration Drift Detector)\config.json", "r") as my_file:
    
    # Line 3: We tell the json library to read the file and turn it into a Python "dictionary".
    server_settings = json.load(my_file)

# Line 4: We print the settings out on the screen so we can see them!
print("Success! Here are the settings we found:")
print(server_settings)