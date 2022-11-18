class Settings:
    def __init__(self):
        self.__admin_password = "123"
        self.__customer_commands = ["0", "1", "9"]
        self.__admin_commands = ["0", "1"]
    
    def get_admin_password(self):
        return self.__admin_password

    def get_admin_commands(self):
        return self.__admin_commands

    def get_customer_commands(self):
        return self.__customer_commands

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
        print("1 - Muokkaa saleja")