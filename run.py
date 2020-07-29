from flask import Flask

app = Flask(__name__)
@app.route('/')

def index():
    return "<script> alert('Hola jsjs');</script>"

if __name__ == '__main__':
    app.run(debug=True,port=8000)