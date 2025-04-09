import random
from BattleSimulator import gameAssets
from os import system

# Prints out messages with multiple parts
def Dialogue(dialogue, attacker, defender):
    i = 0
    for line in dialogue:
        i += 1
        input(f'{line.format(lname=defender,wname=attacker)} ({i}/{len(dialogue)} Enter to Continue)')

# Inflicts the effects of attacks
def inflict_attack(attack, turn_taker, victim):

    def roll_nerves(nerves):

        roll = random.randint(1,int(nerves))

        if roll < nerves * 0.1:
            return 1.5
        elif roll < nerves:
            return 1
        
        if roll > nerves * 1.5:
            return 0
        elif roll > nerves:
            return 0.5

    nerve_multiplier = roll_nerves(turn_taker['max_nerves'])

    # IF the attack doesn't target self, have it affect the enemy
    if not attack['target_self']:

        health_effect = round(-1 * (((attack['damage'] * turn_taker['strength']) / victim['defense']) * nerve_multiplier))
        nerve_effect = round(-1 * (((attack['discomfort'] * turn_taker['strength']) / victim['defense']) * nerve_multiplier))

        health = victim['health'] + health_effect
        nerves = victim['nerves'] + nerve_effect

        if victim['nerves'] < victim['min_nerves']:
            victim['nerves'] = victim['min_nerves']

        target_self = False
    # IF the attack does target self, have it affect self
    else:

        health_effect = round(-1 * attack['damage'] * nerve_multiplier)
        nerve_effect = round(-1 * attack['discomfort'] * nerve_multiplier)


        health = turn_taker['health'] + health_effect
        nerves = turn_taker['nerves'] + nerve_effect

        # If the action makes the user have more health than they should, set nerves down to max
        if health > turn_taker['max_health']:
            health = turn_taker['max_health']
        
        # If the action makes the user have more nerves than they should, set nerves down to max
        if nerves > turn_taker['max_nerves']:
            nerves = turn_taker['max_nerves']

        target_self = True

    user_text = [f'{turn_taker['name']} used {attack['name']}']

    # Display message deprending on succesfulness
    match nerve_multiplier:
        case 0:
            effectiveness = ['Action was a complete failure.']
            Dialogue(user_text + attack['super_failure'] + effectiveness, turn_taker['name'], victim['name'])
        case 0.25:
            effectiveness = ['Action was a ineffective.']
            Dialogue(user_text + attack['failure'] + effectiveness, turn_taker['name'], victim['name'])         
        case 1:
            effectiveness = ['Action was a success!']
            Dialogue(user_text + attack['effective'] + effectiveness, turn_taker['name'], victim['name'])
        case 1.5:
            effectiveness = ['Action was super effective!']
            Dialogue(user_text + attack['super_effective'] + effectiveness, turn_taker['name'], victim['name'])

    # Indicates how much health and nerves the attack inflicts
    if target_self:
        print(f'{health_effect:+} health towards {turn_taker['name']}')
        print(f'{nerve_effect:+} nerves towards {turn_taker['name']}')
    else:
        print(f'{health_effect:+} health towards {victim['name']}')
        print(f'{nerve_effect:+} nerves towards {victim['name']}')

    return health, nerves, target_self

# Takes one turn
def take_turn(turn_taker, victim):

    while True:

        print(f"-!-!-!-!- {turn_taker['name']}'s Turn -!-!-!-!-")
        print('1. Check Stats \n2. Select Attack')
        
        match input('What do you want to do (Enter Number): '):

            # Check Stats
            case '1':
                # Prints Turn Taker's Stats
                print(f"-~-~-~-~- {turn_taker['name']}'s Stats -~-~-~-~-")
                print(f'{turn_taker['health']}/{turn_taker['max_health']} Health')
                print(f'{turn_taker['nerves']}/{turn_taker['max_nerves']} Nerves')
                print(f"Nerves can't go below {turn_taker['min_nerves']}")
                print(f'x{turn_taker['strength']} Damage Multipler')
                print(f'x{turn_taker['defense']} Damage Resistance')

                # Prints Victim's Stats
                print(f"-~-~-~-~- {victim['name']}'s Stats -~-~-~-~-")
                print(f"{victim['health']}/{victim['max_health']} Health")
                print(f"{victim['nerves']}/{victim['max_nerves']} Nerves")
                print(f"Nerves can't go below {victim['min_nerves']}")
                print(f"x{victim['strength']} Damage Multiplier")
                print(f"x{victim['defense']} Damage Resistance")

                input('(Enter to Continue)')

            case '2':
                # Prints all attack information
                print('Attacks:')
                i = 1
                for attack in turn_taker['attacks']:
                    print(f'{i}.    Attack: {attack['name']}')
                    print(f'          Damage: {attack['damage']}')
                    print(f'          Nerves: {-attack['discomfort']}')
                    i += 1

                # Selects Attack
                try:
                    choice = int(input('Which attack do you select? (Enter Number): '))
                    return inflict_attack(turn_taker['attacks'][choice - 1], turn_taker, victim)
                except:
                    pass

# Converts point-stats to actual stats. Example: 5 Health Points = 100 Health
def convert_stats(player):

    max_health = 25 + (int(player['health']) * 15)
    health = max_health

    max_nerves = 75 + (int(player['bravery']) * 5)
    nerves = max_nerves
    min_nerves = 25 + (int(player['bravery'] * 5))

    strength = 0.25 + (int(player['strength']) * 0.15)
    defense = 0.25 + (int(player['defense']) * 0.15)

    # Sets attacks to the attacks of the player's class
    attacks = []
    player_class = ''
    for character_class in gameAssets.classes:
        if character_class['name'] == player['class']:
            player_class = character_class
            attacks = character_class['attacks']

    return {'name': player['name'],
            'max_health': max_health,
            'health': health,
            'max_nerves': max_nerves,
            'nerves': nerves,
            'min_nerves': min_nerves,
            'strength': strength,
            'defense': defense,
            'attacks': attacks,
            'class': player_class}

def fight(character_1, character_2):

    input(f'-!-!-!-!- {character_1['name']} VS. {character_2['name']} -!-!-!-!- \n(Enter to continue)')

    turn = 0

    # Sets players to base stats
    player_1 = convert_stats(character_1)
    player_2 = convert_stats(character_2)

    while True:

        # If the turn is even, player 1 goes, if it's odd, player 2 goes
        if turn % 2 == 0:

            new_health, new_nerves, target_self = take_turn(turn_taker=player_1, victim=player_2)

            # Checks who should take the damage
            if not target_self:
                player_2['health'] = new_health
                player_2['nerves'] = new_nerves
            else:
                player_1['health'] = new_health
                player_1['nerves'] = new_nerves

            turn += 1
        elif turn % 2 == 1:

            new_health, new_nerves, target_self = take_turn(turn_taker=player_2, victim=player_1)

            # Checks who should take the damage
            if not target_self:
                player_1['health'] = new_health
                player_1['nerves'] = new_nerves
            else:
                player_2['health'] = new_health
                player_2['nerves'] = new_nerves

            turn += 1

        # Checks who won
        if player_1['health'] <= 0:
            print(f'{player_2['name']} Wins!')
            return character_2
        elif player_2['health'] <= 0:
            print(f'{player_1['name']} Wins!')
            return character_1