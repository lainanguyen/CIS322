import sys
import math

'''
Strategy: For this bot, I used a defensive strategy. I divided the heroes into 2 categories: offensive and defensive. 
I have 2 heroes that defend the base and target the spiders close to it.
1 hero goes to the enemy's base and targets spiders and enemies there. 
At the start of the game, the heroes slowly inch up until they approach a nearby spider or enemy and attack it.

Issue: I didn't use any mana for spells because it often directed spiders towards areas of my base that I didn't want it to go in so I played it safe
by not using it, even though it would increase my defense if it were to work properly.

Data Structures: The data structures used in this bot includes lists and dictionaries.

'''

# base_x: The corner of the map representing your base
base_x, base_y = [int(i) for i in input().split()]
heroes_per_player = int(input())

# Save data forever (in between rounds)

# game loop
while True:
    # Data for EACH ROUND (replaced each round)
    spiders_near_base = []      # Defense
    spiders_near_enemy = []     # Offense
    heroes = []
    enemies = []
    mymana = 0

    for i in range(2):
        # health: Each player's base health
        # mana: Ignore in the first league; Spend ten mana to cast a spell
        health, mana = [int(j) for j in input().split()]
        if i == 0:  # assuming first input is your health and mana
            mymana = mana

    entity_count = int(input())     # Amount of heroes and monsters you can see

    for i in range(entity_count):
        _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for = [int(j) for j in input().split()]
        if _type == 0:
            spider_info = {"x": x, "y": y, "health": health, "threat": threat_for, "targeted": 0}
            if threat_for == 1:
                spiders_near_base.append(spider_info)
            else:
                spiders_near_enemy.append(spider_info)
        if _type == 1:
            heroes.append({"x": x, "y": y})
        if _type == 2:
            enemies.append({"x": x, "y": y})

    for i in range(heroes_per_player):
        action = ""
        s = None
        e = None
        min_spider_distance = 100000
        min_enemy_distance = 100000

        if i < 2:  # Set up 2 defensive heroes
            for spider in spiders_near_base:
                s_loc = [spider["x"], spider["y"]]
                h_loc = [heroes[i]["x"], heroes[i]["y"]]
                if math.dist(s_loc, h_loc) < min_spider_distance:
                    s = spider
                    min_spider_distance = math.dist(s_loc, h_loc)
            if s is not None:
                action = f"MOVE {s['x']} {s['y']}"
                s["targeted"] += 1
        else:  # Set up last hero as 1 offensive hero
            for spider in spiders_near_enemy:
                s_loc = [spider["x"], spider["y"]]
                h_loc = [heroes[i]["x"], heroes[i]["y"]]
                if math.dist(s_loc, h_loc) < min_spider_distance:
                    s = spider
                    min_spider_distance = math.dist(s_loc, h_loc)
            for enemy in enemies:
                e_loc = [enemy["x"], enemy["y"]]
                h_loc = [heroes[i]["x"], heroes[i]["y"]]
                if math.dist(e_loc, h_loc) < min_enemy_distance:
                    e = enemy
                    min_enemy_distance = math.dist(e_loc, h_loc)
            if e is not None and min_enemy_distance < min_spider_distance:
                action = f"MOVE {e['x']} {e['y']}"
            elif s is not None:
                action = f"MOVE {s['x']} {s['y']}"
                s["targeted"] += 1

        # Inch towards enemy base at start of game
        if action == "":
            step_size = 100
            new_x = min(8800, heroes[i]["x"] + step_size)
            new_y = min(4400, heroes[i]["y"] + step_size)
            action = f"MOVE {new_x} {new_y}"

        print(action)
