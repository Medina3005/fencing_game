#Medina Kubanychbekova
#03/09/2025
# Problem 5 - Character class and item checking
class Character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses

# Checking if character can perform tasks
def check_tasks(player):
    tasks = {
        "Climb a mountain": {"items": {"rope", "coat", "first aid kit"}, "debuff": "slow"},
        "Cook a meal": {"items": {"pan", "groceries"}, "debuff": "small"},
        "Write a book": {"items": {"pen", "paper", "idea"}, "debuff": "confusion"}
    }
    
    for task, req in tasks.items():
        if req["items"].issubset(set(player.weapons)) and req["debuff"] not in player.weaknesses:
            print(f"{task}: Success! You have all the required items.")
        else:
            print(f"{task}: Failed. You are missing some items or have a debuff.")

# Create a character and check tasks
player1 = Character('Dragon Slayer', ['pan', 'paper', 'idea', 'rope', 'groceries'], ['slow'])
for item in player1.weapons:
    print("Item:", item)
for debuff in player1.weaknesses:
    print("Debuff:", debuff)

check_tasks(player1)
