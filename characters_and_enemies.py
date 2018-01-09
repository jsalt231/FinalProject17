import random

# Stats for chooseable characters
leo_stats = {'str': 4, 'int': 4, 'agi': 4, 'cha': 4, 'def': 14, 'health': 100}
joey_stats = {'str': 7, 'int': 1, 'agi': 5, 'cha': 3, 'def': 18, 'health': 110}
vlad_stats = {'str': 2, 'int': 7, 'agi': 1, 'cha': 6, 'def': 10, 'health': 90}

# basic dice rolling function
def dice(x):
    global roll
    roll = random.randint(1, x)
    return roll

# function to choose character, assign stats and inventory
def assignment():
    global player_stats
    global player_inventory
    while True:
        answer = input("Who would you like to play? Enter 1 for Leo, 2 for Joey, and 3 for Vlad\n")
        answer = int(answer)
        if answer == 1:
            player = 'leo'
            break
        elif answer == 2:
            player = 'joey'
            break
        elif answer == 3:
            player = 'vlad'
            break
        else:
            print("I'm sorry, that's not an option. Try again!")

    print(f"You have chosen to play as {player.title()}")
    if player == 'leo':
        player_stats = leo_stats
        player_inventory = ['flag']
    if player == 'joey':
        player_stats = joey_stats
        player_inventory = ['rifle']
    if player == 'vlad':
        player_stats = vlad_stats
        player_inventory = ['book']

    print(f"""Your stats as as follows:
    Strength = {player_stats['str']}, Intelligence = {player_stats['int']}, Agility = {player_stats['agi']}, and Charisma = {player_stats['cha']}
You have the following in your inventory:
    {player_inventory[0].title()}""")

class Tsar(object):
    global attack_roll
    def __init__(self):
        self.stats = {'str': 7, 'int': 6, 'agi': 8, 'cha': 5, 'def': 20, 'health': 150}
    def attack1(self):
        print("The Tsar used the Spear of Romanov!")
        x = dice(20)
        attack_roll = x + self.stats['str']
        if x == 20:
            damage = 2*(dice(8) + dice(8) + dice(8))
            player_stats['health'] -= damage
            print(f"The attack was a crit! You take {damage} damage!")
        if not x == 20 and attack_roll > player_stats['def'] :
            damage = dice(8) + dice(8) + dice(8)
            print("The attack was successful! You take {damage} damage!")
            player_stats['health'] -= damage
        if attack_roll <= player_stats['def']:
            print("The attack was unsuccessful! You take no damage!")





