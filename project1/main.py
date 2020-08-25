from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import flash
from flask import g
from flask import url_for
from flask import redirect

from config import DevelopmentConfig

from flask_wtf import CsrfProtect
import forms
import json

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CsrfProtect(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')




@app.before_request
def before_request():
    #print("1 / request.endpoint=",request.endpoint)
    g.variable="mi variable global desde "

@app.after_request
def after_request(response):
    print(g.variable+"after")
    return response


@app.route('/')
def index():
    print (g.variable+"index")
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


@app.route('/ajax-login',methods=['POST'])
def ajax_login():
    print (request.form)
    username = request.form['username']
    response = {'status':200, 'username':username,'id':1}
    return json.dumps(response)

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(port=5000)