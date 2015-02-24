the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number
	
#same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i
	
# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
# range is a function used to create lists. It has a range(start, stop[,step]), if start
# is not defined is defaults to 0, if step is not defined its steps through defaults to 1.
# The range function only does numbers from first to last, NOT INCLUDING THE LAST.
for i in range(0, 6):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)


# We can save the entire effort above by straight assigning the range function to elements
# like this: 
# elements = range(0, 6)

# now we can print them out too
for i in elements:
	print "Elements was: %d" % i	
	
# Other function calls besides appends for lists include:
# append(value) appends value to end of list. Can only append 1 value at a time
# count(value) returns number of occurrences of a value
# extend(iterable) extend list by appending elements from the iterable
# index(value, [start, [stop]]) returns first index of value.
# insert(index, object) inserts object before index
# pop([index]) remove and return item at index (default last)
# remove(value) removes first occurence of value
# reverse() reverse *in place*
# sort(cmp=None, key=None, reverse=False) stable sort *in place*
