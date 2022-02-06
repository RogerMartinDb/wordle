#!/usr/bin/env python3
from colorama import Fore
from colorama import Style
import sys
import random

def deleteLineAbove():
  sys.stdout.write("\033[F\033[K")

def getGuess():
  guess = input(f'try {attempt+1}: ')

  while not guess in five_letter_words:
    deleteLineAbove()
    guess = input('guess must be a valid 5 letter word, try again: ')

  deleteLineAbove()
  return guess

def giveHint():
  hint = ''

  for i in range(5):
    if answer[i] == guess[i]:
      hint += f'{Fore.GREEN}{Style.NORMAL}{guess[i]}'
    elif guess[i] in answer:
      hint += f'{Fore.YELLOW}{Style.NORMAL}{guess[i]}'
    else:
      hint += f'{Fore.RESET}{Style.DIM}{guess[i]}'

  hint += Style.RESET_ALL
  print(f'try {attempt+1}: {hint}')

def findFiveLetterWords():
  with open('words.txt') as wordFile:
    all_words = map(lambda word: word[:-1], wordFile.readlines())
    return list(filter(lambda work: len(work) == 5, all_words))

def randomFiveLetterWord():
  index = random.randrange(len(five_letter_words))
  return five_letter_words[index]



################################################

five_letter_words = findFiveLetterWords()

answer = randomFiveLetterWord()

for attempt in range(6):
  guess = getGuess()
  giveHint()

  if guess == answer:
    print('\n  hurray! you got it :)\n')
    break

if guess != answer:
  print('\n  sorry dude, better luck next time\n')
  if 'y' == input('wanna know the answer? (y/n) '):
    print(f'the answer was {answer}')
