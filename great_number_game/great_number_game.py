from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/')
def index():
    if 'random_number' not in session:
        session['random_number'] = random.randint(0,101)
    print session['random_number']
    return render_template('index.html')

@app.route('/random', methods=['POST'])
def random_number():
    session['user_number'] = int(request.form['number'])
    return redirect('/')

@app.route('/play_again', methods=['POST'])
def play_again():
    session.pop('random_number')
    session.pop('user_number')
    return redirect('/')

app.run(debug = True)
