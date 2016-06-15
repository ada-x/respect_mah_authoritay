# 3 steps as i see them:
# (1) make a file for the fres_tomatoes.py OR download it into sep file
# (2) file where movies class is defined, with doc
# (3) file where objects are defined and functions called, with doc

import webbrowser

class Movie:
	def __init__(self, title, trailer_youtube_url, storyline, poster_image_url):
		self.title = title
		self.trailer_youtube_url = trailer_youtube_url
		self.storyline = storyline
		self.poster_image_url = poster_image_url

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

