# one.py
def func():
  print('func() in one.py')

print('Top level in one.py')

## if this file is executed directly
if __name__ == '__main__':
  print('one.py is being run directly!')
else:
  print(f'one.py has been imported! {__name__}')