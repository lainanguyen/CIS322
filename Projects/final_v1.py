import sys
import math

# V1: Getting bot to store data and attack spiders

'''
Comments:
        # _id: Unique identifier
        # _type: 0=monster, 1=your hero, 2=opponent hero
        # x: Position of this entity
        # shield_life: Ignore for this league; Count down until shield spell fades
        # is_controlled: Ignore for this league; Equals 1 when this entity is under a control spell
        # health: Remaining health of this monster
        # vx: Trajectory of this monster
        # near_base: 0=monster with no target yet, 1=monster targeting a base
        # threat_for: Given this monster's trajectory, is it a threat to 1=your base, 2=your opponent's base, 0=neither

        # To debug: print("Debug messages...", file=sys.stderr, flush=True)

'''

# base_x: The corner of the map representing your base
base_x, base_y = [int(i) for i in input().split()]
heroes_per_player = int(input())  # Always 3

# Save data forever (in between rounds)


# game loop
while True:
    # Data for EACH ROUND (replaced each round)
    spiders = []
    heroes = []
    enemies = []

    for i in range(2):
        # health: Each player's base health
        # mana: Ignore in the first league; Spend ten mana to cast a spell
        health, mana = [int(j) for j in input().split()]

    entity_count = int(input())  # Amount of heroes and monsters you can see

    for i in range(entity_count):
        _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for = [int(j) for j in input().split()]
        if _type == 0:
            spiders.append({"x": x, "y": y, "threat": threat_for, "targeted": 0})
        if _type == 1:
            heroes.append({"x": x, "y": y})
        if _type == 2:
            enemies.append({"x": x, "y": y})

    for i in range(heroes_per_player):
        action = ""
        s = {}
        min_distance = 100000

        for j in range(len(spiders)):
            if spiders[j]["threat"] == 1 and spiders[j]["targeted"] == 0:
                if math.dist([spiders[j]["x"]], spiders[j]["y"]) < min_distance:

                # action = f"MOVE {spiders[j]['x']} {spiders[j]['y']}"
                # spiders[j]["targeted"] = 1
                # # stop looping through spiders
                # break

        if action == "":
            action = "WAIT"
        print(action)