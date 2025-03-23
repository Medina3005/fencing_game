import random

def train_with_coach():
    """Simulates a training session where the coach gives random advice."""
    advice_list = [
        "Focus on footwork! Movement is key to winning.",
        "Watch your opponent’s blade carefully before attacking.",
        "Stay calm under pressure. A good fencer controls the pace.",
        "Always keep your guard up to avoid quick strikes.",
        "Precision is better than speed. Aim for clean hits!"
    ]
    
    print("\n🏋️ Training Session with Your Coach 🏋️")
    print("Your coach is giving you some important advice...")
    
    # Randomly select one piece of advice
    advice = random.choice(advice_list)
    print(f"📢 Coach: '{advice}'")

# Call the function in the game flow
train_with_coach()
