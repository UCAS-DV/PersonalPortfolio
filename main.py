from TextAdventure import textadventure_main
from PersonalLibrary import personallibrary_main
from Quiz import quiz_main
from BattleSimulator import main as battlesim_main

def show_project(name, description, programming_process, lesson, main_function):
        if input(f'{name} \n\n- {description} \n\n- {programming_process} \n\n- {lesson} \nWould you like to use this project? If so, type "Yes": ').lower() == 'yes':
            main_function()
def main():
    while True:
        print("-~-~-~-~- Darius's Portfolio -~-~-~-~-")

        match input('1. What is a Portfolio? \n2. Projects \n3. Exit \nEnter the number of the option you select: '):
            case '1':
                print('A portfolio is...')
                input('(Enter to Continue)')
            case '2':
                while True:
                    print('-!-!-!-!- Projects -!-!-!-!-')
                    match input('1. Quest for the Country! \n2. Battle for the Country \n3. Personal Library\n4. Video Game Quiz \n5. \n6. \n7. Exit \nEnter the number of the project you want to see: '):
                        case '1':
                            show_project('Quest for the Country!', 'A text-based, turn-based, comedy RPG about going on a quest to reunite the constitution of the Even More United States of America to save the country. The game contains dozens of lines of comedic descriptions, a unique battle system, 5 bosses, and about 30 minutes of playtime.', 
                                         'The process of programming this game was mostly smooth. I began with the foundations, the map and battle system. After those I started writing the descriptions and cutscenes. I then quickly added the level up system once I saw it in the requirements. This was easily what took the longest. I was forced to cut one boss, Super-Robo-Julius-Caesar, from the game due to time constraints, and only Mr. Skellybones and the Voice In Your Head had the target 4 attacks. To make up for this, I made sure that the stats and attacks for the other 3 bosses made somewhat interesting battles despite the limited amount of attacks. I also included Super-Robo-Julius-Caesar as an NPC in a cutscene.', 
                                         "Quest for the Country's development taught me how to develop large projects in a timely manner, when to cut content and scope, and what content to cut when necessary.", 
                                         textadventure_main.main)
                        case '2':
                            show_project('Battle for the Country', 
                                         'A text-based game where you create characters and have them fight each other in turn-based battles to see which faction gets to host the annual celebrations for the reuniting of the constitution of EMUSA. This comedy battle simulator is a spin-off game of Quest For The Country. Characters level up as they win more battles, allowing them to boost their own stats and get stronger.', 
                                         "Battle for the Country's development was not as smooth as its predecessor's. I started with the character creation and battle system, but right before I started writing attack descriptions, I realized that I needed a level up system. The level up system was the hardest and most stressful part since it needed to modify a CSV file. Once I figured that out, it was smooth sailing, although tragically, the level up fiasco forced me to cut two classes, the North Dakotan Mage and the Vorlean.", 
                                         'Battle For The Country taught me how to modify CSV, which is a skill I was able to use for my personal finance project.',
                                         battlesim_main.main)
                        case '3':
                            show_project('Personal Library', 
                                         'A program where you can add to, remove from, and search a library of games sorted by genre, publisher, name, and release year.', 
                                         '_', 
                                         'This program taught me who to write search functions, which was extremely important for the Music Fesitival Group Project, and it taught me how to generally manage dictionaries of data.', personallibrary_main.main)
                        case '4':
                            show_project('Video Game Quiz', 
                                         'A simple quiz about video game history that adjusts difficulty depending on user answers.', 
                                         '_', 
                                         'This was one of my first projects in this class, and it taught me how to respond to user inputs', quiz_main.main)
                        case '5':
                            show_project('')
                        case '7':
                            break
            case '3':
                print('Leaving Portfolio...')
                break

main()