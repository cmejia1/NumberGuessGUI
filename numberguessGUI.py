"""
program: numberguessGUI.py
author: chris 7/13/2023

GUI based version of the number guessing game

NOTE: the file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!
"""

from breezypythongui import EasyFrame
import random
# other imports go here

# class header 
class GuessingGame(EasyFrame):
	# definition of our class constructor method
	def __init__(self):
		EasyFrame.__init__(self, title = "Guessing Game", width = 240, height = 180)

		#initialize the instance variables for the class
		self.magicNumber = random.randint(1, 10)
		self.count = 0 

		#create and widgets to the window
		self.hintLabel = self.addLabel(text = "Guess a number between 1 and 100", row = 0, column = 0, columnspan = 2, sticky = "NSEW")
		self.addLabel(text = "Your guess:", row = 1, column = 0)
		self.guessField = self.addIntegerField(value = 0, row = 1, column = 1)
		self.nextButton = self.addButton(text = "Next", row = 2, column = 0, command = self.nextGuess)
		self.newButton = self.addButton(text = "new Game", row = 2, column = 1, command = self.newGame)

	# definition of the nextGuess() function
	def nextGuess(self):
		self.count += 1
		guess = self.guessField.getNumber()
		# logic that determines the games outcome
		if guess == self.magicNumber:
			self.hintLabel["text"] = "You've guessed it in " + str(self.count) + " attempts!" 
			self.nextButton["state"] = "disabled"
		elif guess < self.magicNumber:
			self.hintLabel["text"] = "Sorry, your guess was too small!"
		else:
			self.hintLabel["text"] = "Sorry, your guess was too large!"

	# definition of the newGame() function
	def newGame(self):
		"""resets the data and GuI to their original states"""
		self.magicNumber = random.randint(1, 10)
		self.count = 0 
		self.hintLabel["text"] = "Guess a Number between 1 and 100"
		self.guessField.setNumber(0)
		self.nextButton["state"] = "normal"

# definition of the main() method
def main():
	GuessingGame().mainloop()

# global call to main() for program entry
if __name__ == '__main__':
	main()