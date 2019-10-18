# //==============================//
# // Haley Glavina - October 2019 //
# // Handy Pantry User Interface  //
# //==============================//

# This program defines all the functions and classes to be referenced amongst Handy Pantry UI files.


from datetime import date
from PIL import Image

class foodItem():
	def __init__(self, name, foodGrp, expDate, img):
		self.inDate = date.today()
		self.expDate = (0, 0, 0)
		self.prevCopy = None

	# Returns index of previous copy for an item inputted by template
	def previousCopy(fooditem):
		return fooditem.prevCopy

	# Determines how long an item has until expiry
	def timeTilExpiry(fooditem):
		timeRemaining = (0,0,0)
		today = date.today()
		timeRemaining[0] = today.year - fooditem.expDate[0]
		timeRemaining[1] = today.month - fooditem.expDate[1]
		timeRemaining[2] = today.day - fooditem.expDate[2]
		return timeRemaining

	# Determines if an item is past its expiry
	def pastExpiry(fooditem):
		if timeTilExpiry[0] < 1
			return True
		return False

# Input a New Food Item
def InputNew():

	# Initialize new food item
	newFood = foodItem("",0,0,None)
	#newFood = foodItem()

	# Page 2
	print("\n Enter food name: ")
	newFood.name = input()
	print(newFood.name)
	
	# Page 3
	print("\n Select food group:")
	print("Type 1 for Fruit/veg/bean")
	print("Type 2 for Soups & sauces")
	print("Type 3 for Custom containers")
	print("Type 4 for Other")
	newFood.foodGrp = int(input())

	print("\n Food group chosen: ")
	if newFood.foodGrp == 1: 
		print("Fruit/veg/bean")
	elif newFood.foodGrp == 2: 
		print("Soups & sauces")
	elif newFood.foodGrp == 3: 
		print("Custom containers")
	elif newFood.foodGrp == 4: 
		print("Other")

	# Page 4
	print("\n Enter expiry date: ")
	print("YYYY: ")
	newFood.expDate[0] = int(input())
	print("MM: ")
	newFood.expDate[1] = int(input())
	print("DD: ")
	newFood.expDate[2] = int(input())



	return newFood


