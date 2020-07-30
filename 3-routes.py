from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
    return "<script> alert('Hola jsjs');</script>"

@app.route('/params')
def params():
    param = request.args.get('params1','no contiene este parametro')
    param2 = request.args.get('params2','no contiene este parametro')
    return '<h1>El parametro es:</h1>{},{}'.format(param,param2)
#http://localhost:8000/params?params1=soylabrga&params2=x2

if __name__ == '__main__':
    app.run(debug=True,port=8000)