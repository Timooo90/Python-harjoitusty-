class CinemaHall():
    def __init__(self, name: str = "no name", seats: int = 0, shows: list = []):
        self.__name = name
        self.__seats = seats
        self.__shows = shows
    

    def __str__(self):
        return(f"{self.__name}, paikkoja {self.__seats}")
    

    def form_dictionary_from_self(self):
        return {"Nimi": self.__name, "Paikkoja": self.__seats, "Näytökset": self.__shows}
    
    
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