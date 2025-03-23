def determine_ending(won_final):
    """Determines the final outcome of the game."""
    if won_final:
        print("\n🏆 Congratulations! You are the Champion! 🏆")
    else:
        print("\nYou fought hard but lost in a close match. You are a Finalist.")
