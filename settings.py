import json

class Settings:
    def __init__(self):
        self.__admin_password = "123"
        self.__last_acceptable_year = 2200

        self.__cinema_halls_filepath = "salit.json"
        self.__films_filepath = "films.json"

        self.__customer_commands = {
                                "0": "self.stop_execution",
                                "1": "self.theater.print_cinema_halls",
                                "9": "self.select_user"
        }

        self.__admin_commands = {
                                "0": "self.exit_admin_mode",
                                "1": "self.theater.cinema_halls_editing_menu",
                                "2": "self.theater.films_editing_menu",
                                "3": "self.theater.shows_editing_menu"
        }

        self.__edit_halls_commands = {
                                "1": "self.print_cinema_halls",
                                "2": "self.add_cinema_hall",
                                "3": "self.edit_cinema_hall",
                                "4": "self.remove_cinema_hall"
        }
        self.__edit_films_commands = {
                                "1": "self.print_films",
                                "2": "self.add_film",
                                "3": "self.edit_film",
                                "4": "self.remove_film"
        }
        
        self.__edit_single_film_commands = {
                                "1": "self.change_name",
                                "2": "self.change_director",
                                "3": "self.change_runtime",
                                "4": "self.change_required_age"
        }

        self.__edit_shows_commands = {
                                "1": "self.print_all_shows",
                                "2": "self.edit_shows_in_a_hall"
        }

        self.__edit_shows_of_selected_hall = {
                                "1": "self.print_shows",
                                "2": "self.add_show",
                                "3": "self.remove_show"
        }


    def print_intro(self):
        print("Tervetuloa Leffanaattoriin!")

    def print_user_types(self):
        print("Käyttäjäluokat: ")
        print("1 - Asiakas")
        print("2 - Omistaja")
        print("")

    def print_customer_commands(self):
        print("")
        print("0 - Sulje ohjelma")
        print("1 - Tulosta salit")
        print("9 - Vaihda käyttäjää")
        print("")

    def print_admin_commands(self):
        print("")
        print("0 - Poistu")
        print("1 - Hallinnoi saleja")
        print("2 - Hallinnoi elokuvia")
        print("3 - Hallinnoi näytöksiä")

    def print_edit_cinema_halls_commands(self):
        print("")
        print("0 - Takaisin")
        print("1 - Tulosta salit")
        print("2 - Luo uusi")
        print("3 - Muokkaa salia")
        print("4 - Poista sali")

    def print_edit_single_hall_commands(self):
        print("")
        print("0 - Peruuta")
        print("1 - Muuta nimeä")
        print("2 - Muuta istuinpaikkojen määrää")

    def print_edit_films_commands(self):
        print("")
        print("0 - Takaisin")
        print("1 - Tulosta elokuvavalikoima")
        print("2 - Lisää uusi elokuva")
        print("3 - Muokkaa elokuvaa")
        print("4 - Poista elokuva")
    
    def print_edit_single_film_commands(self):
        print("")
        print("0 - Takaisin")
        print("1 - Vaihda elokuvan nimi")
        print("2 - Vaihda ohjaajan nimi")
        print("3 - Muuta kestoa")
        print("4 - Muuta ikärajaa")

    def print_edit_shows_commands(self):
        print("")
        print("0 - Takaisin")
        print("1 - Tulosta kaikki näytökset")
        print("2 - Hallitse näytöksiä")

    def print_edit_shows_of_selected_hall_commands(self):
        print("")
        print("0 - Takaisin")
        print("1 - Tulosta salin näytökset")
        print("2 - Lisää näytös")
        print("3 - Poista näytös")

    def print_select_date_options(self):
        print("Valitse päivämäärä: ")
        print("0 - Tänään")
        print("1 - Huomenna")
        print("2 - Aseta päivämäärä")

    def get_admin_password(self):
        return self.__admin_password

    def get_admin_commands(self):
        return self.__admin_commands

    def get_customer_commands(self):
        return self.__customer_commands

    def get_edit_halls_commands(self):
        return self.__edit_halls_commands

    def get_edit_films_commands(self):
        return self.__edit_films_commands
    
    def get_edit_single_film_commands(self):
        return self.__edit_single_film_commands
    
    def get_edit_shows_commands(self):
        return self.__edit_shows_commands

    def get_edit_shows_of_selected_hall_commands(self):
        return self.__edit_shows_of_selected_hall

    def get_cinema_halls_filepath(self):
        return self.__cinema_halls_filepath
    
    def get_films_filepath(self):
        return self.__films_filepath

    def get_default_movies(self):
        return self.__default_movies

    def load_json_data_from_file(self, path: str):
        with open(path, "r") as file:
            data = json.load(file)
            return data
        
    def get_last_acceptable_year(self):
        return self.__last_acceptable_year