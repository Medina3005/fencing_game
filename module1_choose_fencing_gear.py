import random

# Module 1: Choose Fencing Gear
def choose_gear():
    """Allows the player to choose their fencing gear.

    Returns:
        str: The selected weapon choice.
    """
    gear_options = ["Foil", "Epee", "Sabre"]  # Fixed special character
    print("\nChoose your fencing gear:")
    for i, gear in enumerate(gear_options, 1):
        print(f"{i}. {gear}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if choice in range(1, len(gear_options) + 1):
                return gear_options[choice - 1]
            else:
                print("Invalid choice. Please select a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the function for testing
if __name__ == "__main__":
    selected_gear = choose_gear()
    print(f"\nYou selected: {selected_gear}")
