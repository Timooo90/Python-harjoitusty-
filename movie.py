class Movie():
    def __init__(self, name: str, director: str, runtime: int, required_age: int):
        self.__name = name
        self.__director = director
        self.__runtime = runtime
        self.__required_age = required_age


    def __str__(self):
        return(f"{self.__name}, kesto {self.__runtime} minuuttia.")