# //==============================//
# // Haley Glavina - October 2019 //
# // Handy Pantry User Interface  //
# //==============================//

# This program is the UI pathway to insert a new item to the Handy Pantry, where its information is gathered from the template of an existing Handy Pantry item.

from foodItem_class import *
from nonvolatile_mem import *

# Input a New Food Item
def InputTemplate():

	# Initialize new food item to be stored
	newFood = foodItem("",0,0,None)

	# Page 2
	# display templates[]
	# Cancel button
	# Scroll button
	# Choose ith template from scoll list
	i = 0

	# Page 3
	# Display selected image
	# OK button
	newFood = template[i]
	newFood.expDate = addDate(newFood.expDate)
	# Cancel button

	# Page 4
	print("\n Plz place item in LOADING DOCK!!!!")

	return newFood


