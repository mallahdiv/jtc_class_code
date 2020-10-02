# print("Challenge 3.1: Debug code snippets")

# print()

# print("Code Snippet 1:")

# a = 1
# b = 1
# c = (a > b)

# print("The value of c  is false since a is equal to  b.")

# print()

print("Code Snippet 2:")

d = (True or (5 > 7) or not (8 < 20))

print("The value of d is true since the operator is or and the first statement is true")

print()


# print("Code Snippet 3:")

# m = "GOAT"
# n = "goat"

# o = (m == n)

# print ("The value of o is False since Python is case-insensitive.")

# print()

# print("Code Snippet 4:")

# u = 5
# v = 2

# if u * v = 10:
#     print("The product of a and b is 10")
# else:
#     print("The product of a and b is not 10")

# print()

# print("Code Snippet 5:")
# x = 15
# y = 25

# z = 30

# if z < x:
#     print("z is less than x")

# elif z > x and z < y:
#     print("z is between x and y")

# else:
#     print("z is greater than y")


# print()
# print()
# print()

print("Challenge 3.2: Playing with the stock market")

print()

print("Challenge 3.2.1: Creating variables")
# Create variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amzn = 3000
# TODO: Create a variable here for the stock price of
aapl = 100
# TODO: Create a variable here for the stock price o
fb = 250
# TODO: Create a variable here for the stock price of

goog = 1400
# TODO: Create a variable here for the stock price of 
msft = 200
print()


# print("Challenge 3.2.2: Taking user input")
# # TODO: Write code to ask the client his name and save it to a variable.
name = input('Enter your name: ')
# print(name)
# # TODO: Write code to ask the client his savings and save it to another variable.
saving = input('Please enter how much savings you have: ')
# # TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.

stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
amzn_1 = (int(saving)) / amzn
aapl_1 = (int(saving)) / aapl
fb_1 = (int(saving)) / fb
goog_1 = (int(saving)) / goog
msft_1 = (int(saving)) /msft
# print()

# print("Challenge 3.2.3: Perform user-specific calculations")
# # TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

# '''
# Your code should look like this:

if stock == "amzn":  
 	print(f' {name} has ${saving} and can buy {amzn_1} shares of Amazon at the current price of $3000.')
elif stock == "appl":
 	print(f' {name} has ${saving} and can buy {aapl_1} shares of Amazon at the current price of $100.')
elif stock == "fb":
 	print(f' {name} has ${saving} and can buy {fb_1} shares of Amazon at the current price of $250.')
elif stock == "goog":
 	print(f' {name} has ${saving} and can buy {goog_1} shares of Amazon at the current price of $1400.')
elif stock == "msft":
	print(f' {name} has ${saving} and can buy {fb_1} shares of Amazon at the current price of $200.')
else:
	print("Nobody wants to invest")



# print()

# print("Challenge 3.2.4: Output for the user the result")
# # TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# # Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

# print()
