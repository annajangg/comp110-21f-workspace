"""Phantom Tollbooth."""
# All story inspriation and lines come from the book "Phantom Tollbooth" by Norton Juster.

__author__ = "730411065"


points: int = 0
player: str = ""
NAMED_CONSTANT: str = "\U0001F389"


def main() -> None:
    """The story game."""
    global points
    greet()
    while int(input(f"Do you want to continue: 1 for Yes, 2 for No? You have {points} coins right now. ")) == 1:
        print("Now you have three choices:")
        print("1: You can follow through with the instructions, pick a destination, and go through the tollbooth.")
        print("2: You can go through the tollbooth with no destination in mind.")
        print("3: You can put everything in the box again, put it on your porch for your mailman, because this package is not for you.")
        choice: int = int(input("Choose 1, 2, or 3. What do you choose? "))
        if choice == 1:
            adventure()
        else:
            if choice == 2:
                wasteland(points)
            else:
                if choice == 3:
                    boring()
    print("...")
    print(f"Game Over. {NAMED_CONSTANT}{NAMED_CONSTANT}{NAMED_CONSTANT}")
    print(f"Total Coins: {points}")
    print


def greet() -> None:
    """Welcome message and context."""
    global points
    global player
    print("Welcome to the Phantom Tollbooth!")
    print("If you pass through the tollbooth, you will enter the Lands Beyond.")
    player = str(input("What is your name? "))
    print("...")
    print("One monotonous day as you are walking home from school, you remark \"Almost everything is a waste of time. And worst of all, there's nothing for me to do, nowhere I'd care to go, and hardly anything worth seeing.\"")
    print("...")
    print("When you arrive to your room, you see a huge package with a bright-blue envelope which said simply:")
    print(f"FOR {player}, WHO HAS PLENTY OF TIME.")
    print("THIS PACKAGE CONTAINS THE FOLLOWING ITEMS:")
    print("- One map, up to date and carefully drawn by master cartographers.")
    print("- Five coins for use in paying tolls.")
    points = points + 5
    print(f"[Now you have {points} coins.]")
    print("...")
    print("In the big box, there is a tollbooth and a car. You set up the tollbooth. There is a sign on it saying:")
    print("SLOW DOWN APPROACHING TOLLBOOTH.")
    print("HAVE YOUR DESTINATION IN MIND.")
    print("...")


def adventure() -> None:
    """Adventure to the Kingdom of Wisdom."""
    global points
    points = points + 1
    free: int
    print("...")
    print("You choose the biggest dot on the map as your destination. The dot is the location for Kingdom of Wisdom.")
    print("You hop in the car and drive slowly up to the tollbooth. You deposit your coin.")
    points = points - 1
    print(f"[Now you have {points} coins.]")
    print("...")
    print("Suddenly you find yourself speeding along an unfamiliar country highway, with neither the tollbooth nor your room nor even your house anywhere in sight.")
    print("There is a crossroads in the highway, but you follow the map that says the way to the Kingdom of Wisdom is on the right road.")
    print("The Kingdom of Wisdom has two cities: Dictionopolis and Digitopolis. Dictionopolis has the marketplace for words. Digitopolis has the mine for numbers.")
    print("You have arrived during the three-day celebration honoring the reconciliation of the two cities.")
    print("They are giving out free money that you recognize are also used as coins for your tollbooth.")
    print("You run into Tock, whose friend Milo has returned back to his room.")
    print("Tock asks you your name and offers:")
    print(f"I NO LONGER HAVE A NEED FOR THESE COINS MILO GAVE ME. {player}, DO YOU WANT THEM")
    given: int = int(input("Press 1 for yes, press 2 for no. "))
    print("...")
    if given == 1:
        import random
        free = int(random.randint(1, 10))
        points = points + free
        print(f"[Now you have {points} coins.]")
        print("...")
    else:
        print("Tock: THEN I WILL USE THEM AS A KEEPSAKE OF MY DEAR FRIEND MILO.")
    print("You look at the time and oh! How time flies! You start heading back to the direction of your tollbooth.")
    print("Suddenly you find yourself in your own room. You are much too tired to talk and almost too tired for dinner, so you go off to bed as soon as you can.")
    print("You pull the covers around you and take a last look at your room -- which somehow seemed very different than you remembered -- and then drift into a deep and welcome sleep.")
    print("...")


