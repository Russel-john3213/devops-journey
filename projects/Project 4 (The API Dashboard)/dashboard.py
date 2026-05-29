import json
import requests
system_has_failed_nodes = False
with open("config.json", "r") as CONFIG_FILE:
    CONFIG_DATA = json.load(CONFIG_FILE)
    # 1. Start the loop to go through every target box
    for target in CONFIG_DATA["targets"]:
        
        # 2. Extract the name and URL directly from the active target box
        site_name = target["name"]
        site_url = target["url"]
        response = requests.get(site_url)
        status_code = response.status_code
        if status_code == 200:
            print(f"{site_name} is up! Status code: {status_code}")
        else:
            print(f"{site_name} is down! Status code: {status_code}")
            system_has_failed_nodes = True

if system_has_failed_nodes:
    with open("logs.txt", "w") as log_file:
        print("One or more nodes have failed. Please check the logs for details.", file=log_file)
    webhook_url = CONFIG_DATA["discord_webhook"]
    payload = {"content": "One or more nodes have failed. Please check the logs for details."}
    requests.post(webhook_url, json=payload)