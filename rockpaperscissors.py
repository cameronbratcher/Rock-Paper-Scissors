#!/bin/python

#Rock Paper Scissors game
#Cameron Bratcher 2015

#Only tested with python 3.4.3

from random import randint
import sys

def gameStart():
	print("Welcome to Rock, Paper, Scissors!\n")
	print("[1]Rock\n[2]Paper\n[3]Scissors\n")
	
	playerRoll = input("Please choose your roll: ")
	choices = ["1", "2", "3"]
	
	if(playerRoll not in choices):
		print("That's not an option!\n")
		gameStart()
	else:
		gameLogic(playerRoll)
		
def playAgain():
	playAgain = input("\nPlay again? [y/n]: ").upper()
	
	if(playAgain == "Y"):
		gameStart()
	elif(playAgain != "N"):
		print("Invalid input\n")
		playAgain()
	else:
		sys.exit()

def gameLogic(playerRoll):
	compRoll = randint(1,3)
	print("\nComputer rolled: " + str(compRoll) + "\n")
	
	if(int(playerRoll) == int(compRoll)):
		print("Tie")
	elif((int(compRoll) == 1 and int(playerRoll) == 3) or (int(compRoll) == 3 and int(playerRoll) == 2) or (int(compRoll) == 2 and int(playerRoll) == 1)):
		print("Computer Wins")
	else:
		print("Player Wins")
	
	playAgain()
		
gameStart()
