"""EX06 - Choose Your Own Adventure."""

__author__ = "730433734"


import random

hunger: int = 0
player: str = ""
SMILE_FACE: str = "\U0001F603"
SEE_YOU: str = "\U0001F44B"
PLUTO_DOG: str = "\U0001F436"


def main() -> None:
    global hunger
    hunger = 10
    greet()
    endgame: bool = False
    while endgame is False:
        choice = input(f"Hello {player}! You can \"feed\" " + PLUTO_DOG + ", \"play\" with " + PLUTO_DOG + ", or \"quit\" the game. (Please type it correctly): ")
        if choice == "feed":
            feed()
            print(f"Pluto - hunger: {hunger}")
        elif choice == "play":
            if hunger < 4:
                print("Pluto is hungry and tired.")
            else:
                print(f"Pluto - hunger: {play()}")
        elif choice == "quit":
            goodbye()
            endgame = True

def greet() -> None:
    global player
    print(SMILE_FACE + "Welcome! Have fun with your pet Pluto! ")
    player = input("Please enter your name: ")


def goodbye() -> None:
    print(f"You quit the game, {player}. The hunger of Pluto is {hunger}. Pluto hopes to see you again." + SEE_YOU)


def play() -> int:
    global hunger
    random_number = random.randint(1, 4)
    hunger -= random_number
    if hunger < 4:
        print("Pluto is exhausted and need some sleep!")
    elif hunger >= 4 and hunger < 8:
        print(f"{player}, Pluto is a little bit tired.")
    elif hunger >= 8 and hunger < 12:
        print(f"Great work {player}! Maybe give both of you some time to take a rest.")
    elif hunger >= 12:
        print("This is the happiest time in Pluto's life!")
    return hunger

def feed() -> None:
    global hunger
    if hunger > 20:
        print("Pluto is full now and cannot eat more!")
    else:
        random_number = random.randint(1, 4)
        hunger += random_number
        if hunger >= 13 and hunger < 17:
            print("Great! Now Pluto is happy.")
        elif hunger >= 17 and hunger < 19:
            print(f"Pluto seems full. If I were you {player}, I would give him a rest.")
        elif hunger >= 19:
            print("Friendly warning: do feed him anymore.")
        elif hunger < 13:
            print(f"Well done {player}! Pluto seems very like you.")


if __name__ == "__main__":
    main()