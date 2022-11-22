from datetime import date
from datetime import timedelta

from settings import Settings

def string_to_int(value: str) -> int:
    if isinstance(value, int):
        return value

    try:
        value = int(value)
    except:
        print("Virhe. Syöte ei ole kokonaisluku.")
    
    return value

def is_integer(value: str):
    value = string_to_int(value)

    if isinstance(value, int):
        return True

    return False

def is_integer_and_at_least_zero(value: str):
    value = string_to_int(value)

    if isinstance(value, int):
        if value >= 0:
            return True
        else:
            print("Luku on negatiivinen.")
    
    return False

def ask_user_to_input_a_name() -> str:
    while True:
        name = input()

        if len(name) < 100:
            break
        else:
            print("Liian pitkä. Raja 100 merkkiä.")
    
    return name

def ask_user_to_input_number_zero_or_over() -> int:
    while True:
        number = input()

        number = string_to_int(number)

        if not isinstance(number, int):
            continue

        if is_integer_and_at_least_zero(number):
            return number

def ask_command_from_user() -> str:
    return input("Anna komento: ")


def ask_date_from_user() -> date:
    Settings.print_select_date_options(Settings())

    while True:
        command = ask_command_from_user()

        if command == "0":
            return date.today()
        elif command == "1":
            tomorrow = date.today() + timedelta(hours=24)
            return tomorrow
        elif command == "2":
            return get_manual_date_input()

def get_manual_date_input():
    while True:
        print("Vuosi: ")
        year = ask_user_to_input_number_zero_or_over()
        if year < Settings.get_last_acceptable_year(Settings()):
            break
        else:
            print("Vuosi on liian kaukana tulevaisuudessa.")
    
    while True:
        print("Kuukausi: ")
        month = ask_user_to_input_number_zero_or_over()
        if month <= 12:
            break
        else:
            print("Kuukautta ei ole olemassa.")
    
    while True:
        print("Päivä: ")
        day = ask_user_to_input_number_zero_or_over()

        if day <= 31:
            if check_if_day_is_valid_in_given_month(day, month, year):
                break

        print("Päivää ei ole olemassa.")
    
    return date(year, month, day)


def check_if_day_is_valid_in_given_month(day: int, month: int, year: int) -> bool:
    days_30 = [4, 6, 9, 11]
    if month in days_30:
        if day <= 30:
            return True

    elif month == 2:
        if is_leap_year(year):
            if day <= 29:
                return True
            else:
                return False

        elif day <= 28:
            return True
        else:
            return False
    else:
        return True


def is_leap_year(year) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


    #################################################################
    # For testing purposes
    #################################################################
if __name__ == "__main__":
    number_testing = False
    date_testing = True

    while number_testing:
        luku = input("Anna luku: ")
        print("---------------------------")
        print(f"Kokonaisluku: {is_integer(luku)}")
        print("---------------------------")
        print(f"Nolla tai yli: {is_integer_and_at_least_zero(luku)}")
        print("---------------------------")
        print("")
    

    while date_testing:
        print(ask_date_from_user())

        #year = int(input("Vuosi: "))
        #print(is_leap_year(year))