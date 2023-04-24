from Animal import Animal


class Cat(Animal):
    def __init__(self, sound: str):
        # this calls the methods and properties from the parent class
        super().__init__(sound)

    pass


fyodor = Cat('Meow')

print(fyodor.species)  # Animalia
print(fyodor.make_sound())  # Meow
