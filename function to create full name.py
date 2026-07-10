def full_name(first_name,last_name):
    first = first_name.capitalize()
    last = last_name.capitalize()
    name = first + " " + last

    return name

full_name(str(input("enter your first name: ")),str(input("enter your last name: ")))