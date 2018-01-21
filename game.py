# necessary modules (mainly ones I made yay)
import characters_and_enemies as game
import plot as story
import combat as fight
import time

# beginning of game
question = input('Would you like to see the author\'s note? Enter \'y\' for yes or \'n\' for no\n')
time.sleep(1)
if question == 'y':
    story.authors_note()
    story.plot1()
elif question == 'n':
    story.plot1()
else:
    print('Okay you\'re trying to break my code so I guess not')
    time.sleep(1)
    story.plot1()
# stats and inventories assigned based on chosen charactes
player_stuff = game.assignment()
player = player_stuff[0]
player_stats = player_stuff[1]
player_inventory = player_stuff[2]

# tells player their stats and inventory
time.sleep(1)
print(f"""Your stats are as follows:
Strength = {player_stats['str']}, Intelligence {player_stats['int']}, Agility = {player_stats['agi']}, Charisma = {player_stats['cha']},
Defense = {player_stats['def']}, Willpower = {player_stats['wil']} and Health = {player_stats['health']}""")
time.sleep(1)
print(f"""You have the following inventory:
{player_inventory[0].title()}""")


while True:
    story.plot2()
    fight.combat1()
# if you die in combat this loop breaks, giving you one of the endings at the bottom
    if player_stats['health'] <= 0:
        break
    story.plot3()
    fight.encounter1()
    story.plot4()
    fight.combat2()
# if you die in combat this loop breaks, giving you one of the endings at the bottom
    if player_stats['health'] <= 0:
        break
    story.plot5()
# each character gets their own ending
    if player == 'leo':
        story.ending3()
        break
    if player == 'joey':
        story.ending4()
        break
    if player == 'vlad':
        story.ending5()
        break
# you are given one of two endings if you die
if player_stats['health'] <= 0:
    q = game.dice(2)
    if q == 1:
        story.ending1()
    if q == 2:
        story.ending2()




