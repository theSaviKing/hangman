from phrases import p as phrases
from random import choice
from dashing import *

class Hangman:
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
  O   |
      |
      |
      |
=========""",
        """  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
        """  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
        """  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
        """  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
        """  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
    ]

    def __init__(self):
        self.value = 0

    def display(self):
        return Hangman.graphics[self.value]
    
    def pdisplay(self):
        print(Hangman.graphics[self.value])
    
    def __str__(self) -> str:
        return Hangman.graphics[self.value]

    def next(self):
        if self.value <= 5:
            self.value += 1
            self.display()


class Phrase:
    bank = phrases
    def __init__(self, category = "random"):
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