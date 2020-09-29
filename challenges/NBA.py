print("Challenge 2.1:")
jamal_murray_3pts_made = 46
# TODO: Create variable here for number of 3 pt shots made by Fred VanVleet
fred_vanvleet_3pts_made = 34
# TODO: Create variable here for number of 3 pt shots made by James Harden
james_harden_3pts_made = 57

print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
# TODO: Create print statement here for Fred VanVleet
print(f"In the 2020 NBA playoffs, Fred Vanleet made {fred_vanvleet_3pts_made} 3 point shots")
# TODO: Create print statement here for James Harden
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots")

print()

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
# TODO: Create variable here for number of 3 pt shot attempts by Jamal 
jamal_murray_3pts_attempt = 50
# TODO: Create variable here for number of 3 pt shot attempts by Fred VanVleet
fred_vanvleet_3pts_attempt = 20
# TODO: Create variable here for number of 3 pt shot attempts by James Harden
james_harden_3pts_attempt  = 28
print()

print("Challenge 2.4: Build on your print statement")
# TODO: Copy the three print statements you wrote in Challenge 2.2 and extend them to also print
# the number of three point shots for each player. E.g., output should be similar to
# "In the 2020 NBA playoffs, player X made Y 3 point shots and Z 3 point shot attempts."
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots and attempted {jamal_murray_3pts_attempt} 3 point shots ")
print(f"In the 2020 NBA playoffs, Fred Vanleet made {fred_vanvleet_3pts_made} 3 point shots and attempted {fred_vanvleet_3pts_attempt} 3 point shots ")
print(f"In the 2020 NBA playoffs, Fred Vanleet made {james_harden_3pts_made} 3 point shots and attempted {jamal_murray_3pts_attempt} 3 point shots ")
print()

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`
# TODO: Calculate and print the 3 point percentage for Jamal Murray
jamal_murray_3pts_percentage = jamal_murray_3pts_made / jamal_murray_3pts_attempt
print(jamal_murray_3pts_percentage)
# TODO: Calculate and print the 3 point percentage for Fred VanVleet
fred_vanvleet_3pts_percentage = fred_vanvleet_3pts_made / fred_vanvleet_3pts_attempt
print(fred_vanvleet_3pts_percentage)
# TODO: Calculate and print the 3 point percentage for James Harden
james_harden_3pts_percentage = james_harden_3pts_made / james_harden_3pts_attempt
print(james_harden_3pts_percentage)
# print()

print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
 # TODO: Print the giant chunk of text out using escape characters so each sentence comes out on a new line
print(f"In the 2020 NBA playoffs the best teams played for the championship.\n Superstar plays like Jamal Murray, Fred Vanvleet, and James Harden put on a 3 point client.\n The game was watched by millions of people.\n The bookies took in alot of money that day.")

print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
 # TODO: As above, print out the paragraph with only 1 sentence per line, and all in upper case
NBA = "In the 2020 NBA playoffs the best teams played for the championship. \n Superstar plays like Jamal Murray, Fred Vanvleet, and James Harden put on a 3 point client. \n The game was watched by millions of people.  \n The bookies took in a lot of money that day."
print(NBA.upper())
print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# TODO: make a variable called `lakers_are_best` to indicate this
lakers_are_best = True
# # TODO: print out the variable in an f-string to convey your opinion on the lakers
print(f' The lakers are the best is {lakers_are_best}!')

print('Challenge 3.4: Type Conversion')
# TODO: Convert your `lakers_are_best` variable to an integer, and print it out. 
lakers_2 = int(lakers_are_best)
print(type(lakers_2))

# # TODO: Convert your `lakers_are best` variable to a float, and print it out
lakers_1 = float(lakers_are_best)
print(type(lakers_1))
print('Challenge 3.5: Type Conversion Part 2')
# TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.
jamal_str = str(jamal_murray_3pts_percentage)
print(type(jamal_str))
fred_str = str(fred_vanvleet_3pts_percentage)
print(type(fred_str))
james_str = str(james_harden_3pts_percentage)
print(type(james_str))
# # TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.
jamal_int = int(jamal_murray_3pts_percentage)
fred_int = int(fred_vanvleet_3pts_percentage)
james_int = int(james_harden_3pts_percentage)
print(type(jamal_int))
print(type(fred_int))
print(type(james_int))