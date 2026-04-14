import recorder
import player
def main():
    while True:
        print("\nTinyTask Clone")
        print("R - Record")
        print("P - Play")
        print("Q - Quit")

        choice = input("Choose option: ").lower()

        if choice == "r":
            recorder.start_recording()
        
        elif choice == "p":
            player.start_playback()
        elif choice == "q":
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()