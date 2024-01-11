from flask import Flask, render_template

app = Flask(__name__)

@app.route('/more')
def moringa():
   return render_template('index.html')

@app.route('/user/<name>')
def user_person(name):
   return render_template('user.html', name=name)
