# In this file, creation of instances of the class Movie defined in media.py.

import media
# media is in the same folder with this file
import fresh_tomatoes

# Creating the instance for the movie "Finding Nemo". Providing its title, storyline, poster image and YouTube trailer
finding_nemo = media.Movie("Finding Nemo",
                           "The story of the overprotective ocellaris clownfish named Marlin who, along with a regal blue tang named Dory, searches for his abducted son Nemo all the way to Sydney Harbour. Along the way, Marlin learns to take risks and comes to terms with Nemo taking care of himself.",
                           "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
                           "https://www.youtube.com/watch?v=wZdpNglLbt8")

# Creating the instance for the movie "The Incredibles". Providing its title, storyline, poster image and YouTube trailer
the_incredibles = media.Movie("The Incredibles",
                     "The film follows a family of superheroes who are forced to hide their powers and live a quiet suburban life. Mr. Incredible's desire to help people draws the entire family into a battle with Syndrome, a former fan who now plots to wipe out all superheroes with his killer robot.",
                     "https://upload.wikimedia.org/wikipedia/en/e/ec/The_Incredibles.jpg",
                     "https://www.youtube.com/watch?v=eZbzbC9285I",)

# Creating the instance for the movie "Cars". Providing its title, storyline, poster image and YouTube trailer
cars = media.Movie("Cars",
              'In a world populated by anthropomorphic vehicles, the last race of the Piston Cup championship ends in a three-way tie between retiring veteran Strip "The King" Weathers, infamous runner-up Chick Hicks, and rookie Lightning McQueen. The tiebreaker race is scheduled for one week later at the Los Angeles International Speedway in California.',
              "https://upload.wikimedia.org/wikipedia/en/3/34/Cars_2006.jpg",
              "https://www.youtube.com/watch?v=SbXIj2T-_uk")

# Creating the instance for the movie "WALL-E". Providing its title, storyline, poster image and YouTube trailer
wall_e = media.Movie("WALL-E",
              "The story follows a trash compactor robot in a deserted world, left to clean a largely abandoned city. However, he is visited by a probe sent by the Axiom ship, whom he falls in love with and pursues across the galaxy.",
              "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
              "https://www.youtube.com/watch?v=8_X8N_SaU90")

# Creating the instance for the movie "Up". Providing its title, storyline, poster image and YouTube trailer
up = media.Movie("Up",
              "From Disney*Pixar comes Up, a comedy adventure about 78 year old balloon salesman Carl Fredericksen, who finally fulfills his lifelong dream of a great adventure when he ties thousands of balloons to his house and flies away to the wilds of South America.",
              "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
              "https://www.youtube.com/watch?v=qas5lWp7_R0")

# Creating the instance for the movie "Inside Out". Providing its title, storyline, poster image and YouTube trailer
inside_out = media.Movie("Inside Out",
              "Growing up can be a bumpy road, and it's no exception for Riley, who is uprooted from her Midwest life when her father starts a new job in San Francisco.",
              "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
              "https://www.youtube.com/watch?v=1FYA7Hshqo8")

# The list "movies" is the list of all instances (movies)
movies = [finding_nemo, the_incredibles, cars, wall_e, up, inside_out]
# The fresh_tomatoes.py is called to generate a web page having as an input the movie list
fresh_tomatoes.open_movies_page(movies)
