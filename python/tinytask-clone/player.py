import pyautogui
import time

def start_playback():
    while True:
        try:
            delay = float(input("Enter delay between clicks (seconds): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("Starting playback in 3 seconds...")
    time.sleep(3)

    print("Auto-clicking started. Press CTRL+C to stop.")

    while True:
        pyautogui.click()
        time.sleep(delay)