#!/usr/bin/env python3
from colorama import Fore, Back, Style
import sys
import random
import os

def deleteLineAbove():
  sys.stdout.write("\033[F\033[K")

def getGuess():
  guess = input(f'try {attempt+1}: ')

  while guess not in five_letter_words:
    deleteLineAbove()
    guess = input('guess must be a valid 5 letter word, try again: ')

  deleteLineAbove()
  return guess

def giveHint():
  hint = f'{Back.BLACK}'

  for i in range(5):
    if answer[i] == guess[i]:
      hint += f'{Fore.GREEN}{Style.BRIGHT}{guess[i]}'
    elif guess[i] in answer:
      hint += f'{Fore.YELLOW}{Style.BRIGHT}{guess[i]}'
    else:
      hint += f'{Fore.WHITE}{Style.NORMAL}{guess[i]}'

  hint += Style.RESET_ALL
  print(f'try {attempt+1}: {hint}')

def findFiveLetterWords():
  with open('words.txt') as wordFile:
    all_words = [word[:-1] for word in wordFile.readlines()]
    return [word for word in all_words if len(word) == 5]

def randomFiveLetterWord():
  return random.choice(five_letter_words)

################################################

os.system('clear')
print('\n  Welcome to WORDLE!\n\n')

five_letter_words = findFiveLetterWords()

answer = randomFiveLetterWord()

for attempt in range(6):
  guess = getGuess()
  giveHint()

  if guess == answer:
    print(f'\n  hurray! you got it 😊\n')
    break

if guess != answer:
  print(f'\n  🙁 sorry dude, better luck next time\n')
  if 'y' == input('wanna know the answer? (y/n) '):
    print(f'the answer was {answer}')
