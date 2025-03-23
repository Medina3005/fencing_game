import random

# Module 8: The Championship Match
def championship_match():
    """Final match to determine if the player wins the tournament."""
    print("\n🏆 Championship Match: The Final Battle Begins! 🏆")

    strategy = input("Do you want to play aggressively or defensively? (aggressive/defensive): ").lower()

    if strategy == "aggressive":
        print("\nYou go on the offensive, attacking with speed and precision!")
        chance_of_winning = 0.6  # 60% chance of winning
    elif strategy == "defensive":
        print("\nYou focus on defense, waiting for the perfect counterattack!")
        chance_of_winning = 0.7  # 70% chance of winning
    else:
        print("\nYou hesitate, unsure of your strategy. Your opponent takes advantage!")
        chance_of_winning = 0.4  # 40% chance of winning due to hesitation

    # Randomly determine if the player wins the championship
    if random.random() < chance_of_winning:
        print("\n🔥 You land the final hit and win the Championship! You are the Fencing Champion! 🏅")
        return True
    else:
        print("\n😢 You fought hard, but your opponent defeats you. You are the runner-up.")
        return False
