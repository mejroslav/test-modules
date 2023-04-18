import my_module

stegosaur = my_module.Dinosaur("stegosaur")
cat = my_module.Animal("Quída", "cat")

if __name__ == "__main__":
    cat.call()
    stegosaur.call()
    print(my_module.ZOO)
