# Take sentence from user and sorted
sorted_sent = []

print "Lets order the words in a sentence you provide."
sent = raw_input("add sentence: ")

sorted_sent = sent.split(" ")

sorted_sent.sort()

for words in sorted_sent:
	print words

print "-".join(sorted_sent)
