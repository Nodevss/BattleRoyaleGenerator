# made by nodevs =D

import random
import time

usernamewordlist = [
    "Green", "Blue", "The", "Fish", "Cow", "Dog", "Cat", "Bird", "Lion", "Tiger", "TNT",
    "Lover", "Hater", "Alpha", "School", "Weeknd", "Samsung", "Apple", "Jeffery", "Jeff",
    "Harold", "Spider", "Skull", "Emoji", "NuhUh", "Gojo", "Jojo", "Dio",
    "Phantom", "Stand", "Zebra", "Kira", "Jotaro", "Stardust",
    "Zenyatta", "Joseph", "Speedwagon", "Polnareff", "Giorno",
    "Bruno", "Abbacchio", "Mista", "Trish",
    "GoldExperience", "CrazyDiamond", "StoneOcean",
    "Josuke", "EnricoPucci", "Diavolo",
    "BitesTheDust", "Aviation",
    "SilverChariot", "TheWorld",
    "SoftAndWet"
]

weapons = ["pickaxe", "Boom Bow", 
           "shotgun", 
           "Assault Rifle",
           "SMG",
           "Kinetic Blade",
           "sniper",
           "pistol"]
healing_items = ["Medkit",
                 "Bandages",
                 "Shield Potion"]

usernamesList = ["nodev"]

# match countdown 
match_number = 5

for i in range(0, 5):
    print("Match begins in "+ str(match_number) + "...") 
    time.sleep(1)
    match_number -= 1

# bot username generator :P
for i in range(0, 10):
    time.sleep(0.5)
    ListNumber1 = random.randint(0, len(usernamewordlist) - 1)
    ListNumber2 = random.randint(0, len(usernamewordlist) - 1)

    while ListNumber1 == ListNumber2:
        ListNumber2 = random.randint(0, len(usernamewordlist) - 1)

    UserNumber = random.randint(0, 99)

    username = usernamewordlist[ListNumber1] + usernamewordlist[ListNumber2] + str(UserNumber)

    print(username +  " has thanked the bus driver")

    usernamesList.append(username)

# health system
player_health = {username: 100 for username in usernamesList}
player_scores = {username: 0 for username in usernamesList}
player_inventory = {username: [] for username in usernamesList}

def storm_damage():
    for player in list(usernamesList):  
        if random.random() < 0.2:  
            player_health[player] -= 10
            print(f"{player} took 10 storm damage")
            time.sleep(0.5)
            if player_health[player] <= 0:
                print(f"{player} was eliminated by the storm")
                usernamesList.remove(player)
                del player_health[player]
                del player_scores[player]
                del player_inventory[player]
                time.sleep(1)

# battle royale part 
round_number = 1
while len(usernamesList) > 1:
    print(f"\nStorm Circle {round_number}")
    time.sleep(1)

    username1 = random.choice(usernamesList)
    username2 = random.choice(usernamesList)

    while username1 == username2:
        username2 = random.choice(usernamesList)

    weapon = random.choice(weapons)

    # improved combat system
    damage = random.randint(10, 50)
    player_health[username2] -= damage

    if player_health[username2] <= 0:
        print(f"{username1} eliminated {username2} with a {weapon}")
        usernamesList.remove(username2)
        player_scores[username1] += 1
        del player_health[username2]
        del player_scores[username2]
        del player_inventory[username2]

    else:
        print(f"{username1} shot {username2} for {damage} damage with a {weapon}")

    time.sleep(1.5)

    # healing
    if random.random() < 0.3:  
        healing_player = random.choice([username1, username2])

        if healing_player in usernamesList:  
            item = random.choice(healing_items)
            heal_amount = random.randint(25, 50)
            player_health[healing_player] = min(100, player_health[healing_player] + heal_amount)
            print(f"{healing_player} used a {item} and gained {heal_amount}")
            time.sleep(1)

    # inventory
    if random.random() < 0.4:  
        item_finder = random.choice(usernamesList)
        item = random.choice(weapons + healing_items)
        player_inventory[item_finder].append(item)

    # scary storm damage
    storm_damage()

    # display current players and health
    print("\nRemaining players:")

    for player in usernamesList:
        print(f"{player}: Health: {player_health[player]}, Eliminations: {player_scores[player]}")

    time.sleep(2)

    round_number += 1

winner = usernamesList[0]
print(f"\n{winner} has won the game and dogged on {player_scores[winner]} kids lmao")
