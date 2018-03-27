# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
						"A story about a boy and his toys that come to life.",
						"http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = media.Movie("Avatar", 
					"A movie about blue people.",
					"http://photos.imageevent.com/wrestlingfanaticactionfigures/jamescameronavatarthemovie/vertical-bmw-avatar-movie-high-definition-images-free-333798.jpg",
					"https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#print (avatar.storyline)

small_soldiers = media.Movie("Small Soldiers",
							"A movie about small toy soldiers",
							"http://static.rogerebert.com/uploads/movie/movie_poster/small-soldiers-1998/large_l5laJWvcxgkoqC3nRPs9N5u55jR.jpg",
							"https://www.youtube.com/watch?v=YwIt5wagRsg")

saving_private_ryan = media.Movie("Saving Private Ryan",
								"A war movie about saving Matt Damon",
								"http://www.impawards.com/1998/posters/saving_private_ryan_ver2.jpg",
								"https://www.youtube.com/watch?v=zwhP5b4tD6g")

guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy",
								"A group of misfits save the universe.",
								"https://images-na.ssl-images-amazon.com/images/I/51T5sJngQLL.jpg",
								"https://www.youtube.com/watch?v=2XltzyLcu0g")

the_godfather = media.Movie("The Godfather",
							"A story about a guy who is someone's godfather.",
							"http://fontmeme.com/images/The-Godfather-Poster.jpg",
							"https://www.youtube.com/watch?v=sY1S34973zA")

movies = [toy_story, avatar, small_soldiers, saving_private_ryan, guardians_of_the_galaxy, the_godfather]

fresh_tomatoes.open_movies_page(movies)
