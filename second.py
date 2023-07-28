import time

def introduction():
    print("Welcome to the Mysterious Island Adventure!")
    print("You find yourself on a deserted island with a mysterious cave to your left and a dense forest to your right.")
    print("Your goal is to survive and explore the island. Good luck!")
    time.sleep(2)
    start()

def start():
    print("\nWhat would you like to do?")
    print("1. Explore the mysterious cave.")
    print("2. Venture into the dense forest.")
    print("3. Check your surroundings.")
    print("4. Quit the game.")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        explore_cave()
    elif choice == "2":
        venture_forest()
    elif choice == "3":
        check_surroundings()
    elif choice == "4":
        quit_game()
    else:
        print("Invalid choice. Try again.")
        start()

def explore_cave():
    print("\nYou enter the dark cave, and as you venture deeper, you see a glimmering light.")
    print("What would you like to do?")
    print("1. Investigate the glimmering light.")
    print("2. Return to where you started.")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        print("\nYou approach the light and discover a hidden treasure chest!")
        print("Congratulations, you've found the treasure! You win!")
        play_again()
    elif choice == "2":
        print("\nYou decide to leave the cave for now.")
        start()
    else:
        print("Invalid choice. Try again.")
        explore_cave()

def venture_forest():
    print("\nYou enter the dense forest, and the trees tower above you.")
    print("What would you like to do?")
    print("1. Search for food.")
    print("2. Set up a shelter for the night.")
    print("3. Return to where you started.")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        print("\nYou manage to find some berries and eat them.")
        print("You feel energized and ready to continue exploring!")
        venture_forest()
    elif choice == "2":
        print("\nYou gather some branches and leaves to create a makeshift shelter.")
        print("The shelter provides you a safe place to rest for the night.")
        time.sleep(2)
        print("The morning comes, and you wake up refreshed!")
        venture_forest()
    elif choice == "3":
        print("\nYou decide to leave the forest for now.")
        start()
    else:
        print("Invalid choice. Try again.")
        venture_forest()

def check_surroundings():
    print("\nYou take a moment to observe your surroundings.")
    print("You notice a stream nearby and some strange markings on the trees.")
    print("What would you like to do?")
    print("1. Follow the stream.")
    print("2. Investigate the strange markings.")
    print("3. Return to where you started.")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        print("\nYou follow the stream, which leads you to a beautiful waterfall!")
        print("The sight is breathtaking, and you feel at peace.")
        check_surroundings()
    elif choice == "2":
        print("\nAs you investigate the markings, you come across a hidden pathway.")
        print("Where could this lead?")
        check_surroundings()
    elif choice == "3":
        print("\nYou decide to stay where you are for now.")
        start()
    else:
        print("Invalid choice. Try again.")
        check_surroundings()

def quit_game():
    print("\nThanks for playing the Mysterious Island Adventure!")
    print("See you next time!")
    time.sleep(2)
    quit()

def play_again():
    choice = input("\nWould you like to play again? (yes/no): ").lower()
    if choice == "yes":
        introduction()
    elif choice == "no":
        quit_game()
    else:
        print("Invalid choice. Try again.")
        play_again()

if __name__ == "__main__":
    introduction()
