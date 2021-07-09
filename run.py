from flask import Flask
from flask import request
from flask import render_template
import forms
from flask_wtf.csrf import CSRFProtect 
from flask import make_response

app = Flask(__name__)
app.secret_key = 'my_secret_key'

csrf = CSRFProtect(app)

@app.route('/')
def saludo():
    custome_cookie = request.cookies.get('custome_cookie', 'Undefinded')
    print(custome_cookie)
    return "hey!"

@app.route('/params')
def params():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    return f'tus parametros son : {param1},{param2}'

@app.route('/validarruta/')
@app.route('/validarruta/<columna>/')
@app.route('/validarruta/<columna>/<int:id>')
def validarruta(columna = 'valor por default', id = ''):
    return f'el parametro es {columna}, {id}'

@app.route('/template')
def index():
    return render_template('index.html')

@app.route('/template/<tag>')
def tag(tag= 'vf'):
    my_list= [1,2,3]
    return render_template('index.html',list=my_list,tagh=tag)

@app.route('/herencia', methods = ['GET', 'POST'])
def try1():
    comment_form = forms.CommentForm(request.form)
    
    if request.method == 'POST' and comment_form.validate():
        print(comment_form.username.data)

    return render_template('try.html', form = comment_form)

#v16 info de cookies en cookie.html
@app.route('/cookie')
def cookie():
    response = make_response( render_template('cookie.html') )
    response.set_cookie('custome_cookie', 'diego')
    return response

if __name__ == "__main__":
    app.run(debug = True )