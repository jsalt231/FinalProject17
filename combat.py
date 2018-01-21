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
        attack_roll = x + game.player_stats['agi']
# inventory can give bonus to attack roll
        if 'flag' in game.player_inventory:
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
        attack_roll = x + game.player_stats['str']
        if 'rifle' in game.player_inventory:
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
        attack_roll = x + game.player_stats['cha']
        if 'book' in game.player_inventory:
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
    global enemy
    a = game.Grunt()
    b = game.Grunt()
    c = game.Rifle()
    d = game.Stalling()
# while there are enemies alive and while you are alive
    while not (a.stats['health'] <= 0 and b.stats['health'] <= 0 and c.stats['health'] <= 0) or game.player_stats['health'] > 0:
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
# yor attack
        player_attack()
        time.sleep(1)
# enemies attack in set order, only attacks if alive
        while a.stats['health'] > 0:
            time.sleep(1)
            a.attack()
            break
        while c.stats['health'] > 0:
            time.sleep(1)
            c.attack()
            break
        while b.stats['health'] > 0:
            time.sleep(1)
            b.attack()
            break
# second combat encounter
def combat2():
    global enemy
    e = game.Tsar()
    enemy = e
    while e.stats['health'] > 0 or game.player_stats['health'] > 0:
        player_attack()
        time.sleep(1)
        e.attack()
        time.sleep(1)
        break

def encounter1():
    question = input('Enter \'1\' to help the woman, \'2\' to ignore her, or \'3\' to loot her dying body\n')
    if question == '1':
        time.sleep(1)
        print('You use all your might to pull the woman out of the building!')
        time.sleep(1)
        print('She says "Oh, thank you sonny, I owe you my life! Here take this!" and hands you two vials.')
        question2 = input('Do you drink them? Enter \'y\' for yes or \'n\' for no\n')
        if question2 == 'y':
            time.sleep(1)
            print('You drink the vials and feel much, much stronger! Your health has gone up!')
            game.player_stats['health'] += 50
        elif question2 == 'n':
            time.sleep(1)
            print('The bottles topple to the floor and shatter. With the old lady looking in horror, you carry on in your mission.')
        else:
            print('Stop trying to break my code! I\'m subtracting 50 health now get out of my sight smh')
            game.player_stats['health'] -= 50
    if question == '2':
        time.sleep(1)
        print('The old lady shouts "Damn you, commie punk!" as you continue on your way. Wow, you\'re a terrible person lol')
    if question == '3':
        time.sleep(1)
        print('Wow, you\'re a really bad person. You loot the old lady as she shouts "Damn you, damn you!"')
        time.sleep(1)
        question3 = input('You find a vial filled with a green liquid, do you drink it? Enter \'y\' for yes or \'n\' for no\n')
        if question3 == 'y':
            time.sleep(1)
            print('You drink the vials and feel much, much stronger! Your health has gone up!')
            game.player_stats['health'] += 25
        elif question3 == 'n':
            time.sleep(1)
            print('The bottles topple to the floor and shatter. With the old lady looking in horror, you carry on in your mission.')
        else:
            print('Stop trying to break my code! I\'m subtracting 25 from your health now get out of my sight smh')
            game.player_stats['health'] -= 25





