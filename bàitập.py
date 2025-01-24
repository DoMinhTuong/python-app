class Movie():
    def __init__(self, id, name, rdate, score, link):
        self.id = id
        self.name = name
        self.rdate = rdate
        self.score = score
        self.link = link
        
    def update(self, new_data:dict):
        for key, value in new_data.items():
            if hasattr(self, key):
                setattr(self, key, value)
    
    def __str__(self):
        return f"{self.name} {self.rdate}) - {self.score} - {self.link}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "rdate": self.rdate,
            "score": self.score,
            "link": self.link
        }
        
class MovieList:
    def __init__(self):
        self.movies = []
    
    def add(self, m:Movie):
        self.movies.append(m)
        
    def update(self, m:Movie):
        for Movie in self.movies:
            if Movie.id == m.id:
                Movie.update(m.to_dict())
                return
        self.add(m)
        
        def delete(self, id):
            for Movie in self.movies:
                if Movie.id == id:
                    self.movies.remove(Movie)
                    return

        def get(self, id):
            for Movie in self.movies:
                if Movie.id == id:
                    return Movie
            return Movie
        
movie1 = Movie(1, "The Matrix", "1999-03-31", 8.7, "https://www.imdb.com/title/tt0133093/")
movie2 = Movie(2, "The Matrix Reloaded", "2003-05-15", 7.2, "https://www.imdb.com/title/tt0206294/")
movie3 = Movie(3, "The Matrix Revolutions", "2003-11-05", 6.7, "https://www.imdb.com/title/tt0242653/")
movie_list = [movie1, movie2, movie3]
movie4 = Movie(4, "The Matrix Resurrections", "2021-12-16", 6.2, "https://www.imdb.com/title/tt0242653/")
movie_list.append(movie4)
for movie in movie_list:
    if movie.id == 1:
        movie.update({"score"})
    if movie.id == 2:
        movie.update({"score"})











class Student:
    def __init__(self, student_id, name, age, score):
        self.id = student_id
        self.name = name
        self.age = age
        self.score = score

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self):
        return f"Student(id={self.id}, name={self.name}, age={self.age}, score={self.score})"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "score": self.score
        }

student_list = []

student1 = Student(1, "Alice", 20, 85)
student2 = Student(2, "Bob", 22, 90)
student3 = Student(3, "Charlie", 19, 75)

student_list.extend([student1, student2, student3])

def calculate_average_score(students):
    if not students:
        return 0
    return sum(student.score for student in students) / len(students)

def find_highest_and_lowest(students):
    if not students:
        return None, None
    highest = max(students, key=lambda s: s.score)
    lowest = min(students, key=lambda s: s.score)
    return highest, lowest

for student in student_list:
    if student.id == 1:
        student.update(score=95)
        break

student_list = [student for student in student_list if student.id != 2]

print("Danh sách student:")
for student in student_list:
    print(student)

average_score = calculate_average_score(student_list)
print(f"\nĐiểm trung bình của danh sách: {average_score:.2f}")

highest, lowest = find_highest_and_lowest(student_list)
if highest and lowest:
    print(f"\nStudent có điểm cao nhất: {highest}")
    print(f"Student có điểm thấp nhất: {lowest}")
