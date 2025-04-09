# Races
race_human = {
    "name": "Human",
    "health": 100,
    "dexterity": 100,
    "intelligence": 100
}
race_elf = {
    "name": "Elf",
    "health": 75,
    "dexterity": 115,
    "intelligence": 150
}
race_orc = {
    "name": "Orc",
    "health": 150,
    "dexterity": 70,
    "intelligence": 60
}

races = [race_human,race_elf,race_orc]

# Classes
class_warrior = {
    "name": "Warrior",
    "health_bonus": 75,
    "dexterity_bonus": -30,
    "intelligence_bonus": -50
}
class_outlaw = {
    "name": "Outlaw",
    "health_bonus": 10,
    "dexterity_bonus": 30,
    "intelligence_bonus": 20
}
class_embezzeler = {
    "name": "Embezzeler",
    "health_bonus": -20,
    "dexterity_bonus": -20,
    "intelligence_bonus": 60
}
classes = [class_embezzeler, class_warrior, class_outlaw]

stats = {
    "class": "",
    "race": "",
    "health": -1,
    "dexterity": -1,
    "intelligence": -1
}

def main():

    race_chosen = False
    player_race = ""

    print("~-~-~-~-~-~-Create Your Character~-~-~-~-~-~-")

    while True:
        
        if not race_chosen:

            print("Choose your race")

            for race in races:
                print(f"- {race["name"]}")

            player_race = input("Make your selection: ").lower()

            if player_race not in ["human", "orc", "elf", "microbe"]:
                print("Invalid Choice!")
                continue

            race_chosen = True

        for race in races:
            if race["name"].lower() == player_race:
                stats["race"] = player_race.capitalize()
                stats["health"] = race["health"]
                stats["dexterity"] = race["dexterity"]
                stats["intelligence"] = race["intelligence"]

        print("Choose your class")
        for class_choice in classes:
            print(f"- {class_choice["name"]}")
        
        player_class = input("Make your selection: ").lower()

        if player_class not in ["warrior", "outlaw", "embezzeler"]:
            print("Invalid Choice!")
            continue

        for class_choice in classes:
            if class_choice["name"].lower() == player_class:
                stats["class"] = player_class.capitalize()
                stats["health"] += class_choice["health_bonus"]
                stats["dexterity"] += class_choice["dexterity_bonus"]
                stats["intelligence"] += class_choice["intelligence_bonus"]

        break

    print("~-~-~-~-~-~-Your Character~-~-~-~-~-~-")
    print(f"Race: {stats['race']}")
    print(f"Class: {stats['class']}")
    print(f"Health: {stats['health']}")
    print(f"Dexterity: {stats['dexterity']}")
    print(f"Intelligence: {stats['intelligence']}")

    print("\nNo Take-Backsies!")