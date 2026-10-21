# from the slides:
class Student:
    def __init__(self, name: str, grades: list[float]) -> None:
        self.name = name
        self.grades = grades
 
    def average(self) -> float:
        return sum(self.grades) / len(self.grades)
 
s1 = Student("Maya", [88, 92, 75])
s2 = Student("Carla", [88, 92, 75])
print(f'{s1.name = }')         # Maya
print(f'{s1.average() = }')    # 85.0

class Cat:
    def __init__(self, name: str, breed: str) -> None:
        self.__name: str = name 
        self.__breed: str = breed 
    
    def meow(self) -> str:
        return f'{self.__name}: Meow!'

    # information hiding
    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> str:
        self.__name = name

lenny: Cat = Cat('Lenny', 'Maine Coon?')
# print(f'{lenny.__name = }')
print(f'{lenny.get_name() = }')
print(f'{lenny.meow() = }')
