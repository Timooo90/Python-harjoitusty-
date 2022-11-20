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

def ask_user_to_input_number_over_zero() -> int:
    while True:
        number = input()

        number = string_to_int(number)

        if not isinstance(number, int):
            continue

        if is_integer_and_at_least_zero(number):
            return number

if __name__ == "__main__":
    while True:
        luku = input("Anna luku: ")
        print("---------------------------")
        print(f"Kokonaisluku: {is_integer(luku)}")
        print("---------------------------")
        print(f"Nolla tai yli: {is_integer_and_at_least_zero(luku)}")
        print("---------------------------")
        print("")