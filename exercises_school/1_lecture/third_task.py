
def check_name_validity():
    user_name = input("Ahoj, jak se jmenuješ? ")
    answer = input(f'Opravdu se jmenuješ {user_name}? ano/ne')
    if answer == "ano":
        return True
    else:
        return False


is_name_valid = check_name_validity()
while not is_name_valid:
    is_name_valid = check_name_validity()

