# Implement the concept of inheritance using Python.

class Animal:
    def eat(self):
        print("Animal is eating:")

class Dog(Animal):
    def bark(self):
        print("dog is barking")

d = Dog()
d.eat()
d.bark()    
       