def wasteland(c: int) -> int:
    """Adventure to the Doldrums."""
    global points
    print("...")
    print("You hop in the car and drive slowly up to the tollbooth. You deposit your coin and...")
    points = points - 1
    print(f"[Now you have {points} coins.]")
    print("...")
    print("Suddenly you find yourself speeding along an unfamiliar country highway, with neither the tollbooth nor your room nor even your house anywhere in sight.")
    print("The road before you splits into two roads.")
    print("You decide to go on the left road. Things begin to change as soon as you leave the main highway. The sky becomes quite gray and, along with it, the whole countryside seems to lose its color.")
    print("Mile after")
    print("mile after")
    print("mile after")
    print("mile you drive as the car went slower and slower, until it was hardly moving at all.")
    print("...")
    print("You say \"I WONDER WHERE I AM.\" in a very worried tone.")
    print("\"YOU'RE...IN...THE... DOL...DRUMS...,\" wails a voice.")
    print("\"WHAT ARE THE DOLDRUMS?\" you ask.")
    print("\"THE DOLDRUMS, MY FRIEND, ARE WHERE NOTHING EVER HAPPENS AND NOTHING EVER CHANGES.\" says the voice, and you look to see a colorless creature sitting on your shoulder.")
    print("The Lethargarian continues, \"NO ONE'S ALLOWED TO THINK IN THE DOLDRUMS. ACCORDING TO ORDINANCE 574381-W, 'IN THE DOLDRUMS, LAUGHTER IS FROWNED UPON AND SMILING IS PERMITTED ONLY ON ALTERNATE THURSDAYS.\"")
    print("\"WELL, IF YOU CAN'T LAUGH OR THINK, WHAT CAN YOU DO?\" you ask while yawning.")
    print("\"ANYTHING AS LONG AS IT'S NOTHING, AND EVERYTHING AS LONG AS IT'S NOT ANYTHING,\" explained a Lethargarian.")
    print("\"EVERYBODY DOES NOTHING BUT THE WATCHDOG. HE'S ALWAYS SNIFFING AROUND TO SEE THAT NOBODY WASTES TIME.\"")
    print("And at that moment came racing down the road barking furiously and kicking up a great cloud of dust was the very dog of whom they had been speaking.")
    print("...")
    print("\"WHAT ARE YOU DOING HERE?\" growls the watchdog.")
    print("How will you answer?")
    print("Press 1 for \"JUST KILLING TIME.\"")
    print("Press 2 for \"I GOT LOST. CAN YOU HELP ME?\"")
    question: int = int(input("Which answer do you choose? "))
    if question == 1:
        print("\"JUST KILLING TIME\" you reply.")
        print(f"\"KILLING TIME!!!\" roared the dog. \"DUE TO THAT REASON, YOU, {player}, ARE TO BE FINED 3 COINS.")
        points = points - 3
        print(f"[Now you have {points} coins.")
    else:
        print("\"HELP YOU! YOU MUST HELP YOURSELF.\" the dog replies.")
    print("\"NOW GO HOME.\" advises the watchdog.")
    print("...")
    print("You start heading back to the direction of your tollbooth.")
    print("Suddenly you find yourself in your own room. You are much too tired to talk and almost too tired for dinner, so you go off to bed as soon as you can.")
    print("You pull the covers around you and take a last look at your room -- which somehow seemed very different than you remembered -- and then drift into a deep and welcome sleep.")
    print("...")
    return points


def boring() -> None:
    """No Adventure."""
    print("...")
    global points
    print("You pack the package back up. You lug the box to your front door. You leave a note for the mailman that reads:")
    points = 0
    print("NOT MINE.")
    print("You go back to your room and do your homework and get ready for another monotonous day.")
    print("...")


if __name__ == "__main__":
    main()