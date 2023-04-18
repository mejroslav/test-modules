class Dinosaur:
    def __init__(self, name) -> None:
        self.name = name

    def call(self):
        print("Hi, I'm {}".format(self.name))
