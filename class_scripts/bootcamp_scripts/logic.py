# math comparisons
# print(1 > 0 )

a = 0
b = 1
c = 1

print(f" is a equal to b?: {a==b}")
print(f" is a not equal to b?: {a != b}")
print(f"is a greater than b?: {a > b}")
print(f'is a lesser than b?: {a < b}')
print(f"is b greater than or equal to c?: {b >= c}")
print(f" is b less than or equal to c?: {b <=c}")

#integer vs floats
# print(3 == 3.000)

# #booleans
# print(True == 1)
# print(True == 0)
# print(True > 0)
# print(False == 0)

#strings
#print(True == 'True')

# a = 'cat'
# b = 'cat'
# c = 'CAT'

# print( a == b)
# print(a != c)
# print( 'cat' > 'bat')
# print('cat' > 'dog')

#compounding loagic (or, and & not)
# print(2  < 3 or 4 < 3)
# print(2 > 3 or 4 > 3)
# print(2 > 3 or 4 < 3)
# print(2 < 3 or 4 > 3)

#and
# print(2  < 3 and 4 < 3)
# print(2 > 3 and 4 > 3)
# print(2 > 3 and 4 < 3)
# print(2 < 3 and 4 > 3)

#not: flips to to other boolean
# print(not 2 > 3)
# print(not False)
# print(not True)

# a = 1
# b = 2
# print(a < 10 and a >b)
# print(a < 10 and not a > b)

#Conditionals
# a = 5
# if a > 3:
# 	#if condition is true, run below code
# 	print('greater than B!')
	
# if a == 3:
# 	#if condition is true, run below code
# 	print(f'{a} greater than B!')
# else:
# 	print(f'{a}not equals 3!')

# a = 2

# if a < 0:
# 	print('a is a negative number')
# elif a > 0:
# 	print('a positive number ')
# else:
# 	print('this will probably never run')


# season = 'fall'
# if season == 'spring':
# 	print('getting warmer')
# elif season == 'winter':
# 	print('cold out')
# elif season == 'summer':
# 	print('hot out')
# else:
# 	print('i dont care what the weather is')
# 	
# multiple ifs
# a = 2
# b = 30

# if a > 10:
# 	print('agreater than 10')
# if b > 10:
# 	print('b greater than 10')

# a = 10
# if a > 0:

answer = input('Do you want to hear a joke? press y /n')
if answer == "y":
	print("I'm against pciketing, but I don't know how to show it.")
elif answer == "n":
	print("fine.")
else:
	print("I don't understand")