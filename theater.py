import json

import input_validation as input_validation
from films import Films
from cinemahall import CinemaHall
from settings import Settings

class Theater():
    def __init__(self):
        self.__cinema_halls = []
        self.__films = Films()
        self.__load_cinema_halls(Settings.get_cinema_halls_filepath(Settings()))


    def __load_cinema_halls(self, path: str):
        try:
            data = self.__load_json_data_from_file(path)
                
            for hall in data:
                self.add_cinema_hall(False, hall["Nimi"], hall["Paikkoja"], hall["Näytökset"], loading_from_file = True)
        except json.JSONDecodeError:
            print(f"Virhe lukiessa tiedostoa \"{path}\". Virheellinen formaatti tai tyhjä tiedosto.")
        
        self.save_file()
    
    
    def __load_json_data_from_file(self, path: str):
        with open(path, "r") as file:
            data = json.load(file)
            return data


    def save_file(self):
        with open(Settings.get_cinema_halls_filepath(Settings()), "w") as file:
            json_compatible_dict_list = []
            for hall in self.__cinema_halls:
                json_compatible_dict_list.append(hall.form_dictionary_from_self())

            json.dump(json_compatible_dict_list, file, indent=1)


    #################################################################
    # Cinema hall related functions
    #################################################################
    
    def cinema_halls_editing_menu(self):
        while True:
            Settings.print_edit_cinema_halls_commands(Settings())
            command = input_validation.ask_command_from_user()

            if command == "0":
                break

            if command in Settings.get_edit_halls_commands(Settings()):
                func = Settings.get_edit_halls_commands(Settings())[command] + "()"
                eval(func)
    

    def add_cinema_hall(self, manual: bool = True, name: str = "Ei nimeä", seats: int = 0, shows: list = [], loading_from_file = False):
        if manual:
            name, seats, shows = CinemaHall.create_new_hall_from_input(self)

        self.__cinema_halls.append(CinemaHall(name, seats, shows))
        if not loading_from_file:
            self.save_file()


    def edit_cinema_hall(self):
        self.print_cinema_halls()
        hall_index = self.__choose_cinema_hall_number()
        Settings.print_edit_single_hall_commands(Settings())

        command = input_validation.ask_command_from_user()

        if command == "0":
            return
        elif command == "1":
            self.__cinema_halls[hall_index].change_cinema_hall_name()
        elif command == "2":
            self.__cinema_halls[hall_index].change_cinema_hall_seats()
    

    def remove_cinema_hall(self):
        self.print_cinema_halls()
        hall_index = self.__choose_cinema_hall_number()

        if hall_index < 0:
            return

        if len(self.__cinema_halls[hall_index].get_shows()) > 0:
            remove = self.confirm_removal_of_hall_with_shows()
        else:
            remove = True

        if remove:
            self.__cinema_halls.pop(hall_index)


    def confirm_removal_of_hall_with_shows(self):
        remove = False

        while True:
            yes_or_no = input("Salissa on näytöksiä. Haluatko varmasti poistaa salin (k/e)? ")

            if yes_or_no == "k":
                remove = True
                break
            elif yes_or_no == "e":
                break
        
        return remove

    
    def __choose_cinema_hall_number(self):
        while True:
            try:
                index_to_edit = int(input("Anna salin järjestysnumero: "))

                if index_to_edit < 0:
                    break

                if 0 <= index_to_edit < len(self.__cinema_halls):
                    break
            except:
                print("Virhe, anna kokonaisluku tai poistu antamalla negatiivinen luku")
        
        return index_to_edit
        

    def print_cinema_halls(self):
        if len(self.__cinema_halls) < 1:
            print("Ei saleja.")
        else:
            hall_index = 0
            for hall in self.__cinema_halls:
                print(f"#{hall_index}: {hall}")
                hall_index += 1




    #################################################################
    # Films related functions
    #################################################################

    def print_film_selection(self):
        self.__films.print_films()

    def films_editing_menu(self):
        self.__films.edit_films()


    #################################################################
    # Shows related functions
    #################################################################


    def shows_editing_menu(self):
        while True:
            Settings.print_edit_shows_commands(Settings())
            command = input_validation.ask_command_from_user()

            if command == "0":
                return

            if command in Settings.get_edit_shows_commands(Settings()):
                func = Settings.get_edit_shows_commands(Settings())[command] + "()"
                eval(func)

    
    def print_all_shows(self):
        for hall in self.__cinema_halls:
            print(f"Sali: {hall.get_name()}")
            print("Näytökset: ")
            
            hall.print_shows()
    

    def edit_shows_in_a_hall(self):
        self.print_cinema_halls()
        hall_index = self.__choose_cinema_hall_number()

        if hall_index < 0:
            return

        if len(self.__cinema_halls[hall_index].get_shows()) > 0:
            self.__cinema_halls[hall_index].edit_shows()