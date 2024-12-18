# Nested Statements and Scope
print('### Scope')

x = 'outside'

def report():
  # grab the global level 'x' variable
  # global x

  # local assignment
  x = 'inside'
  return x

print(report())
print(x)

def enclosing():
  x = 'enclosing level'
  def inside():
    #x = 'local level'
    print(x)
  inside()

enclosing()

"""
Python search order (LEGB rule)
1. Local
2. Enclosing
3. Global
4. Built in
"""

# Object Oriented Programming - Part One
print('### Object Oriented Programming - Part One')

mylist = [1, 2, 3]
mylist.append(4)
print(type(mylist))

class Sample():
  pass

oop_x = Sample()
print(type(oop_x))

class Dog():
  # class object attributes
  species = 'mammal'
  
  def __init__(self, breed, name):
    self.breed = breed
    self.name = name

oop_sam = Dog('lab', 'Sammy')
print(type(oop_sam), type(oop_sam.breed), oop_sam.breed, oop_sam.name, oop_sam.species)
oop_joe = Dog(breed = 'Huskie', name = 'Joe')
print(oop_joe.breed, oop_joe.name, oop_joe.species)

print('### Object Oriented Programming - Part Two')

class Circle():
  
  pi = 3.14
  
  def __init__(self, radius = 1):
    self.radius = radius
  
  def area(self):
    return self.radius ** 2 * self.pi
  
  def circumfrence(self):
    return 2 * self.pi * self.radius
  
mycircle_default = Circle()
print(mycircle_default.radius)

mycircle_ten = Circle(10)
print(mycircle_ten.radius)
print(mycircle_ten.area())
print(mycircle_ten.circumfrence())

class Animal():
  
  def __init__(self, fur):
    self.fur = fur
    print('Animal Created!')
  
  def report(self):
    print('Animal')
  
  def eat(self):
    print('Eating!')

oop_animal = Animal('fur')
oop_animal.eat()
oop_animal.report()

class Cat(Animal):
  def __init__(self, fur):
    Animal.__init__(self, fur)
    print('Cat Created!')
  
  def report(self):
    print('I am a cat!')


my_cat = Cat('Fuzzy')
my_cat.eat()
my_cat.report()
print(my_cat.fur)

## Special Method
print('### Object Oriented Programming - Part Three')

class Book():
  
  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages
  
  def __repr__(self): # def __str__(self):
    # representation -> print
    return f'Title: {self.title}, Author: {self.author}'
  
  def __len__(self):
    return self.pages

my_book = Book('Python Rocks!', 'Jose', 250)
print(my_book)
print(len(my_book))

## Decorators Overview
print('### Object Oriented Programming - Part Three')

def hello(name = 'Jose'):
  print('the hello() func has been run')
  
  def greet():
    return '  This is inside the greet()'
  
  def welcome():
    return '  This is inside welcome()'
  
  print(greet())
  print(welcome())
  
  if name == 'Jose':
    return greet
  else:
    return welcome

# dec_x = greet
dec_x = hello()
# greet()
print(dec_x())

dec_y = hello(name = 'Sammy')
print(dec_y())

### decorators
def hello_dec():
  return 'Hi Jose'

def other_dec(func):
  print('Some other code')
  # Assume that func passed in is a function!!!
  print(func())

other_dec(hello_dec)

def new_decorator(func):
  
  def wrap_func():
    print('some code before executing func')
    func()
    print('Code here, after executing func()')
  
  return wrap_func

@new_decorator # func_needs_decorator = new_decorator(func_needs_decorator)
def func_needs_decorator():
  print('Please decorate me!!')

func_needs_decorator()

## Pip Install and PyPi
print('### Object Oriented Programming - Part Three')
