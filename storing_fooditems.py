#tinydb file to take in a food item and store it 
from datetime import date
from math import floor
import operator
exec(open('foodItem_class.py').read())

#making a fake food item which will be recieved from UI
fooditem1 = foodItem()
fooditem1.name = 'Yesterday\'s Apple'
fooditem1.foodGrp = 'apple'
fooditem1.setExpiry(2019,12,4)
fooditem1.templateNum = 3


from tinydb import TinyDB, Query

food_db = TinyDB('food_data.json') #making a file which will contain the food info
location_db = TinyDB('location_data.json')

#function to store the info from the foodItem object to a database made above 
def store_in_db(fooditem):
	#converting indate and expiry date to a list of numbers 
	date_inputted = [int(fooditem.inDate.strftime("%Y")),int(fooditem.inDate.strftime("%m")),int(fooditem.inDate.strftime("%d"))]
	date_expiry = [int(fooditem.expDate.strftime("%Y")),int(fooditem.expDate.strftime("%m")),int(fooditem.expDate.strftime("%d"))]

	new_food_id = food_db.insert({'name': fooditem.name,'food_group':fooditem.foodGrp,'image': fooditem.img,'date_inputted':date_inputted,'expiry_date': date_expiry,'template_num':fooditem.templateNum,'location': None})
	return new_food_id
 

#function to reassemble the date from the db to an actual datetime object
def make_date(date_list_from_db):
	#assemble the individual year month and day
	inDate_year = date_list_from_db[0]
	inDate_month = date_list_from_db[1]
	inDate_day = date_list_from_db[2]

	date1 = date(inDate_year,inDate_month,inDate_day) #make into actual date
	return date1


#item_from_db1 = food_db.all()[2] #some item from db to test the next function


#function to reassemble the foodItem object when outputting info to the UI
def make_object_foodItem(item_id_from_db):
	fooditem_object= foodItem() #making it into the foodItem class for the UI
	
	fooditem_object.name = food_db.get(doc_id = item_id_from_db)['name']
	fooditem_object.foodGrp = food_db.get(doc_id = item_id_from_db)['food_group']
	fooditem_object.img = food_db.get(doc_id = item_id_from_db)['image']
	#input date must be resembled
	fooditem_object.inDate = make_date(food_db.get(doc_id = item_id_from_db)['date_inputted'])
	fooditem_object.expDate = make_date(food_db.get(doc_id = item_id_from_db)['expiry_date'])
	fooditem_object.templateNum = food_db.get(doc_id = item_id_from_db)['template_num']

	return fooditem_object #returns reassembled object from db entry 



#need to make location file to manage objects and locations
def make_location(distance):
	location_db.insert({'distance':distance,'item_stored': None})
	return 


#function to find closest available location
def closest_location():
	#first get all locations that are empty
	empty_location = Query()
	empty_loc_list = location_db.search(empty_location.item_stored == None)

	distance_list = [] 
	for location in empty_loc_list:
		distance_list.append(location['distance'])
	
	min_distance = min(distance_list)

	#search location_db for the closest location 
	closest = Query()
	closest_loc = location_db.get(closest.distance == min_distance)
	return  closest_loc.doc_id



#function to move to certain location
def move_to_location(location_id):
	#write function here to output location id to motors
	return 

#questions for mechanical bois:
# how will we differentiate storing item from taking out item from location

#function to sort item to location 
def store_in_location(item_id_from_db):
	#assign closest location to it 
	location_assigned = closest_location()
	food_db.update({'location': location_assigned}, doc_ids=[item_id_from_db])
	location_db.update({'item_stored': item_id_from_db}, doc_ids=[location_assigned])
	move_to_location(location_assigned)
	return location_assigned

#//////***** Grand input function *****//////
#the follow function is the complete inputting an item function that combines
#all the above functions to store the object in the location and db
def complete_input_item(foodItem_object_from_UI):
	new_items_id = store_in_db(foodItem_object_from_UI)
	store_in_location(new_items_id)
	return

