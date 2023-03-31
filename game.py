import phrases
from random import choice

class Hangman:
  graphics = [
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
  ]
  def __init__(self):
    self.value = 0
  def display(self):
    print(Hangman.graphics[self.value])
  def next(self):
    if self.value <= 5:
      self.value += 1
      self.display()

class Phrase:
  bank = phrases.p
  def __init__(self, category):
    if category not in Phrase.bank:
      print("Not a valid category")
      return None
    else:
      self.phrase = choice(Phrase.bank[category])