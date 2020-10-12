
print('Question 1')
# You're starting a deli and your supplier currently provides with these ingredients
meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

# You want to create a menu soon, but first things first...
# TODO: Let's capitalize the first letter of each word in each list using .capitalize()
# for food in meats:
# 	print(food.capitalize())
# for c in cheeses:
# 	print(c.capitalize())


print('Question 2')
# Great! Your lists look much better. You need to come up with every combination of meats and cheeses for your menu.
# TODO: Use nested loops to create every combination of meat and cheese and add it to the sandwiches list
sandwiches = []
for m in meats:
	for c in cheeses:
	   sandwiches.append(f'{m} & {c}')
	   print(sandwiches)


print()

print('Question 3')
# TODO: Let's create an input to take a customer order for a sandwich, for example: 'Ham & Swiss'
order = input('what type of Sandwiich?')
# TODO: Loop over the sandwiches list.
# for s in sandwiches:
# 	if order == s:
# 		print(f' Great choice! One {order} coming right up')
# 		break
# else:
# 	print('We donot have that sandwich')
#Paul help me me with this code
#Boolean was added to help check the code
found = False
for s in sandwiches:
	if order == s:
		print(f' Great choice! One {order} coming right up')
		found = True
		break
if found == False:
	print(f'We do not have {order}')


# TODO: If it exists, print 'Great choice! 1 Ham & Swiss coming right up!'
