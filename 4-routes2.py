from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
    return "<script> alert('Hola jsjs');</script>"

@app.route('/params')
@app.route('/params/<name>')
@app.route('/params/<name>/<int:num>')
def params(name='este es un valor por default',num='nada'):
    return '<h1>El parametro es:</h1>{},{}'.format(name,num)
#http://localhost:8000/params/isaac/14

if __name__ == '__main__':
    app.run(debug=True,port=8000)