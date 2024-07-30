

def say_name(self) -> None:
        print(f'Hi! I am {self.name} and I am {self.age} years old.')

def set_age(self, age: int) -> None:
        self.age = age

bob = Person('Boris', 34)

bob.say_name()
bob.set_age(25)
bob.say_name()

