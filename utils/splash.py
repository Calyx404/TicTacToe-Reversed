from colorama import init, Fore, Style
from time import sleep

init(autoreset=True)

# Global
term_width = 134
term_middle = lambda : print("\n" * 17)

def clear() -> None:
    from os import system, name
    system('cls' if name == 'nt' else 'clear')

def wait(key:bytes, name:str, action:str, end:str = None) -> None:
    from msvcrt import kbhit, getch

    if end is None:
        print(f"{Style.DIM}{f"PRESS '{name.upper()}' TO {action.upper()}":^{term_width}}")

    else:
        print(f"{Style.DIM}{f"PRESS '{name.upper()}' TO {action.upper()}":^{term_width}}", end="\r", flush=True)

    while True:
        if kbhit():
            if getch() == key:
                break

def typing(text:str) -> None:
    for index in range(1, len(text) + 1):
        print(f"{Style.BRIGHT}{text[:index]:^{term_width}}", end="\r", flush=True)
        sleep(0.1)

    print("\n")

def load(text: str) -> None:
    clear()

    bar_width = 100
    animation_char = '█'
    bar_padding = ' ' * ((term_width - bar_width) // 2)

    term_middle()
    print(Style.BRIGHT + f"{text:^{term_width}}\n")

    for bar in range(bar_width + 1):
        filled = animation_char * bar
        empty = ' ' * (bar_width - bar)
        progress_bar = f"{Fore.GREEN}{filled}{empty}"

        print(f"{bar_padding}{progress_bar}", end="\r", flush=True)
        sleep(0.01)

    sleep(1)
    clear()

def line(fore:str, pattern:str) -> None:
    if fore.upper() == "GREEN":
        print(Fore.GREEN + f"\n{pattern * (term_width // len(pattern)):^{term_width}}\n")
    if fore.upper() == "RED":
        print(Fore.RED + f"\n{pattern * (term_width // len(pattern)):^{term_width}}\n")
    if fore.upper() == "YELLOW":
        print(Fore.YELLOW + f"\n{pattern * (term_width // len(pattern)):^{term_width}}\n")
    if fore.upper() == "WHITE":
        print(Fore.WHITE + f"\n{pattern * (term_width // len(pattern)):^{term_width}}\n")

def ascii(text:str, fore:str) -> None:
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

def start() -> None:
    frames = [
        "Hi",
        "Hello",
        "How are you!",
        "Welcome!"
    ]

    for frame in frames:
        clear()
        term_middle()
        typing(text=frame)
        print()
        wait(key=b' ', name="space", action="continue")

    clear()
    term_middle()
    typing(text="Are you ready?")
    wait(key=b'\r', name="enter", action="start game")

    clear()

def banner() -> None:
    line(fore="white", pattern="-X-O")

    ascii(text="TICTACTOE", fore="CYAN")
    ascii(text="REVERSED🤖", fore="CYAN")

    line(fore="white", pattern="O-X-")
