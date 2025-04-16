from os import system
from colorama import init, Fore, Style
from time import sleep

init(autoreset=True)

# Global
term_width = 134
term_padding = 16

def load(text: str) -> None:
    system("cls")

    # Configuration
    bar_width = 100
    animation_char = '█'

    # Pre-calculated positions
    center_padding = ' ' * ((term_width - bar_width - 4) // 2)
    bar_padding = ' ' * ((term_width - bar_width - 4) // 2)

    # Static Layout
    print("\n" * term_padding, end="")
    print(Style.BRIGHT + f"{text:^{term_width}}")
    print(f"{center_padding}  {'-' * bar_width}  ")

    # Animated Loading Bar
    for bar in range(bar_width + 1):
        filled = animation_char * bar
        empty = ' ' * (bar_width - bar)
        progress_bar = f"{Fore.GREEN}{filled}{empty}{Style.RESET_ALL}"
        print(f"{bar_padding}| {progress_bar} |")

        print(f"{center_padding}  {'-' * bar_width}  ")

        print("\033[F\033[F", end='', flush=True)

        sleep(0.01)

    print("\033[E", end='')

    sleep(1)
    system("cls")

def start() -> None:
    from keyboard import wait

    system("cls")

    text = "PRESS 'SPACE' TO START GAME"
    padding_left = (term_width - len(text)) // 2

    print("\n" * term_padding)

    for index in range(1, len(text) + 1):
        print(f"{Style.BRIGHT}{" " * padding_left}{text[:index]}", end="\r", flush=True)
        sleep(0.1)

    wait("space")

    system("cls")

def title() -> None:
    pattern = "-X-0"
    print(f"\n{pattern * (term_width // len(pattern)):^{term_width}}\n")

    ascii_art(text="TICTACTOE", fore="CYAN")
    ascii_art(text="REVERSED🤖", fore="CYAN")

    pattern = "0-X-"
    print(f"\n{pattern * (term_width // len(pattern)):^{term_width}}")

def line(fore:str) -> None:
    if fore.upper() == "GREEN":
        pattern = "X-"
        print(Fore.GREEN + f"\n{pattern * (term_width // len(pattern)):^{term_width}}\n")
    if fore.upper() == "RED":
        pattern = "O-"
        print(Fore.RED + f"\n{pattern * (term_width // len(pattern)):^{term_width}}\n")
    if fore.upper() == "YELLOW":
        pattern = "X-O-"
        print(Fore.YELLOW + f"\n{pattern * (term_width // len(pattern)):^{term_width}}\n")

def ascii_art(text:str, fore:str) -> None:
    letters = {
        "A": [
            " ---------- ",
            "|██████████|",
            "|███|‾‾|███|",
            "|███|__|███|",
            "|██████████|",
            "|███ -- ███|",
            "|███|  |███|",
            " ---    --- ",
        ],
        "B": [
            " ---        ",
            "|███|       ",
            "|███ ------ ",
            "|██████████|",
            "|███|‾‾|███|",
            "|███|__|███|",
            "|██████████|",
            " ---------- ",
        ],
        "C": [
            " ---------- ",
            "|██████████|",
            "|███ ------ ",
            "|███|       ",
            "|███|       ",
            "|███ ------ ",
            "|██████████|",
            " ---------- ",
        ],
        "D": [
            " ---------  ",
            "|█████████| ",
            "|███|‾‾|███|",
            "|███|  |███|",
            "|███|  |███|",
            "|███|__|███|",
            "|█████████| ",
            " --------   ",
        ],
        "E": [
            " ---------- ",
            "|██████████|",
            "|███|‾‾|███|",
            "|██████████|",
            "|███ ------ ",
            "|███|       ",
            "|██████████|",
            " ---------- ",
        ],
        "F": [
            " ---------- ",
            "|██████████|",
            "|███ ------ ",
            "|███|       ",
            "|██████████|",
            "|███ ------ ",
            "|███|       ",
            " ---        ",
        ],
        "G": [
            " ---------- ",
            "|██████████|",
            "|███ ------ ",
            "|███|       ",
            "|██████████|",
            "|███|‾‾|███|",
            "|██████████|",
            " ---------- ",
        ],
        "H": [
            " ---        ",
            "|███|       ",
            "|███ ------ ",
            "|██████████|",
            "|███|  |███|",
            "|███|  |███|",
            "|███|  |███|",
            " ---    --- ",
        ],
        "I": [
            " ---------- ",
            "|██████████|",
            " --- ██ --- ",
            "    |██|    ",
            "    |██|    ",
            " --- ██ --- ",
            "|██████████|",
            " ---------- ",
        ],
        "J": [
            "        --- ",
            "       |███|",
            "       |███|",
            " ---   |███|",
            "|███|  |███|",
            "|███|  |███|",
            "|██████████|",
            " ---------- ",
        ],
        "K": [
            " ---    --- ",
            "|███|  |███|",
            "|███||███| ",
            "|█████|    ",
            "|█████|    ",
            "|███||███| ",
            "|███|  |███|",
            " ---    --- ",
        ],
        "L": [
            " ---        ",
            "|███|       ",
            "|███|       ",
            "|███|       ",
            "|███|       ",
            "|███ ------ ",
            "|██████████|",
            " ---------- ",
        ],
        "M": [
            " ---------- ",
            "|██████████|",
            "|██--██--██|",
            "|██||██||██|",
            "|██||██||██|",
            "|██| -- |██|",
            "|██|    |██|",
            " --      -- ",
        ],
        "N": [
            " ---------- ",
            "|██████████|",
            "|███ -- ███|",
            "|███|  |███|",
            "|███|  |███|",
            "|███|  |███|",
            "|███|  |███|",
            " --      -- ",
        ],
        "O": [
            " ---------- ",
            "|██████████|",
            "|███|‾‾|███|",
            "|███|  |███|",
            "|███|  |███|",
            "|███|__|███|",
            "|██████████|",
            " ---------- ",
        ],
        "P": [
            " ---------- ",
            "|██████████|",
            "|███|‾‾|███|",
            "|███|__|███|",
            "|██████████|",
            "|███ ------ ",
            "|███|       ",
            " ---        ",
        ],
        "Q": [
            " ---------- ",
            "|██████████|",
            "|███|‾‾|███|",
            "|███|__|███|",
            "|██████████|",
            " ------ ███|",
            "       |███|",
            "        --- ",
        ],
        "R": [
            " ---------- ",
            "|██████████|",
            "|███|‾‾|███|",
            "|███|  |███|",
            "|███|   --- ",
            "|███|       ",
            "|███|       ",
            " ---        ",
        ],
        "S": [
            " ---------- ",
            "|██████████|",
            "|███|------ ",
            "|███|______ ",
            "|██████████|",
            " ------|███|",
            "|██████████|",
            " ---------- ",
        ],
        "T": [
            " ---------- ",
            "|██████████|",
            " --- ██ --- ",
            "    |██|    ",
            "    |██|    ",
            "    |██|    ",
            "    |██|    ",
            "     --     ",
        ],
        "U": [
            " ---    --- ",
            "|███|  |███|",
            "|███|  |███|",
            "|███|  |███|",
            "|███|  |███|",
            "|███ -- ███|",
            "|██████████|",
            " ---------- ",
        ],
        "V": [
            " ---    --- ",
            "|███|  |███|",
            "|███|  |███|",
            "|███|  |███|",
            "|███|  |███|",
            " |███--███| ",
            "  |██████|  ",
            "   ------   ",
        ],
        "W": [
            " --      -- ",
            "|██|    |██|",
            "|██| -- |██|",
            "|██||██||██|",
            "|██||██||██|",
            "|██--██--██|",
            "|██████████|",
            " ---------- ",
        ],
        "X": [
            " ---    --- ",
            "|███|  |███|",
            " |███||███| ",
            "    |██|    ",
            "    |██|    ",
            " |███||███| ",
            "|███|  |███|",
            " ---    --- ",
        ],
        "Y": [
            " --      -- ",
            "|███|  |███|",
            "|███ -- ███|",
            "|██████████|",
            " --- ██ --- ",
            "    |██|    ",
            "    |██|    ",
            "     --     ",
        ],
        "Z": [
            " ---------- ",
            "|██████████|",
            " ----- ███| ",
            "    |███|   ",
            "  |███|     ",
            " |███ ----- ",
            "|██████████|",
            " ---------- ",
        ],
        "🤖": [
            " ---------- ",
            "|██████████|",
            "|█|.|██|.|█|",
            "|██████████|",
            "|██████████|",
            "|█||||||||█|",
            "|██████████|",
            " ---------- ",
        ],
    }

    text = text.upper()

    for row in range(8):
        line = ""
        for index, char in enumerate(text):
            if char in letters:
                if index == (len(text) - 1):
                    line += letters[char][row]

                else:
                    line += letters[char][row] + "   "

            else:
                line += " " * 12 + "   "

        if fore.upper() == "BLUE":
            print(Style.BRIGHT + Fore.BLUE + f"{line:^{term_width}}")

        if fore.upper() == "LIGHT BLUE":
            print(Style.BRIGHT + Fore.LIGHTBLUE_EX + f"{line:^{term_width}}")

        if fore.upper() == "CYAN":
            print(Style.BRIGHT + Fore.CYAN + f"{line:^{term_width}}")

        if fore.upper() == "LIGHT CYAN":
            print(Style.BRIGHT + Fore.LIGHTCYAN_EX + f"{line:^{term_width}}")

        if fore.upper() == "GREEN":
            print(Style.BRIGHT + Fore.GREEN + f"{line:^{term_width}}")

        if fore.upper() == "LIGHT GREEN":
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f"{line:^{term_width}}")

        if fore.upper() == "RED":
            print(Style.BRIGHT + Fore.RED + f"{line:^{term_width}}")

        if fore.upper() == "LIGHT RED":
            print(Style.BRIGHT + Fore.LIGHTRED_EX + f"{line:^{term_width}}")

        if fore.upper() == "YELLOW":
            print(Style.BRIGHT + Fore.YELLOW + f"{line:^{term_width}}")

        if fore.upper() == "LIGHT YELLOW":
            print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + f"{line:^{term_width}}")
