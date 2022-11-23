from datetime import datetime

import input_validation as input_validation
from settings import Settings
from films import Films

settings = Settings()

class CinemaHall():
    def __init__(self, name: str = "no name", seats: int = 0, shows: list = []):
        self.__name = name
        self.__seats = seats
        self.__shows = shows
    

    def __str__(self):
        return(f"{self.__name}, paikkoja {self.__seats}")
    

    def form_dictionary_from_self(self): # For JSON format saving in a file
        return {"Nimi": self.__name, "Paikkoja": self.__seats, "Näytökset": self.__shows}
    

    #################################################################
    # Adding, editing and removing related functions for cinema halls
    #################################################################

    def create_new_hall_from_input(self):
        print("Luodaan uusi sali.")
        print("Salin nimi: ", end="")
        name = input_validation.ask_user_to_input_a_name()

        print("Paikkojen määrä: ")
        seats = input_validation.ask_user_to_input_number_zero_or_over()
                    
        shows = []

        return name, seats, shows

      
    def change_cinema_hall_name(self):
        new_name = input("Anna salin uusi nimi: ")
        self.__name = new_name
    

    def change_cinema_hall_seats(self):
        while True:
            new_number = int(input("Anna paikkojen määrä: "))

            if input_validation.is_integer_and_at_least_zero(new_number):
                break
            else:
                print("Anna positiivinen kokonaisluku.")
            
            if new_number < 0:
                continue
            else:
                break

        self.__seats = new_number


            
    #################################################################
    # Show related functions
    #################################################################

    def add_show(self):
        start_date = input_validation.ask_date_from_user()
        start_HH_MM = input_validation.ask_time_HH_MM_from_user()

        date_time_combined = datetime(start_date.year, start_date.month, start_date.day, start_HH_MM.hour, start_HH_MM.minute)

        start_time_string = input_validation.date_to_string(date_time_combined)

        film = Films.select_film_for_show(Films())

        show_id = self.generate_unique_show_id()

        show = {"ID": show_id, "Aloitusaika": start_time_string, "Elokuvan ID": film.get_id(), "Varauksia": 0}

        self.__shows.append(show)


    def generate_unique_show_id(self):
        ids = []

        for show in self.__shows:
            ids.append(show["ID"])
        
        if len(ids) < 1:
            return 1
        
        show_id = ids[-1] + 1

        while True:
            if not show_id in ids:
                return show_id
            show_id += 1
        
    def reserve_seats_in_show(self, number_of_seats: int, show_id: int):
        for show in self.__shows:
            if show["ID"] == show_id:
                show["Varauksia"] += number_of_seats

        
    def edit_shows(self):
        while True:
            Settings.print_edit_shows_of_selected_hall_commands(Settings)
            command = input_validation.ask_command_from_user()

            if command == "0":
                return

            if command in settings.get_edit_shows_of_selected_hall_commands():
                func = settings.get_edit_shows_of_selected_hall_commands()[command] + "()"
                eval(func)


    def remove_show(self):
        self.print_shows()
        print("Valitse poistettavan näytöksen järjestysluku: ")

        while True:
            index = input_validation.ask_user_to_input_number_zero_or_over()

            if index < len(self.__shows):
                self.__shows.pop(index)
                break

            
    def get_shows(self):
        return self.__shows
    
    def print_shows(self):
        index = 0
        if len(self.__shows) < 1:
                print("Ei näytöksiä")
        else: 
            for show in self.__shows:
                show_date = show["Aloitusaika"]
                show_film = Films.get_film_name_from_id(Films(), show["Elokuvan ID"])

                print(f"#{index}: Esitysaika: {show_date}, Elokuva: {show_film}")
                index += 1
            
        print("-" * 20)

    
    def get_number_of_available_seats(self, show_reservations: int):
        return self.get_number_of_seats - show_reservations
        
    
    #################################################################
    # Miscellaneous
    #################################################################

    def get_name(self):
        return self.__name
    
    def get_number_of_seats(self):
        return self.__seats




    #################################################################
    # For testing purposes
    #################################################################

if __name__ == "__main__":
    hall = CinemaHall()
    print(hall.add_show())