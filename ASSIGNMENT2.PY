class Animal:
    def move(self):
        pass  

class Dog(Animal):
    def move(self):
        print("The dog is running ")

class Fish(Animal):
    def move(self):
        print("The fish is swimming ")

class Bird(Animal):
    def move(self):
        print("The bird is flying ")

class snake(Animal):
    def move (self):
        print("The snake is slithering")

# Polymorphism 
animals = [Dog(), Fish(), Bird(), snake()]
for animal in animals:
    animal.move()
