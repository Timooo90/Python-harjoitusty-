from settings import Settings

settings = Settings()

class Films():
    def __init__(self):
        self.__films = []
        self.load_default_movies()

    def load_default_movies(self):
        defaults = settings.get_default_movies()

        for film in defaults:
            self.__films.append(film)

    def print_films(self):
        for movie in self.__films:
            print(movie)

    class Film():
        def __init__(self, name: str, director: str, runtime: int, required_age: int):
            self.__name = name
            self.__director = director
            self.__runtime = runtime
            self.__required_age = required_age


        def __str__(self):
            return(f"{self.__name}, kesto {self.__runtime} minuuttia. Ohjannut {self.__director}.")

        def get_age_limit(self):
            return self.__required_age