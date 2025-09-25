from flask import Flask, render_template, request, redirect
import db


app = Flask(__name__)

db.setup()

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    people = db.get_people()
    return render_template('hello.html', name=name, people=people)

@app.route('/submit',methods=['post'])
def handle_submission():
    name = request.form['name']
    db.add_person(name)
    return redirect('/')