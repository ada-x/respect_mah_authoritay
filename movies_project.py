import movies  # my file with the class definition
import fresh_tomatoes  # renders site

pi_movie = movies.Movie('Pi',
                        'https://www.youtube.com/watch?v=jo18VIoR2xU',
                        'a mathematician makes an incredible discovery',
                        'http://images.moviepostershop.com/pi-movie-poster-1998-1020474533.jpg')

big_fish = movies.Movie('Big Fish',
                        'https://www.youtube.com/watch?v=M3YVTgTl-F0',
                        'a story about the stories between a father and son',
                        'http://www.gstatic.com/tv/thumb/movieposters/32942/p32942_p_v8_aa.jpg')

gone_in_60_seconds = movies.Movie('Gone In 60 Seconds',
                                  'https://www.youtube.com/watch?v=o6AyAM1buQ8',
                                  'A reformed car thief is given three days to steal 50 pristine autos',
                                  'http://www.gstatic.com/tv/thumb/movieposters/25612/p25612_p_v8_aa.jpg')

lauberge_espagnole = movies.Movie('L\'auberge Espagnole',
                                  'https://www.youtube.com/watch?v=CCs6AzLeNQI',
                                  'a student\'s adventures living in Barcelona',
                                  'http://www.gstatic.com/tv/thumb/dvdboxart/30919/p30919_d_v8_aa.jpg')


lilo_and_stitch = movies.Movie('Lilo and Stitch',
                               'https://www.youtube.com/watch?v=hu9bERy7XGY',
                               'a lonely little girl gets an extra-terrestrial friend',
                               'http://img.lum.dolimg.com/v1/images/open-uri20150422-12561-1dajwj_23920e88.jpeg?region=0%2C0%2C1000%2C1409')

idiocracy = movies.Movie('Idiocracy',
                         'https://www.youtube.com/watch?v=BBvIweCIgwk',
                         'an average american wakes up in the future',
                         'http://www.gstatic.com/tv/thumb/dvdboxart/159395/p159395_d_v8_aa.jpg')

movies_list = [pi_movie, lilo_and_stitch, lauberge_espagnole,
               gone_in_60_seconds, big_fish, idiocracy]

# print(movies_list)
# pi_movie.show_trailer()

# opens and renders display
fresh_tomatoes.open_movies_page(movies_list)
