import json

# 1. Read the desired configuration file
with open(r"c:\Users\Awjaypogi\Desktop\devops-journey\projects\Project 1 (The Configuration Drift Detector)\config.json", "r") as my_file:
    desired_settings = json.load(my_file)

# 2. Fake "Live" Server Data (Simulating multiple changes at once!)
live_server_settings = {
    "server_name": "Hacked_Roblox_Server",  # Look! Someone changed the name too!
    "max_players": 100,                     # This is still wrong
    "status": "online"                      # This one actually matches
}

print("--- Starting Full Configuration Drift Check ---")

# 3. Create a flag variable to keep track of any errors we find
drift_found = False

# 4. Loop through every single key/setting inside our desired configuration dictionary
for setting_name in desired_settings:
    
    # Check if the current setting matches between the file and the live server
    if desired_settings[setting_name] != live_server_settings[setting_name]:
        print(f"⚠️ DRIFT DETECTED in '{setting_name}'!")
        print(f"   -> Expected: {desired_settings[setting_name]}")
        print(f"   -> Live Server Has: {live_server_settings[setting_name]}")
        drift_found = True  # We found at least one problem, so flip our flag to True

# 5. Final report summary
if drift_found == False:
    print("✅ System Healthy: All configurations match perfectly!")
else:
    print("\n❌ Audit Complete: System is out of sync. Action required!")