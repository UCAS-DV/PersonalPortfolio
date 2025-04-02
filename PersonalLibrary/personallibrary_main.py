# Darius Vaiaoga - P2 - Personal Library Program
# 
library = []

genres = (
    "FPS",
    "Puzzle",
    "RPG",
    "Platformer",
    "Tower Defense",
    "Action-Adventure",
    "Co-op",
    "Fighting",
    "Party",
    "Survival",
    "Sandbox"
    "Action-Adventure",
    "Fighting",
    "FPS",
    "Horror",
    "Party", 
    "Platformer",
    "Puzzle",
    "Roguelike",
    "RPG",
    "RTS",
    "Sandbox",
    "Simulator",
    "Survival",
)

# Prints out library
def showLibrary(complex):
    num = 1
    print("Your Library:")
    for game in library:

        # If the output is supposed to complex, print all details, if not, print only the name and developer
        if complex:
            print(f'{num}. {game["name"]} - {game["genre"]} - {game["developer"]} - {game['release year']}')

        else:
            print(f'{num}. {game['name']} - {game['developer']}')
        num += 1


# Asks for name, genre, and developer of game to add it to library
def createEntry():
    name = input("What is the name of your game? ")
    
    # Prints all possible genres and then asks user what genre they'd like
    num = 1
    for possible_genre in genres:
        print(f"{num}. {possible_genre}")
        num += 1

    try:
        genre = genres[int(input("Which genre is your game? (Input Number) ")) - 1]
    except:
        input("Invalid Input")
        return None

    developer = input("What studio or person developed or published the game? ")

    try:
        release_year = int(input("What was the year of the game's release? "))
    except:
        input('Invalid Input')
        return None

    library.append({"name": name, "genre": genre, "developer": developer, 'release year': release_year})

# Shows the game library, asks user what to remove, and then loops through the library to find and remove that game.
def removeEntry():
    showLibrary(True)
    game_to_remove = input("Which game do you want to remove? ")
    
    for game in library:
        if game['name'].lower() == game_to_remove.lower():
            library.remove(game)
            print(f"{game['name']} has been removed from your library.")
            break
    else:
        print(f'Could not find "{game_to_remove}" in your library. Please verify if you spelt the name correctly.')

def modifyEntry():
    showLibrary(True)
    game_to_modify = input('Which game do you want to modify? ')

    for game in library:

        if game['name'].lower() == game_to_modify.lower():
            
            match input('What detail do you want to change? \n1. Name \n2. Genre \n3. Developer \n4. Release Year \n'):
                # Modify Name
                case '1':
                    game['name'] = input('What is the changed name of the game? ')
                
                # Modify Genre
                case '2':
                    # Prints all possible genres and then asks user what genre they'd like, like in createEntry()
                    num = 1
                    for possible_genre in genres:
                        print(f"{num}. {possible_genre}")
                        num += 1

                    try:
                        game['genre'] = genres[int(input("Which genre is your game? (Input Number) ")) - 1]
                    except:
                        input("Invalid Input")
                        return None

                # Modify Developer
                case '3':
                    game['developer'] = input("What is the changed developer of the game? ")

                # Modify Release Year
                case '4':
                    try:
                        game['release year'] = int(input("What was the year of the game's release? "))
                    except:
                        input('Invalid Input')
                        return None
            break
    else:
        print(f'Could not find "{game_to_modify}" in your library. Please verify if you spelt the name correctly.')

# Finds and prints games based off of a criteria and a search query
def search(criteria=''):
    query = input(f"Enter Game {criteria.capitalize()}: ")
    num = 1

    for game in library:
        
        if criteria != 'release year':

            # If the first two letters of the query match the first two letters of the criteria, print the game info.
            if [game[criteria][0], game[criteria][1]] == [query[0], query[1]]:
                print(f'{num}. {game["name"]} - {game["genre"]} - {game["developer"]} - {game['release year']}')
                num += 1

        else:
            # If the search criteria is the release year, find games of same release year
            try:

                if game[criteria] == int(query):
                    print(f'{num}. {game["name"]} - {game["genre"]} - {game["developer"]} - {game['release year']}')
                    num += 1
                    
            except:
                input('Invalid Input')

# Main Function for handling UI
def main():
    username = input("Welcome to your personal game library. Enter a username: ")
    while True:
        print(f"{username}'s Library")

        # Asks user to input what they want to do
        match input("What would you like to do? \n1. Go to Library \n2. Add to Library \n3. Remove from Library \n4. Modify Game \n5. Search in Library \n6. Exit \n"):

            # Show Library
            case "1":
                complexity = input('Do you want to see ALL details or do you want the simple view? \n1. Simple View \n2. All Details \n')

                # Simple View
                if complexity == '1':
                    showLibrary(False)

                # All Details
                elif complexity == '2':
                    showLibrary(True)

                else:
                    input('Invalid Input')

            # Create Entry
            case "2":
                createEntry()

            # Remove Entry
            case "3":
                removeEntry()
            
            # Modify Entry
            case '4':
                modifyEntry()

            # Search
            case "5":
                # Asks user to input what they want to search by, and then invokes search to actually search for it
                match input("Search By: \n1. Title \n2. Genre \n3. Developer \n4. Release Year \nWhat do you want to search by? (Input Number) "):
                    case "1":
                        search("name")
                    case "2":
                        search("genre")
                    case "3":
                        search("developer")
                    case '4':
                        search('release year')
                    case _:
                        input("Invalid Input")

            # Exists Program
            case "6":
                break

        input("Press Enter to continue.")