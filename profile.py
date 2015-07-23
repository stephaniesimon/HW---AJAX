import random

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    """Show index page."""
    return render_template("index.html")



@app.route('/profile', methods=['POST'])
def profile():
    """Return results from profile form."""

    fullname = request.form['name']
    age = request.form['age']
    job = request.form['occupation']
    salary = request.form['salary']
    education = request.form['education']
    state = request.form['state']
    city = request.form['city']
    garden = request.form['garden']
    tv = request.form['tv']
    # TODO: get the values from the rest of the form
    # Add them to jsonify
    
    return jsonify({'fullname' : fullname, 'age' : age, 'job' : job, 'salary' : salary, 'education' : education,
    	'state' : state, 'city' : city, 'garden' : garden, 'tv' : tv})





if __name__ == "__main__":
    app.run(debug=True)