import os
import json

class Application():
    def __init__(self):
        self.__execution_on = True
        self.__commands = "01"
        self.__cinema_halls_filepath = "salit.json"
        self.__cinema_halls = []
        self.__load_cinema_halls(self.__cinema_halls_filepath)


    def main(self):
        self.__print_intro()

        while self.__execution_on:
            self.__execute_command(self.__get_command())

    def __print_intro(self):
        print("Tervetuloa Leffanaattoriin!")
    
    def __print_commands(self):
        print("")
        print("0 - Lopeta")
        print("1 - Tulosta salit")
        print("")

    def __get_command(self):
        self.__print_commands()

        while True:
            command = input("Valitse komento: ")

            if command in self.__commands:
                return command
    
    def __execute_command(self, command):
        if command == "0":
            self.__execution_on = False
            return
        elif command == "1":
            self.print_cinema_halls()
        

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
        self.__save_file()
    
    def print_cinema_halls(self):
        if len(self.__cinema_halls) < 1:
            print("Ei saleja.")
        else:
            for hall in self.__cinema_halls:
                print(hall)



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
        name = input("Anna nimi: ")

        while True:
            try:
                seats = int(input("Anna istumapaikkojen määrä: "))
            except:
                print("Virheellinen arvo, anna positiivinen kokonaisluku.")
            
            if seats > 0:
                break
            else:
                print("Virheellinen arvo, anna positiivinen kokonaisluku.")
        
        shows = []

        return name, seats, shows







def main():
    app = Application()
    #app.add_cinema_hall(False, "Sali1", 30, [])
    #app.add_cinema_hall(False, "Sali2", 402, [])
    app.main()



main()