from phrases import p as phrases
from random import choice

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
    def __init__(self):
        self.hangman = Hangman()

    def setPhrase(self, category="random"):
        self.phrase = Phrase(category)

    def display(self):
        pass

    def start(self):
        self.welcome()

    def welcome(self):
        print(t.home + t.clear + t.move_y((t.height // 2) - 2))
        print(t.center(t.khaki1("    WELCOME TO    "), fillchar="+"))
        print(t.black_on_khaki2(t.center("HANGMAN!")))
        print("")
        print(t.center(t.bold("press any key to continue")))
        with t.cbreak(), t.hidden_cursor():
            inp = t.inkey()


def main():
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
