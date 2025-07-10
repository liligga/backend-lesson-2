class Animal:
    def __init__(self) -> None:
        pass

    def say(self):
        raise NotImplementedError
    
    def move(self):
        raise NotImplementedError


class Dog:
    def __init__(self) -> None:
        pass

    def say(self):
        print("Гав")

    def move(self):
        print("Бегу")

def main():
    d1 = Dog()
    d1.say()
    d2 = Dog()
    d2.say()