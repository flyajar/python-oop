from Animal import Animal


class Cat(Animal):
    def __init__(self, sound: str):
        # this calls the methods and properties from the parent class
        super().__init__(sound)

    @staticmethod
    def purr():
        return 'purring'

    def activity(self):
        return 'loves to sleep'


fyodor = Cat('Meow')

print(fyodor.species)  # Animalia
print(fyodor.make_sound())  # Meow
print(fyodor.purr())
print(fyodor.activity())
