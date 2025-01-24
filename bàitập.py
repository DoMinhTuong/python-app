class Movie:
    def __init__(self, id, title, release_date, score, link):
        self.id = id
        self.title = title
        self.release_date = release_date
        self.score = score
        self.link = link
    
    def update(self, new_data:dict):
        for key, value in new_data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        
    def __str__(self):
        return f"{self.id} - {self.title} ({self.release_date}) - {self.score} - {self.link}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date,
            "score": self.score,
            "link": self.link
        }


class MovieList:
    def __init__(self):
        self.movies = []
        
    def add(self, m:Movie):
        self.movies.append(m)
        
    def update(self, m:Movie):
        for movie in self.movies:
            if movie.id == m.id:
                movie.update(m.to_dict())
                return
        self.add(m)
        
    def delete(self, id):
        for movie in self.movies:
            if movie.id == id:
                self.movies.remove(movie)
                return
    
    def get(self, id):
        for movie in self.movies:
            if movie.id == id:
                return movie
        return None


movie1 = Movie(1, "The Matrix", "1999-03-31", 8.7, "https://www.imdb.com/title/tt0133093/")
movie2 = Movie(2, "The Matrix Reloaded", "2003-05-15", 7.2, "https://www.imdb.com/title/tt0206294/")
movie3 = Movie(3, "The Matrix Revolutions", "2003-11-05", 6.7, "https://www.imdb.com/title/tt0242653/")
movie_list = [movie1, movie2, movie3]
movie4 = Movie(4, "The Matrix Resurrections", "2021-12-16", 6.2, "https://www.imdb.com/title/tt11896230/")
movie_list.append(movie4)
for movie in movie_list:
    if movie.id == 1:
        movie.update({"score": 9.0})
    if movie.id == 2:
        movie_list.remove(movie)

for movie in movie_list:
    print(movie)