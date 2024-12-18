from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    some_variable = 'Jose'
    letters = list(some_variable)
    pup_dictionary = {'pup_name': 'Sammy'}
    my_list = [1, 2, 3, 4, 5]
    puppies = ['Fluffy', 'Rufus', 'Spike']
    return render_template('basic.html', my_variable=some_variable, letters=letters, pup_dictionary=pup_dictionary, my_list = my_list, puppies=puppies)


@app.route('/home')
def home():
  return render_template('home.html')


@app.route('/home/puppy/<name>')
def pup_name(name):
  return render_template('puppy.html', name=name)


@app.route('/form/')
def form_index():
  return render_template('form_index.html')


@app.route('/form/form_signup')
def form_signup():
  return render_template('form_signup.html')


@app.route('/form/form_thank')
def form_thank():
  first = request.args.get('first')
  last = request.args.get('last')
  return render_template('form_thank.html', first=first, last=last)


@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
