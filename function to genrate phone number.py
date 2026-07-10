# this is for the USA


def get_phone(country_code = +234, area_code = 0, first= 0, last=0):
    return f"{country_code}-{area_code}-{first}-{last}"

phone = get_phone(country_code= int(input("enter your country code: ")) ,area_code=int(input("enter your area code: ")),first=int(input("enter your first 3 digits: ")),last=int(input("enter your last e digits 4: ")) )
print(phone)