"""
Task: create a computer program which stores information about computer games home library
Additional: keep track of all the actions
            allow user to enter ratings for games

Commands available:
  - add    -> add a game
  - remove -> remove a game
  - list   -> list all games with ratings and counts
  - find   -> check if a game is present
  # - mark which games your friends have (dates)
  # - display the last <N> added games
  # - change rating of a game
  - quit   -> exit the program
"""

COMMANDS_LIST_MSG = """Available commands: 
 - add: add a game
 - remove: remove a game
 - list: lists all available games with ratings and counts
 - find: search for a specific game
 - quit: exit the program"""
"""
library = {
    "Pacman": {
        "rating": 4.5,
        "count": 1,
    },
    "Snake": {
        "rating": 4.3,
        "count": 2,
    }
}
"""


library = {}
history = []

while True:
    print(COMMANDS_LIST_MSG)
    print(library)
    action = input("Select a command: ")

    if action == "quit":
        print("Exiting the program...")
        break

    elif action == "add":
        # print("Adding a game...")
        title = input("Enter the title: ")
        rating = float(input("Enter the rating: "))

        # If title is not in the library, create a placeholder for it
        if title not in library:
            library[title] = {"rating": 0.0, "count": 0}

        # Increment count
        library[title]["count"] += 1
        # Overwrite rating
        library[title]["rating"] = rating

        history.append(f"Added '{title}' to the library with rating '{rating}'.")

    elif action == "remove":
        # print("Removing a game...")
        title = input("Enter the title: ")

        # Check if the game is in the library
        if (title not in library) or (library[title]["count"] < 1):
            print(f"[!] '{title}': not enough copies in the library to remove")
            continue

        library[title]["count"] -= 1

    elif action == "list":
        # print("Listing all games...")
        # for key, value in dictionary.items():
        print(f"title      | cnt | rating")
        print("-------------------------")
        for game_title, game_stats in library.items():
            print(f"{game_title:10.10s} | {game_stats['count']} | {game_stats['rating']}")

    elif action == "find":
        # print("Searching for a game...")
        title = input("Enter the title: ")

        if title not in library:
            print(f"{title} | not found.")
        else:
            count = library[title]["count"]
            rating = library[title]["rating"]
            print(f"Title: {title}")
            print(f"  Count:  {count}")
            print(f"  Rating: {rating}")

    else:
        print(f"Command not supported: '{action}'. Please select another one.")
