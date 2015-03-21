# Play with a couple of lists


movies = ['superman', 'batman', 'star wars', 'avatar', 'top gun', 'indiana jones']

new_list = []

favorite_films = "jungle book, kung fu panda, lion king"

new_list = favorite_films.split(", ")

print new_list

while len(new_list) != 0:
	last_movie = new_list.pop()
	movies.append(last_movie)

for mov in movies:
	print mov

print ""
print '*'.join(movies)
print movies[0]
print movies[-1]

print movies.pop()

for movs in movies:
	print movs

print movies[0:4]