import os
import sys
import time

# Windows 10+ ma ANSI escape codes enable kare che
if os.name == "nt":
    os.system("")

PINK = "\033[38;5;168m"
GOLD = "\033[38;5;179m"
BOLD = "\033[1m"
RESET = "\033[0m"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def type_out(text, color=PINK, speed=0.06):
    sys.stdout.write(f"{BOLD}{color}")
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write(RESET)
    sys.stdout.flush()


LYRICS = [
    "Haaye ve mereya daadeya rabba...",
    "Mere sajna de kol mainu rakhna haaye...",
    "Je tu meri jaan bhi mangg le...",
    "Main taan sajna di bahaan mukna haaye...",
    "Ho ik pal jo tu nazron se gum ho jaye...",
    "Mann soona laage saans bhi tham si jaaye...",
    "Tadpaaye tadpaaye tarsaaye tarsaaye...",
    "Ankhiyon se baadal barsaaye..."
]

def play_song():
    clear()

    print()
    type_out("              \u2661  O SANAM  \u2661", GOLD, 0.1)
    print("\n")

    type_out("          \u266a Play the song please \u266a", PINK, 0.07)
    print("\n")

    input(f"{GOLD}          Press ENTER to play... {RESET}")

    clear()
    print()

    for line in LYRICS:
        type_out("        " + line, PINK, 0.07)
        print("\n")
        time.sleep(2)

    print()


if __name__ == "__main__":
    try:
        play_song()
    except KeyboardInterrupt:
        print(f"{RESET}\n")