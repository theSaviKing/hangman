from phrases import p as phrases
from random import choice
from simple_term_menu import TerminalMenu

# from dashing import *
from blessed import Terminal

t = Terminal()


class Hangman:
    width = 9
    graphics = [
        """  +---+
  |   |
      |
      |
      |
      |
=========""",
        """  +---+
  |   |
  #O   |
      |
      |
      |
=========""",
        """  +---+
  |   |
  #O   |
  #|   |
      |
      |
=========""",
        """  +---+
  |   |
  #O   |
 #/#|   |
      |
      |
=========""",
        """  +---+
  |   |
  #O   |
 #/#|#\  |
      |
      |
=========""",
        """  +---+
  |   |
  #O   |
 #/#|#\  |
 #/    |
      |
=========""",
        """  +---+
  |   |
  #O   |
 #/#|#\  |
 #/ #\  |
      |
=========""",
    ]

    def __init__(self):
        self.value = 0

    def display(self):
        output = list(self.graphics[self.value])
        i = 0
        while i < len(output):
            if output[i] == "#":
                output[i + 1] = t.orangered(output[i + 1])
                output.pop(i)
                i -= 1
            else:
                output[i] = t.chartreuse(output[i])
            i += 1
        return "".join(output)

    def pdisplay(self):
        print(self.display())

    def __str__(self) -> str:
        return Hangman.graphics[self.value]

    def next(self):
        if self.value <= 5:
            self.value += 1
            self.display()


class Phrase:
    bank = phrases

    def __init__(self, category="random"):
        if category == "random":
            self.phrase = choice(Phrase.bank[choice(list(Phrase.bank.keys()))])
        elif category not in Phrase.bank:
            print("Not a valid category")
            return None
        else:
            self.phrase = choice(Phrase.bank[category])
        self.tracker = [False for _ in self.phrase]
        self.guesses = []

    def __str__(self) -> str:
        return self.phrase

    def display(self):
        output = ""
        for i in range(len(self.phrase)):
            if self.tracker[i] or self.phrase[i] == " ":
                output += f"{self.phrase[i]} "
            elif self.phrase[i].isalpha():
                output += "_" + " "
        return output.strip()

    def pdisplay(self):
        print(self.display())

    def guess(self, letter: str):
        if len(letter) != 1:
            return False
        if letter.casefold() in self.guesses:
            return False
        if letter.casefold() in self.phrase.casefold():
            for i in range(len(self.phrase)):
                if self.phrase[i].casefold() == letter.casefold():
                    self.tracker[i] = True
            self.guesses.append(letter.casefold())
            return True
        return False

    def width(self) -> int:
        return len(self.display())


class Game:
    title = [
        t.center(" ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄▄▄▄"),
        t.center("█  █  █  ▄  █   █ █  ▂▂▂█     █  ▄  █   █ █ █"),
        t.center("█     █     █ █ █ █  █  █ █ █ █     █ █ █ █▄█"),
        t.center("█▄▄█▄▄█▄▄█▄▄█▄█▄▄▄█▄▄▄▄▄█▄█▄█▄█▄▄█▄▄█▄█▄▄▄█▄█"),
        t.center(""),
    ]

    def tcenter(string: str) -> str:
        # sourcery skip: instance-method-first-arg-name
        strings = string.split("\n")
        for i in range(len(strings)):
            strings[i] = t.center(strings[i])
        return "\n".join(strings)

    def setup(self, category: str = "random"):
        self.hangman = Hangman()
        self.phrase = Phrase(category)

    def display(self):
        pass

    def start(self):
        self.welcome()
        print(self.menu())

    # ----------------------------------------------------------------
    def welcome(self):
        print(t.home + t.clear + t.move_y((t.height // 2) - 4))
        print(t.center(t.khaki1("    WELCOME TO    "), fillchar="+"))
        print(t.black_on_khaki2("\n".join(Game.title)))
        print("")
        print(t.center(t.bold("press any key to continue")))
        with t.cbreak(), t.hidden_cursor():
            inp = t.inkey()

    def menu(self) -> int:
        print(
            "\n"
            + t.center(
                t.bold(f"Choose an option. Use {t.underline_khaki('SPACE')} to toggle.")
            ),
            end="\n\n",
        )

        def print_menu(
            options: list, highlight: int | None = None, success: bool | None = None
        ):
            max_len = max(len(opt) for opt in options)
            space = (t.width - (max_len * len(options))) // (len(options) + 1)
            # print(f"{max_len = }, {space = }")
            for i in range(len(options)):
                if highlight != i:
                    option = options[i].split("] ")
                print(" " * space, end="")
                if highlight == i:
                    if success:
                        print(t.underline_gold(options[i].center(max_len)), end="")
                    else:
                        print(t.bold_gold_reverse(options[i].center(max_len)), end="")
                else:
                    print(
                        f'{t.gold(f"{option[0]}] ")}{t.cornsilk(option[1])}'.center(
                            max_len
                        ),
                        end="",
                    )
            print(" " * space)

        options = [
            "[1] Play Hangman",
            "[2] Customize",
            "[3] Quit",
        ]
        with t.cbreak(), t.hidden_cursor():
            print_menu(options)
            inp = t.inkey()
            i = 0
            keys = ["KEY_ENTER", *[str(i) for i in range(len(options))]]

            while inp.name not in keys and inp not in keys:
                print(t.move_up(2))
                print_menu(options, highlight=i)
                inp = t.inkey()
                if inp.name == "KEY_ENTER":
                    print(t.move_up(2))
                    print_menu(options, highlight=i, success=True)
                    return i
                elif inp in [str(i) for i in range(len(options))]:
                    print(t.move_up(2))
                    print_menu(options, highlight=i, success=True)
                    return int(inp)
                elif inp == " ":
                    i ^= 1


def main():
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
