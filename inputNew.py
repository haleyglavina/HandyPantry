# //==============================//
# // Haley Glavina - October 2019 //
# // Handy Pantry User Interface  //
# //==============================//

# This program is the UI pathway to gain the user information required to insert a new food item into the Handy Pantry

from foodItem_class import *
from nonvolatile_mem import *

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
	yr = int(input())
	print("MM: ")
	mth = int(input())
	print("DD: ")
	dy = int(input())
	newFood.expDate = date(year = yr, month = mth, day = dy)


	# Page 5
	print("\n Plz place item in LOADING DOCK!!!!")

	# Page 6
	# newFood.img = RPi_Camera_Input

	# Page 7
	print("\n Save as preset template? Y/N : ")
	ans = input()
	if (ans == 'Y'):
		newTemplate = newFood
		# Food item templates 
		newTemplate.newFood = timeTilExpiry(newFood)
		templates.append(newTemplate)

	#UI doesn't do anything with returned item but memory module will
	return newFood












