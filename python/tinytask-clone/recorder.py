import mouse

def start_recording():
    print("Recording started... Press ESC to stop.")

    mouse.hook(print)

    mouse.wait('esc')

    print("Recording stopped.")