# {'name': 'JP', 'age': 28, 'city': 'Bangalore'}

class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display_info(self):
       print(f'Name: {self.name}, Age: {self.age}, City: {self.city}')
    def greeetings(self):
        return f'Hello {self.name}.Welcome to {self.city}.'

s1 = Student("JP", 28, "Bangalore") # creating a object of the class Student and passing the values to the constructor
s2 = Student('Amy', 25, 'New York')

print(s1.display_info())
print(s2.display_info())
print(s2.greeetings())

print('===================')

# i want to see how many objects are there 
object_list =[]
object_list.append(s1)
object_list.append(s2)

for o in object_list:
    print(o.display_info())
    print(o.greeetings())

# class: keyword that start a brand new blueprint defination-- BOILERPLATE for creating objects of the class

# __init__: constructor method that is called when an object of the class is created- constructing the object
# you dont have to do Student.__init__ ----- it is a special method/function 

# when youa re calling the object , you pass the parameters to instrcutor - calling the calss & after that once object 
#                     is created , you can call different methods of the class using the object

# OBJECT -  Instances of the class , for every class you can gonna create objects

# self :  its a python inbuilt capability, filled by python. Refersto the current object of the class
#         self is a reference to the current object of the class