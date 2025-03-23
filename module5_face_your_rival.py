import random
def face_rival():
    """Finals - The player faces their biggest rival.
    
    Returns:
        bool: True if the player wins, False otherwise.
    """
    print("\nFinals - Facing Your Rival!")
    choice = input("Do you regulate endurance? (yes/no): ").strip().lower()
    if choice == "yes":
        print("You fight strategically and have a higher chance to win!")
        return random.choice([True, True, False])  # Higher chance of winning
    else:
        print("You tire quickly and struggle in the match...")
        return random.choice([True, False, False])  # Lower chance of winning