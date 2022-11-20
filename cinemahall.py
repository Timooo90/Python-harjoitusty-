import input_validation as input_validation
from settings import Settings

settings = Settings()

class CinemaHall():
    def __init__(self, name: str = "no name", seats: int = 0, shows: list = []):
        self.__name = name
        self.__seats = seats
        self.__shows = shows
    

    def __str__(self):
        return(f"{self.__name}, paikkoja {self.__seats}")
    

    def form_dictionary_from_self(self):
        return {"Nimi": self.__name, "Paikkoja": self.__seats, "Näytökset": self.__shows}
    

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

    def get_name(self):
        return self.__name

    def get_shows(self):
        return self.__shows
    
    def print_shows(self):
        if len(self.__shows) < 1:
                print("Ei näytöksiä")
        else: 
            for show in self.__shows:
                print(show)
            
        print("-" * 20)

    def add_show(self):
        pass

    def remove_show(self):
        pass

    def edit_shows(self):
        while True:
            Settings.print_edit_shows_of_selected_hall_commands(Settings)
            command = input_validation.ask_command_from_user()

            if command == "0":
                return

            if command in settings.get_edit_shows_of_selected_hall_commands():
                func = settings.get_edit_shows_of_selected_hall_commands()[command] + "()"
                eval(func)