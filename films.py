from settings import Settings
import input_validation as input_validation

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
    
    def add_film(self, manual: bool = False, name:str = "Ei nimeä", director: str = "Ei ohjaajaa", runtime: int = 0, required_age: int = 0):
        if manual:
            print("Elokuvan nimi: ", end="")
            name = input_validation.ask_user_to_input_a_name()
            print("Ohjaaja: ", end="")
            director = input_validation.ask_user_to_input_a_name()
            print("Kesto: ")
            runtime = input_validation.ask_user_to_input_number_over_zero()
            print("Ikäraja: ")
            runtime = input_validation.ask_user_to_input_number_over_zero()
        
        self.__films.append(Films.Film(name, director, runtime, required_age))



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
        