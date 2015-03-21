# stack hats and sort the order

print "I have so many hats. Here is a list of them."
hats = "Texas, Michigan, Alabama, Tigers, Marlins, Steelers, Diamondbacks, Fedor, Shogun, Streetfighter"

print hats

teams = hats.split(', ')

print "Please add a team."
teams.append(raw_input(">"))

teams.sort()

for team in teams:
	print team

print "or backwards order\n"

while len(teams) > 0:
	print teams.pop()

