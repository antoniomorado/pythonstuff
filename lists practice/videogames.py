# Videogame catalogue management software

games = []

print "Lets rank your favorite games!"
choice = raw_input("Would you like to add a game? y or n? ")
while choice == "y":
	title = raw_input("Enter Title: >")
	games.append(title)
	print games
	choice = raw_input("Add another game? y or n? ")

print ""
print "Sorted alphabetically:"

games.sort()

for gm in games:
	print gm

