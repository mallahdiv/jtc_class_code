'''
Planning challenge 2!

For each piece here, write out the pseudocode as comments FIRST, then write your code!
'''


'''
1. Shipping

You are building a system to handle shipping orders. Each order should be a dictionary that has 3 pieces of information:
-destination (string) (for the purposes of this challenge this can be any place, no need to make a full address)
-date_shipped (string)
-weight (float) (how many pounds the package is)

Assign 3 separate orders to 3 separate variables
'''
#creating shipping orders
# Each order has 3 key-value pairs should be a dictionary
#One order per variable 
biden ={'destination': 'NYC',  'date_shipped': '10/29/20', 'weight': 50.12}
#two Variable
trump ={'destination': 'Jail', 'date_shipped':'01/21/21', 'weight': 10}
#three variable
indy = {'destination': ' California', 'date_shipped': '11/03/20', 'weight': 45}


print('\nPART 1')


'''
2. Building the database

Now, let's put the orders all into a database togther (all the orders are storedin 1 variable). 

Your database can either be a dictionary or a list. 

Print out the database to make sure all the info is in there. 

'''
print('\nPART 2')
print('\nPART 2')
biden ={'destination': 'NYC',  'date_shipped': '10/29/20', 'weight': 50.12}
#two Variable
trump ={'destination': 'Jail', 'date_shipped':'01/21/21', 'weight': 10}
#three variable
indy = {'destination': ' California', 'date_shipped': '11/03/20', 'weight': 45}
# create a list to use a database
database = []
# add biden, trump and indy to the database by using append()
database.append(trump)
database.append(biden)
database.append(indy)
# print the database
print(database)
'''
3. Define a function called add_order() that adds one more order to your database, and make sure it works!
Any new orders should be in the same format as your existing ones. 
'''
print('\nPART 3')
# Define a function called add_order
# function takes two parameters - one is database, the other is new order
def add_order(database, new_order):
	# make database take parameters
	# database takes append function
	database.append(new_order)
add_order(database, {'destination': 'MD',  'date_shipped': '10/30/20', 'weight':30.00})
print(database)

'''
4. Define a function called complete_order() to mark a specific order in your database complete

This means that it should add a new key/value pair called 'complete' to a specific order, and set the value to True

Test this out and print out your database to make sure it works!

HINT: Think about how your choice of list/dictionary in part 2 informs how someone would reference an order in the database
'''
print('\nPART 4')
#Create a function called complete_order. The function takes two parameters( datebase, complete order).
# Create a key value pair called complete value is True
# The Function completes order in the list

def complete_order(database, order_index):
	#Point to one specfic index in the database, added a key value pair called complete and set the value to true.
	database[order_index]['complete'] = True
complete_order(database, 2)
complete_order(database, 0)
complete_order(database, 1)
print(database)




