from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/user/<name>')
def user(var1 = 'Eduardo'):
    var2 = 21
    var3 = [1,2,3,4,5,6,7,8,9]
    return render_template('user.html',var1=var1,var2 = var2, var3=var3)

if __name__ == '__main__':
    app.run(debug=True)