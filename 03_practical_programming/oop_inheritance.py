class Animal:
    def __init__(self, species: str) -> None:
        self.species = species 
    
    def get_species(self) -> str:
        return self.species
    
    def speak(self) -> str:
        return ''
    
class Mammal(Animal):
    def __init__(self, species: str) -> None:
        self.species = species 
        self.num_eggs_laid = 0

    def get_num_eggs_laid(self) -> str:
        return self.num_eggs_laid

class Bird(Animal):
    def __init__(self, species: str, neggs: int) -> None:
        super().__init__(species)
        self.num_eggs_laid = neggs

    def get_num_eggs_laid(self) -> str:
        return self.num_eggs_laid
    
    def speak(self) -> str:
        return 'cheep'

class Dog(Mammal):
    def speak(self):
        return 'woof'


x = Mammal('Turtle')
print(f'{x.get_species() = }')
print(f'{x.num_eggs_laid = }')

bird = Bird('Parrot', 1)
print(f'{bird.get_num_eggs_laid() = }')

rufus = Dog('Labrador')
print(f'{rufus.speak() = }')
