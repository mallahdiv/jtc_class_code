'''
GOOGLING CHALLENGE! 

Today, we'll ask you to write a bunch of small pieces of code.

Unlike previous ones, we have NOT showed you the exact code you'll need to answer the questions.

So, you'll want to search out answers on the web, make sure you understand them, then try them out until they work!

For each question, you should also COPY THE LINK TO THE RESOURCE WHERE YOU FOUND THE SOLUTION in so that you can use it in the future too
'''


# 1A. Sort the below list in alphabetical order
print('QUESTION 1\n')
my_friends = ['Yusuf', 'Aedan', 'Mia', 'Ash', 'Paul', 'Aeshna', 'Aryn', 'Rob']
# I obtain the sort function from https://www.kite.com/python/answers/how-to-sort-a-list-alphabetically-in-python
# I created a variable to put the sort in 
friends = sorted(my_friends)
# print(friends)
# 1B. Comment your code in 1A to convince yourself you understand how it works


# 2A. Get all the keys from the below dictionary, then print them out:
# Hint: there is a single command that can do this
#I found how to use the key fuction from https://www.tutorialspoint.com/python/dictionary_keys.htm
#The Key() allows me to pull out all the keys from the dicitionary 
my_account = {'username': 'pbloom',
			  'password': 'python3.7',
			  'balance': 101.8,
			  'transaction_dates': ['9/18/2020', '9/20/2020', '10/5/2020'],
			  'verified': True}
print('Value : %s' % my_account.keys())

# 2B. Comment your code in 2A to convince yourself you understand how it works



# 3A Count how many times the word 'wood' appears in the following string:
# Hint: there is a single command that can do this
print('QUESTION 3\n')
my_string = 'how much wood could a woodchuck chuck if a woodchuck could chuck wood?'
#variable created of what need to be counted
substring = 'wood'
#Had to use the count function https://www.programiz.com/python-programming/methods/string/count
#count function added to the original variable abd pass the second as a variable 
count = my_string.count(substring)
print(" the count is: ", count)
# 3B. Comment your code in 3A to convince yourself you understand how it works



# 4A Count how many times the string 'banana' appears in the following list:
# Hint: there is a way to do this with one line of code
print('QUESTION 4\n')
my_list = ['apple', 'banana', 'banana', 'cherry', 'mango', 'banana', 'banana', 'banana']
#I use the count method https://www.programiz.com/python-programming/methods/list/count
#create variable 
count = my_list.count('banana')
print('The count of banana is: ', count)

# 4B. Comment your code in 4A to convince yourself you understand how it works



# 5A Print out all of the unique strings in my_list
# Hint: there is a way to do this with one line of code
print('QUESTION 5\n')
# I use source to help https://www.freecodecamp.org/news/python-unique-list-how-to-get-all-the-unique-values-in-a-list-or-array/
my_list2 = list(set(my_list))
print(my_list2)

# 5B. Comment your code in 5A to convince yourself you understand how it works


# 6A. Import numpy, then use it to generate a random number between 0-1
print('QUESTION 6\n')
# Pull source to underdatand random from https://www.w3schools.com/python/numpy_random.asp
from numpy import random
print(random.rand())
# 6B. Comment your code in 6A to convince yourself you understand how it works


'''
Nice job! Hopefully after doing this challenge you feel a bit more ready to be able to search out new code solutions.
We'll be doing more challenges like this coming up in the future. 

Remember to comment all your code and push your work to your Github repo when you're done!
'''