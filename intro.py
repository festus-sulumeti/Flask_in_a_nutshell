# Learning the introduction of Flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome into the system'
