def is_day(day1):
    match day1:
        case 1:
         print("it is monday ")
        case 2:
         print("it is tuesday")
        case 3:
         print("it is wednesday ")
        case 4:
         print("it is Thursday ")
        case 5:
         print("it is friday")
        case 6:
          print("it is saturday")
        case 7:
           print("it is sunday ")
        case _:
          print("invalid input")



def is_weekend(day):
    match day:
        case "monday"|"tuesday"|"wednesday"|"Thursday"|"friday":
         return False
        case "Saturday" | "sunday":
         return True
        case _:
         return "invalid input"

is_day(int(input("enter the day of the week: ")))
is_weekend(str(input("enter the day of the week: ")))

