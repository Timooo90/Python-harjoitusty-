import os
import json

from movie import Movie
from cinemahall import CinemaHall
from settings import Settings


class Application():
    def __init__(self):
        self.__execution_on = True
        self.__logged_as_admin = False
        self.__login_success = False

        self.__settings = Settings()

        self.__cinema_halls_filepath = "salit.json"
        self.__cinema_halls = []
        self.__load_cinema_halls(self.__cinema_halls_filepath)


    def main(self):
        self.__settings.print_intro()
        self.__select_user()

        while self.__execution_on:
            self.__execute_command(self.__get_command())


    def __select_user(self):
        self.__settings.print_user_types()
        
        self.__exit_admin_mode()
        self.__login_success = False
        while not self.__login_success:
            choice = input("Valitse käyttäjä: ")
            if choice in ["1", "2"]:
                if choice == "1":
                    self.__exit_admin_mode()
                    self.__login_success = True
                elif choice == "2":
                    self.__admin_login_passcheck()
    

    def __admin_login_passcheck(self):
        while True:
            attempt = input("Anna salasana: (no se on oletuksena tietysti \"123\")")

            if attempt == "":
                break

            if attempt == self.__settings.get_admin_password():
                self.__logged_as_admin = True
                self.__login_success = True
                print("Sisäänkirjaus onnistui!")
                break
            else:
                print("Väärä salasana. Anna tyhjä salasana, jos haluat peruuttaa kirjautumisen.")


    def __exit_admin_mode(self):
        self.__logged_as_admin = False


    def __get_command(self):
        if self.__logged_as_admin:
            self.__settings.print_admin_commands()
        else:
            self.__settings.print_customer_commands()

        while True:
            command = input("Valitse komento: ")

            if self.__logged_as_admin == True:
                if command in self.__settings.get_admin_commands():
                    return command

            else:
                if command in self.__settings.get_customer_commands():
                    return command
    

    def __execute_command(self, command):
        if self.__logged_as_admin == True:
            self.__execute_admin_command(command)
        else:
            self.__execute_customer_command(command)

    
    def __execute_customer_command(self, command):
        if command == "0":
            self.__execution_on = False
            return

        elif command == "1":
            self.print_cinema_halls()
        
        elif command == "9":
            self.__select_user()


    def __execute_admin_command(self, command):
        if command == "0":
            self.__exit_admin_mode()


    def __load_cinema_halls(self, path):
        try:
            data = self.__load_json_data_from_file(path)
                
            for hall in data:
                self.add_cinema_hall(False, hall["Nimi"], hall["Paikkoja"], hall["Näytökset"])
        except:
            print(f"Virhe lukiessa tiedostoa \"{path}\". Virheellinen formaatti tai tyhjä tiedosto.")


    def __load_json_data_from_file(self, path):
        with open(path, "r") as file:
            data = json.load(file)
            return data


    def __save_file(self):
        with open(self.__cinema_halls_filepath, "w") as file:
            json_compatible_dict_list = []
            for hall in self.__cinema_halls:
                json_compatible_dict_list.append(hall.form_dictionary_from_self())

            json.dump(json_compatible_dict_list, file, indent=1)

    
    def add_cinema_hall(self, manual: bool = True, name: str = "Ei nimeä", seats: int = 0, shows: list = []):
        if manual:
            name, seats, shows = CinemaHall.create_new_hall_from_input(self)

        self.__cinema_halls.append(CinemaHall(name, seats, shows))
        self.__save_file() # Tämä tulee siirtää johonkin järkevämpään kohtaan ettei tallenneta joka lisäyksen välissä turhaan.
    

    def print_cinema_halls(self):
        if len(self.__cinema_halls) < 1:
            print("Ei saleja.")
        else:
            for hall in self.__cinema_halls:
                print(hall)





def main():
    app = Application()

    #app.add_cinema_hall(False, "Sali1", 30, [])
    #app.add_cinema_hall(False, "Sali2", 402, [])

    app.main()



main()