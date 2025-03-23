import random
def elimination_match():
    """Simulates the first elimination match.
    
    Returns:
        bool: True if the player wins, False otherwise.
    """
    print("\nFirst Elimination Match!")
    if random.choice([True, False]):
        print("You won and move to the next round!")
        return True
    else:
        print("You lost the elimination match. Game Over.")
        return False