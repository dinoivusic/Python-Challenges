class Pets:
    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())


class Dog:
    species = 'Mammal'
    is_hungry = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return 'My name is {} and I am {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}'.format(self.name, sound)

    def eat(self):
        self.is_hungry = False

    def walk(self):
        return '{} is walking'.format(self.name)


class Lab(Dog):

    def run(self, speed):
        return '{} runs {} kmh'.format(self.name, speed)


class Terrier(Dog):

    def run(self, speed):
        return '{} runs {} kmh'.format(self.name, speed)


dogs = [Lab('Fido', 6), Terrier('Labs', 3), Lab('Tip', 87)]

my_pets = Pets(dogs)

# Output
print("I have {} dogs.".format(len(my_pets.dogs)))
for dog in my_pets.dogs:
    dog.eat()
    print('{} is {} years old'.format(dog.name, dog.age))

print('And they are all {}s'.format(Dog.species))

dogs_hungry = False
is_walking = False
for dog in my_pets.dogs:
    if dog.is_hungry:
        dogs_hungry = True
if dogs_hungry:
    print('Yes my dogs are hungry')
else:
    print('My dogs are not hungry')
my_pets.walk()
