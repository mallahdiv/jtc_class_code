#lists inside lists
shopping_list =[['mangos', 'apples', 'organges'], ['carrots', 'brocccoli', 'lettuce'] ['conflakes','oatmeal']]
#access an inner list
print(shopping_list[1])

#one mover level down
#access and item inside an inner list
print(shopping_list[1][0])

shopping_list[1].append('avocados')
shopping_list[1].append('peach')
shopping_list[1].append('kiwi')

#nested loops with nested lists
for food_group in shopping_list:
	print(food_group)

for food_group in shopping_list:
	for food in food_group:
		print(food)
#dictionaries inside lists
user = [{'username': 'ash', 'password': 'ilovepython'},
        {'username': 'paul', 'password': 'ilovegir'},
        {'username': 'aryn', 'password': 'ilovedicitionaries', 'last_login': '9/28'}]

        print(users)

        #print out and item in adictionary in list
        print(users[2]['last_login'])

        #loop through a list of dictionaries, and get the same info form each one
        for user in users:
        	print(user['username'])

	#liar inside dictionaries, 
	cart = {'fruits': ['mangos', 'apples']
			'veggies: ['spinach', 
	}