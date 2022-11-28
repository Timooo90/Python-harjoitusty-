import tkinter as tk

from theater import Theater

class GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("640x480")
        self.root.title("Leffanaattori")
        self.theater = Theater()

        self.__buttonframe = tk.Frame(self.root, pady=10)
        self.__hall_buttons = []

        self.__main()

    def __main(self):        
        self.print_halls()

        self.root.mainloop()


        
    def set_up_4_column_buttonframe(self):
        for i in range(4):
            self.__buttonframe.columnconfigure(i, weight=1)

    def print_halls(self):
        self.label = tk.Label(self.root, text="Salit:", font=("Arial", 25))
        self.label.pack(padx=10, pady=10)

        self.__hall_buttons.clear()
        halls = self.theater.get_cinema_halls()

        for hall in halls:
            hall_name = hall.get_name()
            shows = hall.get_shows()
            self.__hall_buttons.append(tk.Button(self.__buttonframe, text=f"{hall_name}", width = 20))

        
        self.set_buttons_in_grid()

            
    def set_buttons_in_grid(self):
        row_no = 0
        column_no = 0

        button_number = 0
        for button in self.__hall_buttons:
            button.grid(row=row_no, column=column_no)

            button_number += 1

            column_no += 1

            if button_number % 4 == 0:
                row_no += 1
                column_no = 0

                
        self.__buttonframe.pack()





if __name__ == "__main__":
    app = GUI()