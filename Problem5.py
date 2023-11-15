# Francisco Sanchez
# 11/15/23

class Character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_nickname(self):
        return self.nickname

    def get_weapons(self):
        return self.weapons

    def get_weaknesses(self):
        return self. weaknesses

    def profile(self):
        return self.nickname, self.weapons, self. weaknesses


def check_character_status(character):
    # Check if all required items for Task 1 are picked up
    task1_required_items = ['rope', 'coat', 'first aid kit']
    if all(item in character.get_weapons() for item in task1_required_items):
        print("Character has all required items for Task 1: Climb a mountain.")
    else:
        print("Character is missing some required items for Task 1.")

    # Check if all required items for Task 2 are picked up
    task2_required_items = ['pan', 'groceries']
    if all(item in character.get_weapons() for item in task2_required_items):
        print("Character has all required items for Task 2: Cook a meal.")
    else:
        print("Character is missing some required items for Task 2.")

    # Check if all required items for Task 3 are picked up
    task3_required_items = ['pen', 'paper', 'idea']
    if all(item in character.get_weapons() for item in task3_required_items):
        print("Character has all required items for Task 3: Write a book.")
    else:
        print("Character is missing some required items for Task 3.")

    # Check for status debuffs
    status_debuffs = ['slow']
    if any(debuff in character.get_weaknesses() for debuff in status_debuffs):
        print("Character has a status debuff: slow.")
    else:
        print("Character does not have any status debuffs.")


# Creating an instance of the Character class
player1 = Character('Dragon Slayer',['Pan','Paper', 'idea', 'rope', 'groceries'], ['slow'])

# Accessing and printing individual attributes
print("Nickname:", player1.get_nickname())
print("Weapons:", player1.get_weapons())
print("Weaknesses:", player1.get_weaknesses())

# printing the profile
print("Profile:", player1.profile())

# Call the new function to check character status
check_character_status(player1)

# Looping through weapons
print("Weapons:")
for item in player1.get_weapons():
    print("Item:", item)

# Looping through weaknesses
print("Weaknesses:")
for debuff in player1.get_weaknesses():
    print("Debuff:", debuff)
