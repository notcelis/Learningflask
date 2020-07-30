from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    var1 = 'Isaac'
    return render_template('index.html',var1=var1)

@app.route('/route2')
def route2():
    list_vars = ['var1','var2','var3']
    return render_template('route2.html',list_vars=list_vars)

if __name__ == '__main__':
    app.run(debug= True,port=5000)