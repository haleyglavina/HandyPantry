# //==============================//
# // Haley Glavina - October 2019 //
# // Handy Pantry User Interface  //
# //==============================//

# This program handles UI requests from the HP touch screen. 
from dataclasses import dataclass
from PIL import Image

@dataclass
class foodItem:
	name: str
	foodGrp: int
	inDate: int
	expDate: int 
	img: Image

# Requests from memory module if the pantry is full
def AmIFull():
	return 1

# Input a New Can Item
def InputNew(name, foodGroup, expDate, img):
	# Check if there's room in Pantry
	if (AmIFull()):
		print("Cannot fit a new item in the Handy Pantry")

	# Function contents

	return None