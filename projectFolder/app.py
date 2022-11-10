from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    name = "Evelyn Lechuga"
    details = readDetails('static/detail.txt')
    return render_template("base.html", name = name, aboutMe = details)

@app.route('/user/<name>')
def greet (name):
    return f'<p> Hello, {name}!<p>'

@app.route('/form', methods ['GET', 'POST'])
def formDemo():
    name = None 
    if request.method == 'POST':
        name = request.form['name']    

if __name__ == '__main__':
    app.run(debug=True)