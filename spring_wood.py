def add_player(): #Function used to add players
    name = input("Enter player name: ")
    score = int(input("Enter player score: "))
    player_record = f'{name},{score}\n'
    with open("golf.txt", "a") as file:
        file.write(player_record)
    print("Player information added successfully.")

def display_players(): #function used to display the players
    try:   #Exception Handling
        with open("golf.txt", "r") as file:
            players = file.readlines()
            if not players:
                print("No player information found.")
            else:
                print("Player Information:")
                for player in players:
                    name, score = player.strip().split(",")
                    print(f'Name: {name}, Score: {score}')
    except FileNotFoundError:
        print("players information is not found.")

def main(): #Main function
    while True:
        print("============================================")
        print("** Welcome to SpringWood Golf Club **")
        print("Please choose an option from the following:")
        print("1) Add player name and score")
        print("2) Display all the player information and scores")
        print("3) Quit")
        print("============================================")
        user_choice = input("Enter your choice (1-3): ")

        if user_choice == "1":
            add_player()
        elif user_choice == "2":
            display_players()
        elif user_choice == "3":
            print("**GoodBye.. See you again!** ")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

