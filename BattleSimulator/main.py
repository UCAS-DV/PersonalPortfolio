from BattleSimulator import character_create
from BattleSimulator import battle
from BattleSimulator import gameAssets
import os
import random
import matplotlib.pyplot as plt
import pandas as pd

def choose_characters(preview):
    characters = character_create.read_characters()
    
    character_names = []

    # Determines which player goes first
    def determine_order(choice_1, choice_2):

        # Whatever player has the higher speed goes first
        if choice_1['speed'] > choice_2['speed']:
            input(f"{choice_1['name']}'s {choice_1['speed']} Speed > {choice_2['name']}'s {choice_2['speed']} Speed \n{choice_1['name']} goes first! (Enter to Continue)")
            return choice_1, choice_2
        elif choice_2['speed'] > choice_1['speed']:
            input(f"{choice_2['name']}'s {choice_2['speed']} Speed > {choice_1['name']}'s {choice_1['speed']} Speed \n{choice_2['name']} goes first! (Enter to Continue)")
            return choice_2, choice_1
        
        # If both players have the same speed, randomly choose between either one
        elif choice_1['speed'] == choice_2['speed']:

            if random.randint(1,10) <= 5:
                input(f'Tied Speed \n {choice_1['name']} goes first! (Enter to Continue)')
                return choice_1, choice_2
            else:
                input(f'Tied Speed \n {choice_2['name']} goes first! (Enter to Continue)')
                return choice_2, choice_1
            
    # Chooses character based on user input
    def choose_character():

        choosen_character = {}

        while True:

            i = 1
            for character in characters:
                character_names.append(character['name'].lower())

                print(f'{i}. {character['name']} - {character['class']} - Lvl {character['level']} - {character['wins']} Wins')
                i += 1

            choice = input('Choose a character to look at (Enter name): ').lower()
            if choice in character_names:

                for character in characters:
                    if choice == character['name'].lower():
                        choosen_character = character

                names = []
                values = []
                choosen_character_data = []

                for stat in choosen_character:          

                    if stat not in ['name', 'class', 'backstory']:
                        names.append(stat.capitalize())
                        values.append(int(choosen_character[stat]))
                        if stat not in ['wins', 'level']:
                            choosen_character_data.append(int(choosen_character[stat]))

                # Visualizes stats

                plt.bar(x=names,height=values)
                plt.show()

                character_data = pd.DataFrame([choosen_character_data])

                print(f'Stat Average: {character_data.mean(1).values[0]}')
                print(f'Mode of Stats: {character_data.mode(1).values[0]}')
                print(f'Median Stat: {character_data.median(1).values[0]}')
                print(f'Highest Stat: {character_data.max(1).values[0]}')
                print(f'Lowest Stat: {character_data.min(1).values[0]}')

                if input('Do you want to select this character? If so, type "Yes": ').lower() == 'yes':
                    return choosen_character

    if not preview:   
        character_1, character_2 = determine_order(choose_character(), choose_character())
        return character_1, character_2
    else:
        return choose_character()

# Main function  
def main():
    
    while True:

        os.system('Cls')

        print('-~-~-~-~- Battle for the Country -~-~-~-~-')

        # Checks if there are enough characters to battle with
        if len(character_create.read_characters()) >= 2:

            match input('1. Backstory \n2. Create Fighter \n3. Fighter List \n4. Battle \n5. Exit \nEnter the number of the option you want to select: '):

                # Backstory
                case '1':
                    battle.Dialogue(gameAssets.intro, 0, 0)
                
                # Create Character
                case '2':
                    character_create.create_character()

                # Choose Character
                case '3':
                    choose_characters(True)

                # Battle
                case '4':

                    while True:

                        match input('-!-!-!-!- Battle -!-!-!-!- \n1. Tutorial \n2. Battle \n3. Back \nEnter the number of the option you want to select: '):

                            # Tutorial
                            case '1':
                                battle.Dialogue(gameAssets.tutorial, 0, 0)

                            # Battle
                            case '2':
                                player_1, player_2 = choose_characters(False)

                                if player_1 != player_2:
                                    # Determine winner of battle by having battle
                                    winner = battle.fight(player_1, player_2)

                                    character_create.edit_character(winner, 'wins', int(winner['wins']) + 1)

                                    winner['wins'] = str(int(winner['wins']) + 1)

                                    # Checks if the player has enough wins to level up
                                    if int(winner['wins']) > int(winner['level']) * 2:
                                        
                                        character_create.edit_character(winner, 'level', int(winner['level']) + 1)
                                        input(f'{winner['name']} is now at Level {int(winner['level']) + 1}')

                                        winner['level'] = str(int(winner['level']) + 1)

                                        while True:
                                            match input('Which stat do you want to buff by one point? \n1. Health \n2. Strength \n3. Defense \n4. Speed \n5. Bravery \nEnter Number: '):

                                                # Health
                                                case '1':
                                                    character_create.edit_character(winner, 'health', int(winner['health']) + 1)
                                                    print(f"{winner['name']} now has {int(winner['health']) + 1} health points.")
                                                    break

                                                # Strength
                                                case '2':
                                                    character_create.edit_character(winner, 'strength', int(winner['strength']) + 1)
                                                    print(f"{winner['name']} now has {int(winner['strength']) + 1} strength points.")
                                                    break

                                                # Defense
                                                case '3':
                                                    character_create.edit_character(winner, 'defense', int(winner['defense']) + 1)
                                                    print(f"{winner['name']} now has {int(winner['defense']) + 1} defense points.")
                                                    break

                                                # Speed
                                                case '4':
                                                    character_create.edit_character(winner, 'speed', int(winner['speed']) + 1)
                                                    print(f"{winner['name']} now has {int(winner['speed']) + 1} speed points.")
                                                    break

                                                # Bravery
                                                case '5':
                                                    character_create.edit_character(winner, 'bravery', int(winner['bravery']) + 1)
                                                    print(f"{winner['name']} now has {int(winner['bravery']) + 1} bravery points.")
                                                    break


                            # Back
                            case '3':
                                break

                # Exit
                case '5':
                    print('Exiting Game...')
                    break
        else:
            input('No fighters found. (Enter to Continue)')
            input('Creating First Fighter... (Enter to Continue)')
            character_create.create_character()
            input('Creating Second Fighter... (Enter to Continue)')
            character_create.create_character()
