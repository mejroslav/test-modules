from .animals import Animal, ZOO
from .dinosaurs import Dinosaur

__all__ = [
    "Animal", "Dinosaur", "ZOO"
]

print("Načítám modul {}".format(__name__))

x = 21

print("Konečná odpověď je: {}".format(x*2))