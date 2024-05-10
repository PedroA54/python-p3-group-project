import ipdb


class Dog:
    def __init__(self, name, breed, id=None):
        self.id = id
        self.name = name
        self.breed = breed


Dog(name="Sparky", breed="poodle")
ipdb.set_trace()
