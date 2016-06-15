import webbrowser


class Movie:

    def __init__(self, title, trailer_url, storyline, poster_image_url):
        self.title = title
        self.trailer_youtube_url = trailer_url
        self.storyline = storyline
        self.poster_image_url = poster_image_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
