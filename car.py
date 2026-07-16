class car:
    def __init__(self, model, colour, year, for_sale):
        self.model = model
        self.colour = colour
        self.year = year
        self.for_sale = False

    def drive(self):
        print(f"{self.model}car is driving")

    def parked(self):
        print(f"this {self.model}car the has stopped")

    def available(self):
        print(f"this {self.model} car is available")

    def spec(self):
        print(f"{self.model}, {self.colour}, {self.year}")