#/
#/
#/
#/
#/
#/
#////** OUTPUTTING THE ITEM FROM STORAGE **//////
#give UI a list of avaible items to remove (ignoring repeats)
#tell motors to move to location to output object 
#update food and location database to not contain the item

#function which takes in a list of items from food_db and fines the min value of one catagory 
def find_closest_expiry(list_of_same_template): #catagory_of_item must be an actual catagroy in the item's dictionary ex:'name'
	date_list = []
	for item in list_of_same_template: #extracting date from the items
		date_list.append([make_date(item['expiry_date']),item.doc_id])

	date_list.sort(key=operator.itemgetter(0)) #sorting by date

	return date_list[0][1] #returns the id of the item with closest date 

#this function outputs a list of all food items stored in db for the UI
#to let the user decide which they want to select
#Output is in the format [foodItem object , quantity, item id]
def make_UI_inventory():
	aviable_inventory = []
	checked_templates = []

	for item in food_db: #iterate through all stored items
		if item['template_num']!=None and item['template_num'] not in checked_templates: #if there is a template number, then there is repeats of same item
			template = item['template_num']
			checked_templates.append(item['template_num'])

			repeats = food_db.search(food.template_num == template) #search through all the repeats 
			itemid_w_closest_expiry = find_closest_expiry(repeats) #use function to get only the min expiry date of all the repeats 
			
			aviable_inventory.append([make_object_foodItem(itemid_w_closest_expiry),len(repeats),itemid_w_closest_expiry]) #adding the item id of closest expiry date and it's quantity

		elif item['template_num']==None: #if there is no other item like this, we simply add this item to the inventory
			aviable_inventory.append([make_object_foodItem(item.doc_id),1,item.doc_id])

	return aviable_inventory



#this function tells motors to remove item from certain location
def remove_from_location(item_location_id):
	#send signal to motors to get object from certain location 
	return 

#this function takes in a food item given by UI and removes it from 
#location and food db, as well as telling the motors to remove it
def output_item(item_id_from_UI):
	location_id = food_db.get(doc_id = item_id_from_UI)['location']
	remove_from_location(location_id) #tell motors to remove item 
	location_db.update({'item_stored': None}, doc_ids=[location_id]) #delete item from location
	return

#function to delete item profile after item has been sucessfully removed
def delete_item(location_id):
	item = Query()
	food_db.remove(item.location==location_id)
	return 'item has been deleted'

#///* Grand Removal Function *///
def complete_output_item(item_id_from_UI):
	output_item(item_id_from_UI)
	#wait for confirmation from motors 
	location_id = food_db.get(doc_id = item_id_from_UI)['location']
	delete_item(location_id)
	return 

#/
#/
#/
#///////////**** Multiple item retrival ******////////

#this function will sort the location of items into accending order
def find_closest_location(list_of_item_ids_from_UI): #catagory_of_item must be an actual catagroy in the item's dictionary ex:'name'
	location_list = []
	for item_id in list_of_item_ids_from_UI: #extracting date from the items
		location = food_db.get(doc_id = item_id)['location'] #getting location of stored object 
		location_distance = location_db.get(doc_id = location)['distance']#getting distance of the location of stored object 
		location_list.append([location, location_distance, item_id])

	location_list.sort(key=operator.itemgetter(1)) #sorting by distance

	return location_list #returns the id of the item with closest date 


#this function will take in a list of multple items to be outputted and it will 
#output them in order of shortest distance location to largest
def output_multiple(list_of_item_ids_from_UI):
	location_list = find_closest_location(list_of_item_ids_from_UI)
	for item in location_list:
		print(item[2])
		complete_output_item(item[2])

	return 



#/
#/
#/
#/
#/
#/
#/
#/
#/
#//////////****** Favorite food function ********//////////
#/ this function will store any food items which are frequently used and will tell
#the user when they are running low on this item 

favorites_db = TinyDB('favorites_data.json')

#this function will store the template and time of an inputted item into the 
#favorites database
def store_template(item_id):
	template = food_db.get(doc_id = item_id)['template_num']
	return template



