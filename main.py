import input_validation as input_validation
from settings import Settings
from theater import Theater


class Application():
    def __init__(self):
        self.__execution_on = True
        self.__logged_as_admin = False
        self.__login_success = False
        self.theater = Theater()


    def main(self):
        Settings.print_intro(Settings())
        self.select_user()

        while self.__execution_on:
            self.__execute_commands()


    def select_user(self):
        Settings.print_user_types(Settings())
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

            if attempt == Settings.get_admin_password(Settings()):
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

    def __execute_commands(self):
        if self.__logged_as_admin:
            self.execute_admin_commands()
        else:
            self.execute_customer_commands()


    def execute_customer_commands(self):
        while self.__execution_on and not self.__logged_as_admin:
            Settings.print_customer_commands(Settings())
            command = input_validation.ask_command_from_user()

            if command in Settings.get_customer_commands(Settings()):
                func = Settings.get_customer_commands(Settings())[command] + "()"
                eval(func)


    def execute_admin_commands(self):
        while self.__execution_on and self.__logged_as_admin:
            Settings.print_admin_commands(Settings())
            command = input_validation.ask_command_from_user()

            if command in Settings.get_admin_commands(Settings()):
                func = Settings.get_admin_commands(Settings())[command] + "()"
                eval(func)



def main():
    app = Application()
    app.main()

    app.theater.save_file()


main()