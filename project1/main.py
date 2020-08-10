from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import flash

from flask import url_for
from flask import redirect

from flask_wtf import CsrfProtect
import forms

app = Flask(__name__)
app.secret_key = 'mi_palabra_secreta'
csrf = CsrfProtect(app)

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        print (username)

    title = 'Index'
    return render_template('index.html', title = title)

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        username = login_form.username.data
        success_message = 'Bienvenido {}'.format(username)
        flash(success_message)
        session['username'] = login_form.username.data
    return render_template('login.html', form = login_form)

@app.route('/cookie')
def cookie():
    reponse = make_response(render_template('cookie.html'))
    reponse.set_cookie('mi_primera_cookie','Isaac')
    return reponse

@app.route('/comment',methods=['GET','POST'])
def comment():
    return render_template('comment.html')

if __name__ == '__main__':
    app.run(debug=True,port=5000)