class Car:

    def __init__(self, color: str, mileage: int):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."

blue = Car('blue', 20000)
print(blue)