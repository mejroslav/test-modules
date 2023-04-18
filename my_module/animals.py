class Animal:
    def __init__(self, name, kind) -> None:
        self.name = name
        self.kind = kind

    def call(self):
        print("Hi! My name is {} and I'm a {}".format(self.name, self.kind))


ZOO = "Zoo Praha"
