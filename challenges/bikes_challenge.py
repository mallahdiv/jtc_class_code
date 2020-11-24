# You are starting a bike-sharing service. Your first bike station will be at 14th St and 5 Ave.
# The dictionary below represents your first station.

station = { 
	'name': 'Station A',
 	'address': '14th St and 5 Ave',
 	'bikes': []
}

print('Question 1')

# You don't have any bikes at this station. Create a function 'add' that adds bikes to the bikes list.
# A bike can be represented by an id number in the bikes list
# Parameters: id (int)
# Returns: nothing
def add(bikes):
	station['bikes'] = bikes 

print('')

print('Question 2')
# Create a function 'check_out' to checks out a bike (removes it by id) from the bikes list
# Parameters: id (int)
# Returns: nothing
def check_out(id):
	station['bikes'].remove(id)

print('')

print('Question 3')
# Create a function 'check_in' that returns a bike (adding it by id) to the bikes list.
# Parameters: id (int)
# Returns: nothing
def check_in(id):
	station['bikes'].append(id)
print('')

print('Question 4')
# Congratulations! Your business is expanding. You want to create multiple stations around the city.
# Create a class BikeStation that has the data (name, address, bikes) and all the functions (add, check_out, check_in)
# Parameters to create object: name (string) and address (string)
# Returns: BikeStation Object
class BikeStation():
	def __init__(self, name, address):
		self.name = name
		self.address = address
		self.bikes = []

	def add(self, id):
		self.bikes.append(id)

	def check_out(self, id):
		self.bikes.remove(id)

	def check_in(self, id):
		self.bikes.append(id)

print('')

print('Question 5')
# You will create station objects using BikeStation class and save them to variables.
# 5.1 - First station, name is Station A. Give it an address of your own choosing. 
# 5.2 - Second station, name is Station B. Give it an address of your own choosing.
stationA = BikeStation('Station A', '45 GetBusy Lane')
stationB = BikeStation('Station B', '777 Covid Ave')
print('')

print('Question 6')
# 6.1 - Add bikes 1, 2, 3 to Station A. 
# 6.2 - Add bikes 4, 5, 6 to Station B.
# Print the bikes attributes for both Station A and Station B objects.
stationA.add(1)
stationA.add(2)
stationA.add(3)

stationB.add(4)
stationB.add(5)
stationB.add(6)

print(stationA.bikes)
print(stationB.bikes)

print('')

print('Question 7')
# 7.1 - Check out bike 3 from Station A
# 7.2 - Check out bike 5 from  Station B
# 7.3 - Check in bike 3 to Station B 
# Print the bikes attributes for both Station A and Station B objects.
stationA.check_out(3)
stationB.check_out(5)
stationB.check_in(3)

print(stationA.bikes)
print(stationB.bikes)
