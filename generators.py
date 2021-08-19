# Python is mainly composed of objects
# From classes to strings to integers and lists, all of ese are 
# objects. Surprisignly a class is also included as an object though 
# we do know that it actually is a template or blueprint to making an object. 
# But how so?
class Foo:
    pass

def make_func():
    s= 17
    t = "gibberish"
    return 
print(type(Foo()))
print(type(Foo))
# The results return Foo as an object of class 'type'
# lets try with a string and an integer
print(type(4))
print(type("Bobby"))
print(type([1,2,3]))
print(type(make_func))
# They portray that they are all instances of a certain class
# But are those classes the superclasses? You may be surprised 
# what these statements will print out
print(type(int))
print(type(str))
print(type(list))
print(type(type))
# What this basically means is that all these other classes, whether we create 
# custom classes or they are built-in, they all inherit from the super class TYPE 
# HOW CAN THIS REVOLUTIONIZE HOW WE APPROACH CLASSES AND BUILD THEM?

x= type("Person", (), {'name': 'Jarib', 'age':20})
print(x.name)
# The code above is exactly the same as the code below
# since we already know that any class are objects of the class type 
# we can create our class as an instance of the type class like so above.
class Person:
    name = 'Jarib'
    age = 20

print(Person.age)

# But we can do better than that. We can infact create our own Meta classes 
# that aren't necessarily objects of the type class, in short, a MetaClass!
# Let's do it
# we inherit from the type metaclass because we want to change some unique mthods in it.
class School(type):
    def __new__(self, class_name, bases, attrs):
        # This function is ussually the very first that is called when we create an object
        # of any class, even before the __init__ function.
        # It describes the class as a whole. It particularly important  especially 
        # if we would like to use it to create other classes or inherited by other classes
        # There is alot of what we can do in this function 
        print(attrs)
        return type(class_name, bases, attrs)
    def __init__(self):
        pass

# Let's now create a class and instead of having its metaclass as originally `type` 
# let's make the metaclass our own metaclass that we defined up there 

class Student(metaclass=School):
    gpa = 4.0
    course = 'Comp SCience'

# The output was portrayed because we defined it in our metaclass line 53
# That means our metaclass can have an influence on how our class Student works
# since it borrows from metaclass School

