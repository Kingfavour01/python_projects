# temperature converter from Celsius to Fahrenheit and Kelvin


temp , unit =  float(input(f"enter the temperature: ") ), str.lower(input(f"enter the unit of measurement Celsius(C)/kelvin (K)/Fahrenheit (F) : ") )
if unit == "c" or unit == "Celsius":
    Formula_1 = ( temp * 9 / 5) + 32 # convert c to f
    Formula_2 =  temp - 273.15  # convert c to k
    print(f"the temp in Fahrenheit is {Formula_1}°f and in kelvin is {Formula_2}°k ")
    print('Celsius function is called')
elif unit == "f" or unit == "Fahrenheit":
    Formula_3 = (temp - 32) * 5/9 # convert f to c
    Formula_4 = (temp - 32) * 5/9 + 273.15 # convert f to k
    print(f"the temp in Celsius is {Formula_3}°c and in kelvin is {Formula_4}°k ")
    print('Fahrenheit function is called')
elif unit == "k" or unit == "kelvin":
    Formula_5 = temp + 273.15 # convert k to c
    Formula_6 = (temp- 273 * (9/5)+32 ) # convert k to f
    print(f"the temp in  Celsius is {Formula_5}°c and in kelvin is {Formula_6}°f ")
    print('Kelvin function is called')
else:
    print(f"This {unit}is not a proper unit to measure temp  ")

print('This is the end of the function')