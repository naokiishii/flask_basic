# two.py

import one

print('Top level in two.py')

one.func()

if __name__ == '__main__':
  print('two.py is being run directly!')
else:
  print(f'two.py is imported. {__name__}')