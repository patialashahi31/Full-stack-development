class Movie():
    def __init__(self,title,storyline,poster,youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = youtube_url


carry_on_jatta = Movie("Carry On jatta","Comedy","https://upload.wikimedia.org/wikipedia/en/thumb/b/be/Carry_on_Jatta_-_Poster.jpg/220px-Carry_on_Jatta_-_Poster.jpg",
                                                 "https://www.youtube.com/watch?v=7UoOy9PvJrA")

movies = [carry_on_jatta]
import fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
