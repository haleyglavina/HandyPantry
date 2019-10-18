# //==============================//
# // Haley Glavina - October 2019 //
# // Handy Pantry User Interface  //
# //==============================//

# This program handles UI requests from the HP touch screen. 

from foodItem_class import *
from inputNew import *
'''
from inputNew import *
from inputPreset import *
from putBack import *
from retrieve import *
'''

#==================================================
# Nonconstants set as constant for testing
# Requests from memory module if the pantry is full
def AmIFull():
	return 0

# Which button on home page is selected
button = 1

#==================================================

def main():
	# Check for user to click on a button
	if button == 1:
		if (AmIFull()):
			print("Your Handy Pantry's storage is full.")
		else:
			InputNew()
			'''
	elif button == 2: 
		InputPreset()
	elif button == 3: 
		PutBack()
	elif button == 4: 
		Retrieve()
		'''
main()

