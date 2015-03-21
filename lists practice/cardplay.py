# practice with lists

cards = ['Ace', 'King', 'Queen', 'Jack']
i = 1

while i < 9:
	i = i + 1
	print "Adding card face = %s" % i
	cards.append(i)
	print cards

print "That is how you add cards to a deck"
print cards[3:8] # prints from jack to 5 (includes ordinal values 3-8 not including 8)
