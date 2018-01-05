leo_stats = {'str': 4, 'int': 4, 'agi': 4, 'cha': 4, 'health': 100}
joey_stats = {'str': 7, 'int': 1, 'agi': 5, 'cha': 3, 'health': 120}
vlad_stats = {'str': 2, 'int': 7, 'agi': 1, 'cha': 6, 'health': 80}

def assignment():
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

