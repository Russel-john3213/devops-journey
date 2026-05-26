import psutil
import requests
import time

# 1. Configuration Settings
DISCORD_WEBHOOK_URL = "linklinklink"
CPU_THRESHOLD = 30.0  # The alert level percentage
CHECK_INTERVAL = 5    # How many seconds to wait between checks

print(f"--- System Monitor Active (Threshold: {CPU_THRESHOLD}%) ---")

# 2. Infinite monitoring loop
while True:
    # Grab a 1-second snapshot of CPU usage
    current_cpu = psutil.cpu_percent(interval=1)
    print(f"Checking system status... Current CPU: {current_cpu}%")
    
    # 3. Decision Logic: Is the system running too hot?
    if current_cpu > CPU_THRESHOLD:
        print("⚠️ THRESHOLD EXCEEDED! Sending Discord alert...")
        
        # Build the panic message payload
        alert_payload = {
            "content": f"🚨 **SYSTEM ALERT:** High CPU Usage Detected!\n"
                       f"-> **Current Load:** {current_cpu}%\n"
                       f"-> **Threshold Limit:** {CPU_THRESHOLD}%"
        }
        
        # Fire off the webhook POST request
        requests.post(DISCORD_WEBHOOK_URL, json=alert_payload)
    
    # 4. Rest before the next check cycle
    time.sleep(CHECK_INTERVAL)