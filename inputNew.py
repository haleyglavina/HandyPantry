# //==============================//
# // Haley Glavina - October 2019 //
# // Handy Pantry User Interface  //
# //==============================//

# This program is the UI pathway to gain the user information required to insert a new food item into the Handy Pantry

from foodItem_class import *

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
	newFood.expDate.year = int(input())
	print("MM: ")
	newFood.expDate.month = int(input())
	print("DD: ")
	newFood.expDate.day = int(input())



	return newFood