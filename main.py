# made by nodevs =D

import random
import time

usernamewordlist = ["Green",
                "Blue",
                "The",
                        "Fish",
                        "Cow",
                        "Dog",
                        "Cat",
                        "Bird",
                        "Lion",
                        "Tiger",
                        "TNT",
                    "Lover",
                    "Hater",
                    "Alpha",
                    "School",
                    "Weeknd",
                    "Samsung",
                    "Apple",
                    "Jeffery",
                    "Jeff",
                    "Harold",
                    "Spider",
                    "Skull",
                    "Emoji",
                    "NuhUh",
                    "Gojo",
                    "Jojo"
                    "Dio"
]


weapons = ["pickaxe", "Boom Bow", "shotgun", "Assault Rifle", "SMG", "Kinetic Blade",
           "sniper", "pistol"]

usernamesList = ["nodev"]

#match countdown 
match_number = 5

for i in range(0,5):
  print("Match begins in " + str(match_number) + "...")
  time.sleep(1)
  match_number = match_number - 1

# bot username generator :P
for i in range(0,10):
  time.sleep(0.5)
  ListNumber1 = random.randint(0, len(usernamewordlist) - 1)
  ListNumber2 = random.randint(0, len(usernamewordlist) - 1)

  while ListNumber1 == ListNumber2:
    ListNumber2 = random.randint(0, len(usernamewordlist) - 1)

  UserNumber = random.randint(0,99)

  username = usernamewordlist[ListNumber1] + usernamewordlist[ListNumber2] + str(UserNumber)
  
  print(username + " has thanked the bus driver")

  usernamesList.append(username)


#battle royale part 

while len(usernamesList) > 1:
  username1 = random.choice(usernamesList)
  username2 = random.choice(usernamesList)
  weapon = random.choice(weapons)
  usernamesList.remove(username2)

  print(username1 + " killed " + username2 + " with a " + weapon)

  time.sleep(random.randint(0,5))

print(usernamesList[0] + " has won the game")

  
  
