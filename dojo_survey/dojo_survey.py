from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    name = request.form['name']
    location = request.form['Location']
    favorite_language = request.form['Favorite Language']
    comment = request.form['comment']
    return render_template('result.html', name = name, location = location, favorite_language = favorite_language, comment = comment)

app.run(debug = True)
