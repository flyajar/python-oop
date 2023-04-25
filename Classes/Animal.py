class Animal:
    species: str = 'Animalia'

    def __init__(self, sound: str):
        self.sound = sound

    def make_sound(self):
        return self.sound
