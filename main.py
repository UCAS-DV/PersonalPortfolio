from TextAdventure import textadventure_main
from PersonalLibrary import personallibrary_main
from Quiz import quiz_main

def show_project(name, description, programming_process, lesson, main_function):
        if input(f'{name} \n- {description} \n- {programming_process} \n- {lesson} \nWould you like to use this project? If so, type "Yes": ').lower() == 'yes':
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
                            show_project('Quest for the Country!', 'A text-based, turn-based, comedy RPG about going on a quest to reunite the constitution of the Even More United States of America to save the country. The game contains dozens of lines of comedic dialogue, a unique battle system, 5 bosses, and about 15 minutes of playtime', '_', "Quest for the Country's development taught me how to develop large projects in a timely manner, when to cut content and scope, and what content to cut when necessary.", textadventure_main.main)
                        case '3':
                            show_project('Personal Library', 'A program where you can add to, remove from, and search a library of games sorted by genre, publisher, name, and release year', '_', 'This program taught me who to write search functions, which was extremely important for the Music Fesitival Group Project, and it taught me how to generally manage dictionaries of data.', personallibrary_main.main)
                        case '4':
                            show_project('Video Game Quiz', 'A simple quiz about video game history that adjusts difficulty depending on user answers.', '_', 'This was one of my first projects in this class, and it taught me how to respond to user inputs', quiz_main.main)
                        case '5':
                            show_project('')
                        case '7':
                            break
            case '3':
                print('Leaving Portfolio...')
                break

main()