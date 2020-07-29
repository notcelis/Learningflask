from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "<script> alert('Hola jsjs');</script>"

app.run()