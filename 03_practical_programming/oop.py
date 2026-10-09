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
