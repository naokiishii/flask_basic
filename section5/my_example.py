# Numbers and Variables
print('hello world')
print(2 + 1)
print(1 / 2)
print(1 - 2)
print(3 * 3)
print(2 ** 3)

a = 10
print(a)
a = a + a
print(a)

puppies = 6
weight = 2

total = puppies * weight
print(total)

# Strings
print('hello')
print(len('hello'))

mystring = 'hello'
print(mystring[0])
print(mystring[1])
print(mystring[-1])
print(mystring[-2])

print(mystring[0:3])
print(mystring[2:5])

mystring2='abcdefghijklmn'
print(mystring2[0:10:3])
print(mystring2[:5])
print(mystring2[5:])
print(mystring2[::2])
print(mystring2[::-1])
#mystring2[0] = 'z'  # TypeError: 'str' object does not support item assignment
print(mystring2 + mystring2)

mystring3 = 'AbCdEfG'
print(mystring3.upper())
print(mystring3.lower())

mystring4 = 'abcd,efgh'
print(mystring4.split(','))

username = 'Sammy'
color = 'blue'
print('The {} favorite is {}'.format(username, color))
## python 3.6 and above
print(f'The {username} chose {color}')

# Lists
mylist = [1, 2, 3]
print(mylist)
print(len(mylist))

mylist2 = [1, 1.03, 'hello']
print(mylist2)
print(mylist2[2])

mylist3 = ['a', 'b', 'c', 'd', 'e']
print(mylist3[1:4])
mylist3.append('f')
print(mylist3)
mylist3.insert(0, 'Z')
print(mylist3)
popped_item = mylist3.pop(0)
print(mylist3)
print(popped_item)

mylist_a = [1, 2, 3]
mylist_b = [4, 5, 6]
mylist_c = [7, 8, 9]
mega_list = [mylist_a, mylist_b, mylist_c]
print(len(mega_list))
print(mega_list)
print(mega_list[2])
print(mega_list[2][1])

# Dictionaries
print('### Dictionaries')
mydict = {'key1': 'value1', 'key2': 'value2'}
print(mydict)
print(mydict['key1'])
print(mydict.keys())
print(mydict.items())
print(mydict.values())

salary_dict = {'John': 20, 'Sally': 30, 'Sammy': 15}
print(salary_dict['Sally'])
salary_dict['Cindy'] = 100
print(salary_dict)
salary_dict['John'] = salary_dict['John'] + 40
print(salary_dict)

people_dict = {'John': [1, 2, 3], 'Sally': [40, 10, 30]}
print(people_dict['John'])
print(people_dict['Sally'][0])

people_dict2 = {'John': {'salary': 10, 'age': 30}}
print(people_dict2['John'])
print(people_dict2['John']['salary'])

# Tuples, Sets, Booleans
print('### Tuples')
mytuples = (1, 2, 3)
print(mytuples)
print(mytuples[0])

# mytuples[0] = 2 #TypeError: 'tuple' object does not support item assignment

mytuples2 = (1, 2, 3, 'a', 'b', 'c')
print(mytuples2)
print(mytuples2[0])

print('### Sets')
myset = set()
print(myset)
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)
myset.add(3)
myset.add(3)
print(myset)

myduplist = [1, 1, 1, 1, 2, 3, 4, 5, 5, 2, 1, 1, 1, 2]
print(set(myduplist))

print('### Booleans')
a = True
b = False
c = None
print(a)
print(b)
print(c)
print(1 < 2)

# Comparison and Logical Operators
print('### Comparisons')
print(1 > 2, 3 <= 2, 3 <= 3, 2 > 1, 3 == 3, 3 != 3)
username = 'Admin'
check = 'Admin'
print(username == check)
print( 1 == 1 and 2 < 3)
print( 1 == 2 and 2 < 3)
print( 1 == 1 or 2 < 3)
permission = False
print(username == check and permission)
print(username == check or permission)

# If Elif and Else Statements in Python
print('### If - Elif - Else')
user_name = 'admin'
check_name = 'admin'
if 1 < 2:
  print('Yep!')

#if user_name == check_name:
if user_name != check_name:
  print('Access Granted!')
elif 1 == 3:
  print('Middle condition true!')
elif 1 == 2:
  print('Third condition true!')
else:
  print('All above conditions, were not true!')
  
# While Loops and For Loops in Python
print('### For')
my_seq = [1, 2, 3, 4, 5]
for item in my_seq:
  print(item, item ** 2)
  
my_seq_str = 'hello'
for char in my_seq_str:
  print(char)

my_seq_salaries = {'John': 10, 'Sally': 20, 'Lisa': 30}
for employee in my_seq_salaries:
  print(employee, my_seq_salaries[employee])

## Tuple unpacking
my_pairs = [('a', 1), ('b', 2), ('c', 3)]
for (letter, num) in my_pairs:
  print(letter, num)

print('### While')
w_i = 1
while w_i < 5:
  print(f'index is currently: {w_i}')
  w_i = w_i + 1

for x in range(0, 5):
  print(x)

for x in range(0, 11, 2):
  print(x)

my_range = range(0, 11, 2)
print(my_range)

print('s' in 'abcdefghijklmn')
print('a' in 'abcdefghijklmn')
print(1 in [1, 2, 3, 4, 5])

# Functions in Python Part One
print('### Function Part One')
def report_person():
  print('reporting person!')

report_person()

def report_person_name(name = 'BLANK'):
  print(f'reporting {name}!')

report_person_name('Cindy')
report_person_name()

def add_num(num1, num2):
  print(f'add_num: {num1 + num2}')
  return num1 + num2

add_result = add_num(2, 4)
print(add_result)
print(add_result + 10)

print('### Function Part Two')
## max and min
print(max(2, 4))
print(max([1, 2, 3, 4, 5, 6]))

## enumerate
my_letters = ['a', 'b', 'c']
letter_index = 0
for letter in my_letters:
  print(f'{letter} is at index: {letter_index}')
  letter_index = letter_index + 1

for index, item in enumerate(my_letters):
  print(f'{item} is at index: {index} enumerate')
  
## .join
my_chars = ['a', 'b', 'c', 'd']
print(''.join(my_chars))
print('-->'.join(my_chars))

## string check
def secret_check(mystring):
  # return 'secret' in mystring.lower()
  if 'secret' in mystring.lower():
    return True
  else:
    return False

print(secret_check('simple'))
print(secret_check('this is a secret.'))
print(secret_check('this is a Secret.'))

## code check
def code_maker(mystring):
  output = list(mystring)
  for index, letter in enumerate(mystring):
    for vowel in 'aeiou':
      if letter.lower() == vowel:
        output[index] = 'x'
  output = ''.join(output)
  return output

print(code_maker('Sammy'))
print(code_maker('Adam'))