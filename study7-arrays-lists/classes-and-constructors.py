### CLASSES AND CONSTRUCTORS
# (Just a small taste into Object Oriented Programming with Python)

'''
In Python, you can use constructors to create objects from a class. 
Constructors are special methods within a class that are automatically called when an object of that class is created. 
The most common constructor in Python is the __init__() method, which initializes the object's attributes.

To define your own constructor in a class, you need to define a method with the name __init__(). 
This method will be automatically called when creating an object of that class.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object of the Person class using the constructor
person1 = Person("John", 25)
print(person1.name)  # Output: John
print(person1.age)   # Output: 25
person1.greet()  # Output: Hello, my name is John and I am 25 years old.

'''
In the example above, the Person class has a constructor that takes two parameters (name and age) and a method (greet()). 
The constructor initializes the name and age attributes of the object. 
When creating an object of the Person class, we pass the values for name and age to the constructor (__init__() method), 
and the object is initialized with those attributes.
We can then call the greet() method on the object, which accesses and uses the object's attributes.

You can define your own constructors with different names as well, but it's recommended to use 
the standard __init__() method for clarity and consistency with other Python classes.


In Python, you can create objects using classes, which provide a way to define data structures with attributes and methods. 
Classes in Python serve a similar purpose to structs in C and other languages from the C family, but they offer more flexibility and functionality.

A class in Python can have attributes (variables) and methods (functions). 
You can define attributes to hold data associated with the object, and methods to perform operations or actions on that data. 
Classes encapsulate related data and functionality into a single entity.
'''
