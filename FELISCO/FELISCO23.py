class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def wrapper():
            print("Introducing")
            func()
            print(f"{self.name} is cool!")
        return wrapper

tan = AnimeCharacter("Tanjiro", "Sun Breathing")

@tan.introduce
def character_intro():
    print(f"I am {tan.name} and I can use {tan.ability}.")

character_intro()