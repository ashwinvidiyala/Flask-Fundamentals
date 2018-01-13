from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'super secret key'

now = datetime.now()

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    activities = []
    if request.form['building'] == 'farm':
        random_number = random.randint(10,21)
        session['gold'] += random_number
        activities.append('Earned {} golds from the farm! ({})'.format(random_number, now))
    elif request.form['building'] == 'cave':
        random_number = random.randint(5,11)
        session['gold'] += random_number
        activities.append('Earned {} golds from the Cave! ({})'.format(random_number, now))
    elif request.form['building'] == 'house':
        random_number = random.randint(2,5)
        session['gold'] += random_number
        activities.append('Earned {} golds from the House! ({})'.format(random_number, now))
    elif request.form['building'] == 'casino':
        random_number = random.randint(-50, 51)
        session['gold'] += random_number
        if random_number < 0:
            activities.append('Entered a casino and lost {} golds. Ouch.({})'.format(random_number * -1, now))
        else:
            activities.append('Entered a casino and won {} golds. Yay!({})'.format(random_number, now))
    session['activities'] += activities
    return redirect('/')

app.run(debug = True)
