"""EX06 - Choose Your Own Adventure."""

__author__ = "730433734"


import random

points: int
player: str = ""
SMILE_FACE: str = "\U0001F603"
SEE_YOU: str = "\U0001F44B"
PLUTO_DOG: str = "\U0001F436"


def main() -> None:
    """Main function provides three options for player."""
    global points
    points = 10
    greet()
    endgame: bool = False
    while endgame is False:
        choice = input(f"Hello {player}! You can \"feed\" " + PLUTO_DOG + ", \"play\" with " + PLUTO_DOG + ", or \"quit\" the game. (Please type it correctly): ")
        if choice == "feed":
            feed()
            print(f"Pluto - hunger: {points}")
        elif choice == "play":
            if points < 4:
                print("Pluto is hungry and tired.")
            else:
                points = play(points)
                print(f"Pluto - hunger: {points}")
        elif choice == "quit":
            if again() is True:
                points = 10
                greet()
            else:
                goodbye()
                endgame = True


def greet() -> None:
    """Greet and record the user's name."""
    global player
    print(SMILE_FACE + "Welcome! Have fun with your pet Pluto! ")
    player = input("Please enter your name: ")


def again() -> bool:
    """Ask play if want to play again."""
    while True:
        decision = input("Do you want to play again? Reply \"y\" for YES and \"n\" for NO: ")
        if decision == "y":
            return True
        elif decision == "n":
            return False


def goodbye() -> None:
    """Return a goodbye text when calling upon."""
    print(f"You quit the game, {player}. The hunger of Pluto is {points}. Pluto hopes to see you again." + SEE_YOU)


def play(x: int) -> int:
    """Play with your pet resulting in subduction in hunger."""
    random_number = random.randint(1, 4)
    x -= random_number
    if x < 4:
        print("Pluto is exhausted and need some sleep!")
    elif x >= 4 and x < 8:
        print(f"{player}, Pluto is a little bit tired.")
    elif x >= 8 and x < 12:
        print(f"Great work {player}! Maybe give both of you some time to take a rest.")
    elif x >= 12:
        print("This is the happiest time in Pluto's life!")
    return x


def feed() -> None:
    """Feed your pet with various food."""
    global points
    food: str = ""
    food = input("What food do want feed Pluto: ")
    if points >= 20:
        print(f"Pluto is full after having {food} and cannot eat more!")
    else:
        random_number = random.randint(1, 4)
        points += random_number
        if points >= 13 and points < 17:
            print("Great! Now Pluto is happy.")
        elif points >= 17 and points < 19:
            print(f"Pluto seems full with {food}. If I were you {player}, I would give him a rest.")
        elif points >= 19:
            print("Friendly warning: do feed him anymore.")
        elif points < 13:
            print(f"Well done {player}! Pluto seems very like {food}.")


if __name__ == "__main__":
    main()