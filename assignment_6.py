# # 10 questions about classes, objects, inheritance, polymorphism, queues, stacks, and more

# 1. create a credit card class with the following attributes: card number, expiration date, and security code.
#  Create a method that will print out the card number, expiration date, and security code. Create an instance of 
# the class and call the method.

from ctypes import addressof
from curses import ACS_GEQUAL
from queue import Queue
from unicodedata import name


class credit_card:
    def __init__(self, card_number, expiration_date, security_code):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.security_code = security_code

    def card_details(self):
        return( f"<credit_card is {self.card_number} expires on {self.expiration_date} with access code {self.security_code}>")
my_credit_card = credit_card("202219800056", "01.01.2025", "071715")
print(my_credit_card.card_details())
    


# 2. create Animal class and Dog class. Make the Dog class inherit from the Animal class. Add a bark method to the 
# Dog class. Create an instance of the Dog class and call the bark method.

class Animal:
    def __init__(self):
        print("Animal is a mammal")
   
class Dog(Animal):
    def __init__(self, sound) -> None:
        super().__init__(name, sound)
    def bark(self):
        return(f"The big {self.name} {self.sound} at at people everyday")

dog = Dog('Germanshepherd' , 'barks')
        Print(dog.bark)



# 3. create a class called Queue. The class should have the following methods: enqueue, dequeue, and size. 
# The enqueue method should add an item to the queue. The dequeue method should remove an item from the queue. 
# The size method should return the size of the queue.

Class queue:
    def __init__(self):
        self.items = []

    def isFull(self):
        len(self.items) > 0
        return("The list is full")

    def isEmpty(self):
        len(self.items) == 0
        return("The list is empty")

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item) #(1,2,3,4,5,6)
        return self.items

    def size(self):
        return len(self.items)

    def dequeue(self):
        self.items.pop(0)
        return self.items

    def display(self):
        return self.items

new_queue_instance = queue()
new_queue_instance.enqueue(6)
new_queue_instance.enqueue(5)
new_queue_instance.enqueue(4)
new_queue_instance.enqueue(3)
new_queue_instance.enqueue(2)
print(new_queue_instance.display())
print(new_queue_instance.size())
new_queue_instance.dequeue()
new_queue_instance.dequeue()
new_queue_instance.dequeue()
new_queue_instance.dequeue()
new_queue_instance.dequeue()
print(new_queue_instance.display())
print(new_queue_instance.size())

# 4. create a class called Stack. The class should have the following methods: push, pop, and size. 
# The push method should add an item to the stack. The pop method should remove an item from the stack. 
# The size method should return the size of the stack.


class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        return self.items
    def pop(self):
        self.items.pop(0)
        return self.items

    def size(self):
        return len(self.items)

    def display(self):
        return self.items

instance = stack()
instance.push(Jonathan)
instance.push(Oscar)
instance.push(Lowine)
print(instance.size())
print(instance.display())
print(instance.pop())

# 5. create a class called Person. The class should have the following attributes: name, age, and address. 
# The class should have the following methods: eat, sleep, and work. 
# The eat method should print out the name of the person and the word "is eating". 
# The sleep method should print out the name of the person and the word "is sleeping". 
# The work method should print out the name of the person and the word "is working".

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

    def work(self):
        return f"{self.name} is working."
    
person = Person("Lowine", "23", "Oregon")
print(person.eat())
print(person.sleep())
print(person.work())
    



# 6. create a class called Employee. The class should have the following attributes: name, age, and salary. 
# The class should have the following methods: eat, sleep, and work. 
# The eat method should print out the name of the person and the word "is eating". 
# The sleep method should print out the name of the person and the word "is sleeping". 
# The work method should print out the name of the person and the word "is working". 
# Create a subclass of Employee called Programmer. The Programmer class should have the following attributes: 
# name, age, salary, and programming language. The Programmer class should have the following methods: eat, sleep, 
# work, and code. The code method should print out the name of the person and the word "is coding in" 
# and the programming language. Create an instance of the Programmer class and call all the methods.

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"

    def work(self):
        return f"{self.name} is working"

