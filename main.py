import os
import json

from films import Films
from cinemahall import CinemaHall
from settings import Settings


class Application():
    def __init__(self):
        self.__execution_on = True
        self.__logged_as_admin = False
        self.__login_success = False
        self.__settings = Settings()

        self.__cinema_halls = []
        self.__films = Films()
        self.__load_cinema_halls(self.__settings.get_cinema_halls_filepath())


    def main(self):
        self.__settings.print_intro()
        self.select_user()

        while self.__execution_on:
            self.__execute_commands()


    def select_user(self):
        self.__settings.print_user_types()
        self.exit_admin_mode()
        self.__login_success = False

        while not self.__login_success:
            choice = input("Valitse käyttäjä: ")
            if choice in ["1", "2"]:
                if choice == "1":
                    self.exit_admin_mode()
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


    def exit_admin_mode(self):
        self.__logged_as_admin = False
    
    def stop_execution(self):
        self.__execution_on = False

    def get_command(self):
        return input("Anna komento: ")

    def __execute_commands(self):
        if self.__logged_as_admin:
            self.execute_admin_commands()
        else:
            self.execute_customer_commands()


    def execute_customer_commands(self):
        while self.__execution_on and not self.__logged_as_admin:
            self.__settings.print_customer_commands()
            command = self.get_command()

            if command in self.__settings.get_customer_commands():
                func = self.__settings.get_customer_commands()[command] + "()"
                eval(func)


    def execute_admin_commands(self):
        while self.__execution_on and self.__logged_as_admin:
            self.__settings.print_admin_commands()
            command = self.get_command()

            if command in self.__settings.get_admin_commands():
                func = self.__settings.get_admin_commands()[command] + "()"
                eval(func)


    def cinema_halls_editing_menu(self):
        while True:
            self.__settings.print_edit_cinema_hall_commands()
            command = self.get_command()

            if command == "0":
                break

            if command in self.__settings.get_edit_halls_commands():
                func = self.__settings.get_edit_halls_commands()[command] + "()"
                eval(func)


    def __load_cinema_halls(self, path):
        try:
            data = self.__load_json_data_from_file(path)
                
            for hall in data:
                self.add_cinema_hall(False, hall["Nimi"], hall["Paikkoja"], hall["Näytökset"], loading_from_file = True)
        except:
            print(f"Virhe lukiessa tiedostoa \"{path}\". Virheellinen formaatti tai tyhjä tiedosto.")
        
        self.save_file()


    def __load_json_data_from_file(self, path):
        with open(path, "r") as file:
            data = json.load(file)
            return data


    def save_file(self):
        with open(self.__settings.get_cinema_halls_filepath(), "w") as file:
            json_compatible_dict_list = []
            for hall in self.__cinema_halls:
                json_compatible_dict_list.append(hall.form_dictionary_from_self())

            json.dump(json_compatible_dict_list, file, indent=1)

    
    def add_cinema_hall(self, manual: bool = True, name: str = "Ei nimeä", seats: int = 0, shows: list = [], loading_from_file = False):
        if manual:
            name, seats, shows = CinemaHall.create_new_hall_from_input(self)

        self.__cinema_halls.append(CinemaHall(name, seats, shows))
        if not loading_from_file:
            self.save_file()

    def edit_cinema_hall(self):
        self.print_cinema_halls()
        hall_index = self.__choose_cinema_hall_number()

        print("0 - Peruuta")
        print("1 - Muuta nimeä")
        print("2 - Muuta istuinpaikkojen määrää")

        command = self.get_command()


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


    def print_film_selection(self):
        film_list = self.__films.print_films()



def main():
    app = Application()
    app.main()

    app.save_file()





main()