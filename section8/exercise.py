# Set up your imports and your flask app.
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # This home page should have the form.
    return render_template('exercise_index.html')


# This page will be the page after the form
@app.route('/report')
def report():
    # Check the user name for the 3 requirements.

    # HINTS:
    # https://stackoverflow.com/questions/22997072/how-to-check-if-lowercase-letters-exist/22997094
    # https://stackoverflow.com/questions/26515422/how-to-check-if-last-character-is-integer-in-raw-input

    # Return the information to the report page html.
    username = request.args.get('username')
    isupper = username.isupper()
    islower = username.islower()
    end_with_number = username[-1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # lower_letter = any(c.islower() for c in username)
    # upper_letter = any(c.isupper() for c in username)
    # num_end = username[-1].isdigit()

    return render_template('exercise_report.html', isupper=isupper, islower=islower, end_with_number=end_with_number, username=username)

if __name__ == '__main__':
    # Fill this in!
    app.run(debug=True)
