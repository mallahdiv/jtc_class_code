#loops inside of loops
days = ['monday', 'tuesday', 'wed', 'thurs', 'friday', 'sat', 'sun']

#logic in loops
for day in days:
	if day.startswith('s'):
		print(f'{day} is a weekend')
	else:
		print(f'{day} is a weekday')
#loops
for day in days:
	print(day)
	for letter in day:
		print(letter)


#nested loops
for outer_var in range(3):
	for inner_var in range(3):
		print(f'outer: {outer_var}, inner: {inner_var}')

#break get you out the loop
for day in days:
	print(day)
	if day.startswith("w"):
		break
print('done with loop')
