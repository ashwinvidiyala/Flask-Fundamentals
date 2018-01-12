from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<ninja_color>')
def show_each_ninja(ninja_color):
    if ninja_color == 'purple':
        return render_template('donatello.html', ninja_color = ninja_color)
    elif ninja_color == 'blue':
        return render_template('leonardo.html', ninja_color = ninja_color)
    elif ninja_color == 'orange':
        return render_template('michelangelo.html', ninja_color = ninja_color)
    elif ninja_color == 'red':
        return render_template('raphael.html', ninja_color = ninja_color)
    else:
        return render_template('notapril.html')

app.run(debug = True)
