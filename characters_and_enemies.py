import random

# Stats for chooseable characters
leo_stats = {'str': 4, 'int': 4, 'agi': 4, 'cha': 4, 'def': 14, 'wil': 14, 'health': 100}
joey_stats = {'str': 7, 'int': 1, 'agi': 5, 'cha': 3, 'def': 16, 'wil': 12, 'health': 110}
vlad_stats = {'str': 2, 'int': 7, 'agi': 1, 'cha': 6, 'def': 12, 'wil': 16, 'health': 90}

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
        if answer == '1':
            player = 'leo'
            break
        elif answer == '2':
            player = 'joey'
            break
        elif answer == '3':
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

# enemy classes, basic combat system sorta
class Tsar(object):
    def __init__(self):
        self.stats = {'str': 7, 'int': 6, 'agi': 8, 'cha': 5, 'def': 18, 'wil': 18, 'health': 150}
# Tsar class' attack function, has two randomly selected options using different stats and attacking different defense stat (wil or def)
    def attack(self):
        x = dice(20)
        y = dice(2)
        if y == 1:
            damage = dice(8) + dice(8) + dice(8)
            attack_roll = x + self.stats['str']
            print("The Tsar used the Spear of Romanov!")
        if y == 2:
            damage = dice(8) + dice(8) + dice(6)
            attack_roll = x + self.stats['cha']
            print("The Tsar used Cry for Unity!")
        if x == 20:
            damage = 2*damage
            player_stats['health'] -= damage
            print(f"The attack was a crit! You take {damage} damage!")
# attack_roll applied to either def or wil depending on the attack used
        elif x < 20 and ((y == 1 and attack_roll > player_stats['def']) or (y == 2 and attack_roll > player_stats['wil'])):
            print(f"The attack was successful! You take {damage} damage!")
            player_stats['health'] -= damage
        else:
            print(f"The attack was unsuccessful! You take no damage!")

class Grunt(object):
    def __init__(self):
        self.stats = {'str': 4, 'int': 2, 'agi': 3, 'cha': 2, 'def': 10, 'wil': 8, 'health': 30}
# Grunt class' attack function, has two randomly selected options using different stats and attacking different defense stat (wil or def)
    def attack(self):
        x = dice(20)
        y = dice(2)
        if y == 1:
            damage = dice(8) + dice(6)
            attack_roll = x + self.stats['str']
            print("The Grunt used his billy club!")
        if y == 2:
            damage = dice(6) + dice(6) + 1
            attack_roll = x + self.stats['cha']
            print("The Grunt used screech!")
        if x == 20:
            damage = 2*damage
            player_stats['health'] -= damage
            print(f"The attack was a crit! You take {damage} damage!")
# attack_roll applied to either def or wil depending on the attack used
        elif x < 20 and ((y == 1 and attack_roll > player_stats['def']) or (y == 2 and attack_roll > player_stats['wil'])):
            print(f"The attack was successful! You take {damage} damage!")
            player_stats['health'] -= damage
        else:
            print(f"The attack was unsuccessful! You take no damage!")

class Rifle(object):
    def __init__(self):
        self.stats = {'str': 3, 'int': 6, 'agi': 2, 'cha': 4, 'def': 12, 'wil': 14, 'health': 35}
# Rifle class' attack function, has two random;y selected options using different stats and attacking different defense stat (wil or def)
    def attack(self):
        x = dice(20)
        y = dice(2)
        if y == 1:
            damage = dice(8) + dice(8) + dice(6)
            attack_roll = x + self.stats['int']
            print("The Rifleman used his gun!")
        if y == 2:
            damage = dice(6) + dice(6) + 3
            attack_roll = x + self.stats['str']
            print("The Rifleman used his blade!")
        if x == 20:
            damage = 2*damage
            player_stats['health'] -= damage
            print(f"The attack was a crit! You take {damage} damage!")
# attack_roll applied to either def or wil depending on the attack used
        elif x < 20 and attack_roll > player_stats['def']:
            print(f"The attack was successful! You take {damage} damage!")
            player_stats['health'] -= damage
        else:
            print(f"The attack was unsuccessful! You take no damage!")

# useless class added to make it harder to break the game
class Stalling():
    def __init__(self):
        self.stats = {'def': 100}