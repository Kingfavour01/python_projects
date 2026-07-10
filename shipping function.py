def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end= " ")
    print()
    for value in kwargs.values():
        print(value, end=" ") #you could also use an f string alongside the get method for you to  print this out
    print()

shipping_label("king ","favour ","I",
               street= "grace land",
               city= "cool",
               place= "stn james",
)