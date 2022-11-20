def string_to_int(value):
    try:
        value = int(value)
    except:
        print("Virhe. Syöte ei ole kokonaisluku.")
    
    return value

def is_integer(value):
    value = string_to_int(value)

    if isinstance(value, int):
        return True

    return False

def is_integer_and_at_least_zero(value):
    value = string_to_int(value)

    if isinstance(value, int):
        if value >= 0:
            return True
    
    return False




if __name__ == "__main__":
    while True:
        luku = input("Anna luku: ")
        print("---------------------------")
        print(f"Kokonaisluku: {is_integer(luku)}")
        print("---------------------------")
        print(f"Nolla tai yli: {is_integer_and_at_least_zero(luku)}")
        print("---------------------------")
        print("")