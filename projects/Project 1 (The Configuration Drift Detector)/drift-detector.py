import json

# 1. Read the desired configuration file
with open(r"c:\Users\Awjaypogi\Desktop\devops-journey\projects\Project 1 (The Configuration Drift Detector)\config.json", "r") as my_file:
    desired_settings = json.load(my_file)

# 2. Fake "Live" Server Data (Simulating that someone changed the max players!)
live_server_settings = {
    "server_name": "My_Roblox_Server",
    "max_players": 100,  # Look! This is 100, but our JSON file says 50!
    "status": "online"
}

print("--- Starting Configuration Drift Check ---")

# 3. Compare the 'max_players' value between both dictionaries using if/else
if desired_settings["max_players"] == live_server_settings["max_players"]:
    print("✅ Success: Max players setting matches perfectly!")
else:
    print("⚠️ ALERT: Configuration Drift Detected!")
    print(f"Expected: {desired_settings['max_players']}")
    print(f"Live Server Has: {live_server_settings['max_players']}")