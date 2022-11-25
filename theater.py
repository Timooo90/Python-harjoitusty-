import json
from datetime import datetime
from datetime import date
from datetime import timedelta

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
        while True:
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


    def confirm_removal_of_hall_with_shows(self) -> bool:
        remove = False

        while True:
            yes_or_no = input("Salissa on näytöksiä. Haluatko varmasti poistaa salin (k/e)? ")

            if yes_or_no == "k":
                remove = True
                break
            elif yes_or_no == "e":
                break
        
        return remove

    
    def __choose_cinema_hall_number(self) -> int:
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

            
    def print_halls_and_shows_in_readable_format(self, indexed_list: list):
        for show_and_hall in indexed_list:
            show = show_and_hall["Show"]
            hall = show_and_hall["Hall"]
            index = show_and_hall["Index"]

            date_and_time = show["Aloitusaika"]
            film_name = self.__films.get_film_name_from_id(show["Elokuvan ID"])
            available_seats = hall.get_number_of_seats() - show["Varauksia"]
            
            print(f"#{index} | Näytösaika: {date_and_time} | Sali: {hall.get_name()} | Elokuva: {film_name} | Vapaita paikkoja: {available_seats}")
    

    def edit_shows_in_a_hall(self):
        self.print_cinema_halls()
        hall_index = self.__choose_cinema_hall_number()

        if hall_index < 0:
            return

        self.__cinema_halls[hall_index].edit_shows()

    
    def browse_shows(self):
        while True:
            Settings.print_browse_shows_commands(Settings())
            command = input_validation.ask_command_from_user()

            if command == "0":
                return

            if command in Settings.get_browse_shows_commands(Settings()):
                func = Settings.get_browse_shows_commands(Settings())[command] + "()"
                eval(func)

    
    def seat_reservation(self, indexed_list, index):
        if index == 0:
            return
        else:
            self.reserve_seats_in_show(indexed_list[index - 1])
    
    
    def reserve_seats_in_show(self, show_info: dict):
        print("Kuinka monta paikkaa haluat varata näytökseen?")
        while True:
            number_to_reserve = input_validation.ask_user_to_input_number_zero_or_over()
            if number_to_reserve == 0:
                return
            else:
                hall_seats = show_info["Hall"].get_number_of_seats()
                reservations = show_info["Show"]["Varauksia"]
                show_id = show_info["Show"]["ID"]
                available_seats = hall_seats - reservations

                if number_to_reserve <= available_seats:
                    print("Varaus tehty!")
                    show_info["Hall"].reserve_seats_in_show(number_to_reserve, show_id)
                    
                    break
                else:
                    print(f"Esityksessä ei ole {number_to_reserve} vapaata paikkaa!")


    
    def get_and_print_indexed_list_and_chosen_index(self, show_list: list) -> list:
        indexed_list = self.add_indices_to_a_list_of_shows(show_list)
        self.print_halls_and_shows_in_readable_format(indexed_list)
        if len(indexed_list) < 1:
            return []
        index = self.get_user_show_choice(indexed_list[-1]["Index"])

        return indexed_list, index

                
    def choose_show_by_date(self):
        chosen_date = input_validation.get_manual_date_input()
        show_list = self.get_list_of_shows_for_given_date(chosen_date)

        if len(show_list) < 1:
            print("Ei näytöksiä valitulla aikavälillä.")
        else:
            indexed_list, index = self.get_and_print_indexed_list_and_chosen_index(show_list)
            self.seat_reservation(indexed_list, index)


    def choose_from_todays_shows(self):
        show_list = self.get_sorted_list_limited_by_days(0)
        indexed_list = self.add_indices_to_a_list_of_shows(show_list)

        if len(indexed_list) < 1:
            print("Ei näytöksiä valitulla aikavälillä.")
        else:
            indexed_list, index = self.get_and_print_indexed_list_and_chosen_index(show_list)
            self.seat_reservation(indexed_list, index)

    
    def choose_from_next_7_days_shows(self):
        show_list = self.get_sorted_list_limited_by_days(7)
        indexed_list = self.add_indices_to_a_list_of_shows(show_list)

        if len(indexed_list) < 1:
            print("Ei näytöksiä valitulla aikavälillä.")
        else:
            indexed_list, index = self.get_and_print_indexed_list_and_chosen_index(show_list)
            self.seat_reservation(indexed_list, index)


    def get_user_show_choice(self, largest_index: int) -> int:
        print("Aseta haluamasi esityksen järjestysluku")
        while True:
            choice = input_validation.ask_user_to_input_number_zero_or_over()

            if choice == 0:
                return 0
            
            if choice <= largest_index:
                return choice
            else:
                print(f"Esitystä numerolla {choice} ei löytynyt.")


    def add_indices_to_a_list_of_shows(self, list: list) -> list:
        indexed_list = list[:]
        index = 1

        for show in indexed_list:
            show["Index"] = index
            index += 1

        return indexed_list


    def get_shows_from_all_halls(self):
        show_list = []

        for hall in self.__cinema_halls:
            hall_shows = hall.get_shows()
            
            for show in hall_shows:             
                show_list.append({"Hall": hall, "Show": show})

        return show_list


    def sort_list_of_shows(self, show_list):
        return sorted(show_list, key=lambda d: d["Show"]["Aloitusaika"])
    
    def get_sorted_list_limited_by_days(self, days: int) -> list:
        show_list = self.sort_list_of_shows(self.get_shows_from_all_halls())
        limited_list = self.limit_list_of_shows_to_number_of_days_from_today(show_list, days)

        return limited_list

    def get_list_of_shows_for_given_date(self, date: datetime.date) -> list:
        show_list = self.get_shows_from_all_halls()
        sorted_list = self.sort_list_of_shows(show_list)

        return self.limit_list_of_shows_to_chosen_date(sorted_list, date)
    
    def limit_list_of_shows_to_chosen_date(self, shows: list, chosen_date: datetime.date) -> list:
        match_list = []

        for show in shows:
            show_datetime = input_validation.string_to_date(show["Show"]["Aloitusaika"])
            show_date = show_datetime.date()

            if show_date == chosen_date:
                match_list.append(show)
        
        return match_list

    def limit_list_of_shows_to_number_of_days_from_today(self, shows: list, max_days: int):
        date_now = datetime.today().date()
        match_list = []

        for show in shows:
            show_datetime = input_validation.string_to_date(show["Show"]["Aloitusaika"])
            show_date = show_datetime.date()

            if show_date >= date_now and show_date <= date_now + timedelta(days=max_days):
                match_list.append(show)
        
        return match_list



    #################################################################
    # For testing purposes
    #################################################################

if __name__ == "__main__":
    theater = Theater()
    shows = theater.get_shows_from_all_halls()

    shows_sorted = theater.sort_list_of_shows(shows)

    chosen_date = date(2022, 11, 24)

    limited_list = theater.limit_list_of_shows_to_chosen_date(shows_sorted, chosen_date)

    for show in limited_list:
        print(show)

    #for show in shows_sorted:
        #print(show)
    
    #test_list = theater.limit_list_of_shows_to_number_of_days_from_today(shows_sorted, 7)

    #for show in test_list:
        #print(show)