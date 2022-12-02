import tkinter as tk
from functools import partial

from theater import Theater

class GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("640x480")
        self.root.title("Leffanaattori")
        self.theater = Theater()

        self.__hall_buttonframe = tk.Frame(self.root, pady=10)
        self.__show_buttonframe = tk.Frame(self.root, pady=10)
        self.__hall_buttons = []
        self.__show_buttons = []

        self.__main()

    def __main(self):        
        self.print_halls()

        self.root.mainloop()


        
    def set_up_4_column_hall_buttonframe(self):
        for i in range(4):
            self.__hall_buttonframe.columnconfigure(i, weight=1)
    
    def set_up_4_column_show_buttonframe(self):
        for i in range(4):
            self.__hall_buttonframe.columnconfigure(i, weight=1)

    def print_halls(self):
        self.label = tk.Label(self.root, text="Salit:", font=("Arial", 25))
        self.label.pack(padx=10, pady=10)

        halls = self.theater.get_cinema_halls()

        for hall in halls:
            hall_name = hall.get_name()

            command_with_argument = partial(self.open_show_selection, hall_name)
            self.__hall_buttons.append(tk.Button(self.__hall_buttonframe, text=f"{hall_name}", width = 20, command=command_with_argument))

        
        self.set_buttons_in_grid("hall")

            
    def set_buttons_in_grid(self, button_type: str):
        row_no = 0
        column_no = 0

        button_number = 0

        if button_type == "hall":
            for button in self.__hall_buttons:
                button.grid(row=row_no, column=column_no)

                button_number += 1

                column_no += 1

                if button_number % 4 == 0:
                    row_no += 1
                    column_no = 0

        elif button_type == "show":
            for button in self.__show_buttons:
                button.grid(row=row_no, column=column_no)

                button_number += 1

                column_no += 1

                if button_number % 4 == 0:
                    row_no += 1
                    column_no = 0
                
        self.__hall_buttonframe.pack()


    def open_show_selection(self, hall_name: str):
        self.label = tk.Label(self.root, text="Näytökset:", font=("Arial", 25))
        self.label.pack(padx=10, pady=10)


        shows = self.theater.get_cinema_hall_by_name(hall_name).get_shows()

        for show in shows:
            show_start = show["Aloitusaika"]

            self.__show_buttons.append(tk.Button(self.__show_buttonframe, text=f"{show_start}", width = 20))
        
        self.set_buttons_in_grid("show")


    def delete_old_buttons(self, buttons: list):
        for button in buttons:
            button.destroy()



if __name__ == "__main__":
    app = GUI()