import characters_and_enemies as game
import time

# function player uses to attack
def player_attack():
    attack = input('Which attack would you like to use?\nEnter \'1\' for your flag-spear, \'2\' for your bayonet, or \'3\' for you unadulterated anger\n')
    x = game.dice(20)
    damage = game.dice(10) + game.dice(10) + game.dice(10)
# different options for attack depending on player choice
    if attack == '1':
        print('You used your flag-spear!')
        attack_roll = x + player_stats['agi']
# inventory can give bonus to attack roll
        if 'flag' in player_inventory:
            attack_roll += 5
        if attack_roll > enemy.stats['def'] and not x == 20:
            enemy.stats['health'] -= damage
            print(f"You did {damage} damage to your enemy!")
        elif x == 20:
            damage = 2*damage
            print(f"The attack was a crit! You did {damage} damage to your enemy!")
        else:
            print('Your attack missed!')
    elif attack == '2':
        print('You used your bayonet!')
        attack_roll = x + player_stats['str']
        if 'rifle' in player_inventory:
            attack_roll += 5
        if attack_roll > enemy.stats['def'] and not x == 20:
            enemy.stats['health'] -= damage
            print(f"You did {damage} damage to your enemy!")
        elif x == 20:
            damage = 2*damage
            print(f"The attack was a crit! You did {damage} damage to your enemy!")
        else:
            print('Your attack missed!')
    elif attack == '3':
        print('You used your unadulterated anger!')
        attack_roll = x + player_stats['cha']
        if 'book' in player_inventory:
            attack_roll += 5
        if attack_roll > enemy.stats['wil'] and not x == 20:
            enemy.stats['health'] -= damage
            print(f"You did {damage} damage to your enemy!")
        elif x == 20:
            damage = 2*damage
            print(f"The attack was a crit! You did {damage} damage to your enemy!")
        else:
            print('Your attack missed!')
    else:
        print('That is not an attack, your turn will be skipped :(')

# first combat encounter
def combat1():
    a = game.Grunt()
    b = game.Grunt()
    c = game.Rifle()
    d = game.Stalling()
# while there are enemies alive
    while not (a.stats['health'] <= 0 and b.stats['health'] <= 0 and c.stats['health'] <= 0):
# chooses enemy to attack
        question = input('Who would you like to attack?\nEnter \'1\' for the leader (a rifleman), \'2\' for his sergeant (a grunt), or \'3\' for the private (another grunt)?\n')
        if question == '1':
            enemy = c
            print('You are attacking the leader!')
        elif question == '2':
            enemy = a
            print('You are attacking the sergeant!')
        elif question == '3':
            enemy = b
            print('You are attacking the private!')
        else:
            enemy = d
            print('You are attacking nothing and wasting your turn, good job!')
        time.sleep(1)
# attacks happen
        player_attack()
        time.sleep(1)
# enemy olnly attacks if alive
        while a.stats['health'] > 0:
            time.sleep(1)
            a.attack()
        while c.stats['health'] > 0:
            time.sleep(1)
            c.attack()
        while b.stats['health'] > 0:
            time.sleep(1)
            b.attack

# second combat encounter
def combat2():
    e = game.Tsar()
    enemy = e
    while e.stats['health']:
        player_attack()
        time.sleep(1)
        e.attack()
        time.sleep(1)



