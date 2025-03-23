import random

def group_stage():
    """Simulates the group stage matches and returns whether the player qualifies."""
    print("\nGroup Stage Begins!")
    win_count = 0

    for i in range(3):
        print(f"Match {i+1}: Fighting...")
        if random.choice([True, False]):  # Correct usage of random.choice
            print("You won this match!")
            win_count += 1
        else:
            print("You lost this match.")

    if win_count >= 2:
        print("You qualified for the next round!")
        return True
    else:
        print("You did not qualify. Game Over.")
        return False

# Call the function
qualified = group_stage()

