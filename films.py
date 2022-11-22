import json

from settings import Settings
import input_validation as input_validation

settings = Settings()

class Films():
    def __init__(self):
        self.__films = []
        self.__load_films(Settings.get_films_filepath(Settings()))


    def __load_films(self, path: str):
        try:
            data = Settings.load_json_data_from_file(Settings(), path)
                
            for film in data:
                self.add_film(False, film["Nimi"], film["Ohjaaja"], film["Kesto"], film["Ikäraja"], loading_from_file = True)
        except:
            print(f"Virhe lukiessa tiedostoa \"{path}\". Virheellinen formaatti tai tyhjä tiedosto.")
        
        self.save_file()


    def save_file(self):
        with open(Settings.get_films_filepath(Settings()), "w") as file:
            json_compatible_dict_list = []
            for film in self.__films:
                json_compatible_dict_list.append(film.form_dictionary_from_self())

            json.dump(json_compatible_dict_list, file, indent=1)


    #################################################################
    # Adding, editing and removing related functions for films
    #################################################################
    
    def add_film(self, manual: bool = True, name:str = "Ei nimeä", director: str = "Ei ohjaajaa", runtime: int = 0, required_age: int = 0, loading_from_file = False):
        if manual:
            print("Elokuvan nimi: ", end="")
            name = input_validation.ask_user_to_input_a_name()
            print("Ohjaaja: ", end="")
            director = input_validation.ask_user_to_input_a_name()
            print("Kesto: ")
            runtime = input_validation.ask_user_to_input_number_zero_or_over()
            print("Ikäraja: ")
            runtime = input_validation.ask_user_to_input_number_zero_or_over()
        
        self.__films.append(Films.Film(name, director, runtime, required_age))

        if not loading_from_file:
            self.save_file()

    def edit_films(self):
        while True:
            Settings.print_edit_films_commands(Settings)
            command = input_validation.ask_command_from_user()

            if command == "0":
                break

            if command in settings.get_edit_films_commands():
                func = settings.get_edit_films_commands()[command] + "()"
                eval(func)

    def edit_film(self):
        while True:
            self.print_films()
            print("Anna muokattavan elokuvan järjestysnumero. Negatiivinen luku peruuttaa.")
            film_index = input_validation.ask_user_to_input_number_zero_or_over()
            
            if film_index < 0:
                break

            if self.film_index_exists(film_index):
                self.Film.edit_film(self.__films[film_index])
                break
            

    def remove_film(self):
        while True:
            self.print_films()
            print("Anna poistettavan elokuvan järjestysnumero. Negatiivinen luku peruuttaa.")
            film_index = input_validation.ask_user_to_input_number_zero_or_over()

            if film_index < 0:
                break

            if self.film_index_exists(film_index):
                self.__films.pop(film_index)
                break


    #################################################################
    # Miscellaneous
    #################################################################

    def film_index_exists(self, film_index) -> bool:
        if 0 <= film_index < len(self.__films):
            return True
        
        return False
    
    def print_films(self):
        index = 0
        for movie in self.__films:
            print(f"#{index}: {movie}")
            index += 1



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
        
        def get_name(self):
            return self.__name

        def change_name(self):
            name = input_validation.ask_user_to_input_a_name()
            self.__name = name
        
        def change_director(self):
            director = input_validation.ask_user_to_input_a_name()
            self.__director = director

        def change_runtime(self):
            runtime = input_validation.ask_user_to_input_number_zero_or_over()
            self.__runtime = runtime
        
        def change_required_age(self):
            required_age = input_validation.ask_user_to_input_number_zero_or_over()
            self.__required_age = required_age
        

        def edit_film(self):
            while True:
                settings.print_edit_single_film_commands()
                command = input_validation.ask_command_from_user()

                if command == "0":
                    break

                if command in settings.get_edit_single_film_commands():
                    func = settings.get_edit_single_film_commands()[command] + "()"
                    eval(func)
                    break
        
        def form_dictionary_from_self(self):
            return {"Nimi": self.__name, "Ohjaaja": self.__director, "Kesto": self.__runtime, "Ikäraja": self.__required_age}