from datetime import datetime
from films import Films

class Show():
    def __init__(self, start_time: datetime, film: Films.Film):
        self.__start_time = start_time
        self.__film = film
    
    def __str__(self):
        return f"{self.__film.get_name()}. Alkaa {self._start_time}, loppuu {self.__end_time}"