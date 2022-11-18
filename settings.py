class Settings:
    def __init__(self):
        self.__admin_password = "123"

        self.__customer_commands = {"0": "self.stop_execution",
                                    "1": "self.print_cinema_halls",
                                    "9": "self.select_user"}

        self.__admin_commands = {"0": "self.exit_admin_mode",
                                "1": "self.cinema_halls_editing_menu"}
        
        self.__edit_halls_commands = {"1": "self.print_cinema_halls",
                                    "2": "self.add_cinema_hall",
                                    "3": "self.edit_cinema_hall",
                                    "4": "self.remove_cinema_hall"}

        self.__cinema_halls_filepath = "salit.json"
    

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

    def print_edit_cinema_commands(self):
        print("")
        print("0 - Takaisin")
        print("1 - Tulosta salit")
        print("2 - Luo uusi")
        print("3 - Muokkaa salia")
        print("4 - Poista sali")

    def get_admin_password(self):
        return self.__admin_password

    def get_admin_commands(self):
        return self.__admin_commands

    def get_customer_commands(self):
        return self.__customer_commands

    def get_edit_halls_commands(self):
        return self.__edit_halls_commands

    def get_cinema_halls_filepath(self):
        return self.__cinema_halls_filepath