from flask import Flask

app = Flask(__name__)

@app.route('/') # 127.0.0.1:5000
def index():
  return '<h1>Hello Puppy!</h1>'

@app.route('/information')  #127.0.0.1:5000/information
def info():
  return '<h1>Puppies are cute!</h1?'

@app.route('/puppy/<name>')
def puppy(name):
  return f'<h1>This is a page for {name} and 10th letter is {name[9]}</h1>'

# spotty -> spottiful, spot -> spoty
@app.route('/puppy_latin/<name>')
def puppy_latin(name):
  latin_name = ''
  if name[-1] != 'y':
    latin_name = name + 'y'
  else:
    latin_name = name[:-1] + 'iful'
  return f'<h1>This is a page for {name} and its latin name is {latin_name}.</h1>'

if __name__ == '__main__':
  app.run(debug=True)