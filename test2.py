class Anime:
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


class AnimeList:
    def __init__(self):
        self.animes = []
        
    def add(self, a:Anime):
        self.animes.append(a)
        
    def update(self, a:Anime):
        for anime in self.animes:
            if anime.id == a.id:
                anime.update(a.to_dict())
                return
        self.add(a)
        
    def delete(self, id):
        for anime in self.animes:
            if anime.id == id:
                self.animes.remove(anime)
                return
    
    def get(self, id):
        for anime in self.animes:
            if anime.id == id:
                return anime
        return None


anime1 = Anime(1, "Attack on Titan", "2013-04-07", 9.1, "https://www.imdb.com/title/tt2560140/")
anime2 = Anime(2, "Naruto", "2002-10-03", 8.4, "https://www.imdb.com/title/tt0409591/")
anime3 = Anime(3, "One Piece", "1999-10-20", 9.0, "https://www.imdb.com/title/tt0388629/")
anime_list = [anime1, anime2, anime3]
anime4 = Anime(4, "Demon Slayer", "2019-04-06", 8.7, "https://www.imdb.com/title/tt9335498/")
anime_list.append(anime4)
for anime in anime_list:
    if anime.id == 1:
        anime.update({"score": 9.2})
    if anime.id == 2:
        anime_list.remove(anime)

for anime in anime_list:
    print(anime)
