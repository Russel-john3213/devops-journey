import os
import json
import requests
from pathlib import Path
from dotenv import load_dotenv

# 1. Dynamically find the exact folder where this dashboard.py file lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")
LOG_PATH = os.path.join(BASE_DIR, "logs.txt")

# 2. Tell python-dotenv to read the .env file sitting right next to this script
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=ENV_PATH)

# Temporary debug line to confirm what python-dotenv extracted:
print("DEBUG: Webhook value loaded is ->", os.environ.get("discord_webhook"))

system_has_failed_nodes = False
with open(CONFIG_PATH, "r") as CONFIG_FILE:
    CONFIG_DATA = json.load(CONFIG_FILE)
    
    # Start the loop to go through every target box
    for target in CONFIG_DATA["targets"]:
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
    with open(LOG_PATH, "w") as log_file:
        print("One or more nodes have failed. Please check the logs for details.", file=log_file)
    
    webhook_url = os.environ.get("discord_webhook")
    payload = {"content": "One or more nodes have failed. Please check the logs for details."}
    requests.post(webhook_url, json=payload)