class Programmer(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"

    def work(self):
        return f"{self.name} is working"

    def code(self):
        return f"{self.name} is coding"

employee = Employee("Iden", "35", "5000000")
print(employee.eat())
print(employee.sleep())
print(employee.work())
programmer = Programmer("Claire", "42", "5000000")
print(programmer.code())
print(programmer.eat())
print(programmer.sleep())
print(programmer.work())

# 7. create a class called Vehicle. The class should have the following attributes: make, model, and year. 
# The class should have the following methods: start, stop, and drive. The start method should print out the make, 
# model, and year of the vehicle and the word "is starting". The stop method should print out the make, model, and 
# year of the vehicle and the word "is stopping". The drive method should print out the make, model, and year of the 
# vehicle and the word "is driving". Create a subclass of Vehicle called Car. The Car class should have the following 
# attributes: make, model, year, and color. The Car class should have the following methods: start, stop, drive,
#  and park. The park method should print out the make, model, year, and color of the car and the word "is parking". 
# Create an instance of the Car class and call all the methods.
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return(f"The release of the {self.make} {self.model} {self.year} model is starting later this year.")

    def stop(self):
        return(f"The release of the {self.make} {self.model} {self.year} model is stopping later this month.")
    
    def drive(self):
        return(f"The Company CEO is driving a {self.make} {self.model} {self.year} model.")

class Car(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year)
        self.color = color

    def start(self):
        return(f"Start the engine of the {self.color} {self.make} {self.model} {self.year} model right before you.")

    def stop(self):
        return(f"Stop the engine of the {self.color} {self.make} {self.model} {self.year}model right before you.")

    def drive(self):
        return(f"I took my {self.color} {self.make} {self.model} {self.year} model for a test drive around my yard.")

    def park(self):
        return(f"The chauffer is parking the boss' {self.color} {self.make} {self.model} {self.year} vehicle in the VIP parking area.")

vehicle = Vehicle("Range Rover", "Sport", "2020")
print(vehicle.start())
print(vehicle.stop())
print(vehicle.drive())

car = Car("Toyota", "Fortuner", "2020", "Black")
print(car.start())
print(car.stop())
print(car.drive())
print(car.park())

# 8. create a class called Animal. The class should have the following attributes: name, color, and age. 
# The class should have the following methods: eat, sleep, and make_sound. The eat method should print out the name of
#  the animal and the word "is eating". The sleep method should print out the name of the animal and the word 
# "is sleeping". The make_sound method should print out the name of the animal and the word "is making a sound". 
# Create a subclass of Animal called Dog. The Dog class should have the following attributes: name, color, age, and 
# breed. The Dog class should have the following methods: eat, sleep, make_sound, and bark.
#  The bark method should print out the name of the dog and the word "is barking". 
# Create an instance of the Dog class and call all the methods.

class Animal:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def eat(self):
        return(f"The {self.name} is eating.")

    def sleep(self):
        return(f"The {self.name} is sleeping.")

    def make_sound(self):
        return(f"The {self.name} is making a sound.")

class Dog(Animal):
    def __init__(self, name, color, age, breed):
        super().__init__(name, color, age)
        self.breed = breed

    def eat(self):
        return(f"{self.name} is eating.")

    def sleep(self):
        return(f"{self.name} is sleeping.")

    def make_sound(self):
        return(f"{self.name} is making a sound.")

    def bark(self):
        return(f"{self.name} is barking.")

animal = Animal("cow", "brown", "6")
print(animal.eat())
print(animal.sleep())
print(animal.make_sound())

dog = Dog("Mickie", "brown", "6", "Germa Shepherd")
print(dog.eat())
print(dog.sleep())
print(dog.make_sound())
print(dog.bark())



# 9. create a class of your choice. It should have at least 3 attributes and 3 methods where one of the methods is a static method. Implement polymorphism, encapsulation, and inheritance.

class Phones:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __repr__(self):
        return(f"This is a {self.color} {self.brand}.")

    # Inheritance
class Tecno(Phones):
    def __init__(self, brand, color, model, version):
        super().__init__(brand, color)
        self.__version = 14
        self.model = model

    def __repr__(self):    
        return(f"This is a {self.color} {self.brand} {self.model}.")

    # encapsulation.
    def get_version(self):
        return self.__version

    def update_version(self, version):
        self.__version = version
        return version

    # ploymorphism.
class Infinix(Phones):
    def __init__(self, brand, color, model, year_of_make: int, current_year: int):
        super().__init__(brand, color)
        self.model = model
        self.year_of_make = year_of_make
        self.current_year = current_year

    def how_old_is_phone(self):
        return(self.current_year - self.year_of_make)
            

phone = Phones('Samsung', 'White')
print(phone)

# inheritance and encapsulation.
tecno = Tecno("Tecno", "blue", "Camon", "15")
print(tecno)
print(tecno.get_version())
print(tecno.update_version(16))

# ploymorphism.
infinix = Infinix("infinix", "Note", "10", 2019, 2022)
print(infinix.how_old_is_phone())
