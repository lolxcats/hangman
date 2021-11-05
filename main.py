import random
import time
from graphics import hangmanname, HANGMANPICS
from wordlist import *



def startGame():
    print(f"{hangmanname}\n\nWelcome to Hang Man")

def ChooseDif():
    validAnswers = ["1",'2','3']
    ans = input("Please select the Difficulty\n1: Easy\n2: Medium\n3: Hard\n\n")
    while True:
        if ans in validAnswers:
            break
        else:
            ans = input('Please enter a valid input\n')
    if ans == "1":
        gameword = random.choice(easywords)
    if ans == "2":
        gameword = random.choice(medwords)
    if ans == "3":
        gameword = random.choice(hardwords)
    return gameword

def checkguess(guess,word,progress):
    for i in range(len(word)):
        if guess == word[i]:
            progress[i] = word[i]
    return progress

def hangmangame(gameword):
    life = 0
    wincon = False
    finalword = [char for char in gameword]
    progress = ["_"] * len(finalword)
    while life < 6 and wincon == False:
        if progress == finalword:
            wincon == True
        print(f"{HANGMANPICS[life]}\n{progress}\n")
        guess = input('Please enter a guess\n')
        if guess in finalword:
            progress = checkguess(guess,finalword,progress)
        else:
            life +=1
            print('Try again')
    if wincon == True:
        print('Congratz you win!')
    if life == 6:
        print(f"{HANGMANPICS[6]}\n YOU LOSE\nThe word was: {finalword}")

def main():
    while True:
        startGame()
        time.sleep(4)
        hangmangame(ChooseDif())
        userAns = input('Play again?  y/n\n')
        if userAns == 'y':
            continue
        else:
            break
main()

input('Press ENTER to exit')