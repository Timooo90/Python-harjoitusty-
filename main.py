import os
import json

class Application():
    def __init__(self):
        self.__cinema_halls_filepath = "salit.json"
        self.__cinema_halls = []
        self.__load_cinema_halls(self.__cinema_halls_filepath)

    def __load_cinema_halls(self, path):
        data = self.__load_json_data_from_file(path)
        
        for hall in data:
            self.add_cinema_hall(False, hall["Nimi"], hall["Paikkoja"], hall["Näytökset"])


    def __load_json_data_from_file(self, path):
        with open(path, "r") as file:
            data = json.load(file)
            return data

    def __save_file(self):
        with open(self.__cinema_halls_filepath, "w") as file:
            json.dump(self.__cinema_halls, file)

    
    def add_cinema_hall(self, manual: bool = True, name: str = "Ei nimeä", seats: int = 0, shows: list = []):
        if manual:
            name, seats, shows = CinemaHall.create_new_hall_from_input(self)

        self.__cinema_halls.append({"Nimi": name, "Paikkoja": seats, "Näytökset": shows})
        self.__save_file()



class CinemaHall():
    def __init__(self, name: str = "no name", seats: int = 0, shows: list = []):
        self.__filepath = "salit.json"
        self.__read_file_or_create_if_not_found()
        self.__name = name
        self.__seats = seats
        self.__shows = shows
    
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
    #app.add_cinema_hall()
    #app.add_cinema_hall()




main()