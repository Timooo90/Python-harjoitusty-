import json

from datetime import datetime
from datetime import timedelta
from films import Films

class Show():
    def __init__(self, start_time: datetime, film: Films.Film):
        self.__start_time = start_time
        self.__film = film
        self.__end_time = self.get_end_time()
    
    def __str__(self):
        return f"{self.__film.get_name()}. Alkaa {self.__start_time}, loppuu {self.__end_time}"
        
    def get_end_time(self):
        runtime = self.__film.get_runtime()
        end_time = self.__start_time + timedelta(minutes=runtime)

        return end_time


    



    #################################################################
    # For testing purposes (datetime is killing me)
    #################################################################

if __name__ == "__main__":
    film1 = Films.Film("Leffa", "Ohjaajanaattori", 105, 10)

    show1 = Show(datetime(2022, 11, 22, 12, 30, 0, 0), film1)


    print(show1.get_end_time())