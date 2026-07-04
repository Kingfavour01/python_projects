# weight comverter from lb to kg and back
weight = float(input(f"input your weight: "))
unit = str.lower(input (f"chose between lb/kg: "))
weight_convertion = 2.205

if unit == "lb":
    new_weight = round(weight/weight_convertion , 3 )
    print(f"you weigh {new_weight} kg 😊 ")
elif unit == "kg":
    new_weight = round (weight *weight_convertion , 3)
    print(f" you weigh {new_weight} lb 😊")
else:
    print (f"{unit} this is not a recognised unit ")




