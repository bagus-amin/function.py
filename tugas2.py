class Rhino(Animal):
    def __init__(self, name, habitat, horn_size=0):
        super().__init__(name, "Plants", habitat, "Vivipar")
        self.horn_size = horn_size

    def grow_horn(self, size):
        self.horn_size += size
        print(f"{self.name}'s horn size is now {self.horn_size} inches.")

class Fish(Animal):
    def __init__(self, name, habitat, fins=2):
        super().__init__(name, "Plankton", habitat, "Ovipar")
        self.fins = fins

    def swim(self):
        print(f"{self.name} is swimming.")

class Snake(Animal):
    def __init__(self, name, habitat, length=0):
        super().__init__(name, "Small animals", habitat, "Ovipar")
        self.length = length

    def grow(self, length):
        self.length += length
        print(f"{self.name}'s length is now {self.length} inches.")

# Contoh penggunaan
rhino = Rhino("Rhino1", "Savannah")
rhino.grow_horn(10)

fish = Fish("Fish1", "Ocean")
fish.swim()

snake = Snake("Snake1", "Forest")
snake.grow(20)
