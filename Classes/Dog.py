from Animal import Animal


class Dog(Animal):
    def __init__(self, sound: str):
        super().__init__(sound)

    def activity(self):
        return 'loves to run'


primo = Dog('Woof')
print(primo.make_sound())
print(primo.activity())