from flask import Flask
from flask import request
from flask import render_template
import forms
from flask_wtf.csrf import CSRFProtect 
from flask import make_response

#Primer argumento el nombre del módulo o paquete de la aplicación. Para estar seguros de ello, utilizaremos la palabra reservada name.
#Esto es necesario para que Flask sepa, por ejemplo, donde encontrar las plantillas de nuestra aplicación o los ficheros estáticos.
app = Flask(__name__)


app.secret_key = 'my_secret_key'

csrf = CSRFProtect(app)

@app.route('/')
def saludo():
    #recepcion de cookie
    custome_cookie = request.cookies.get('custome_cookie', 'Undefinded')
    print(custome_cookie)
    return "hey!"

#No se pueden repetir metodos en rutas(puebalo;), podemos recibir parametros de diferentes tipos vienen en la direccion url despues de
# ?<nombreparametro> = <valor> con & concatenas parametros indefinidamente 
@app.route('/params')
def params():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    return f'tus parametros son : {param1},{param2}'

#Podemos conocer el orden de nuestra url por ejemplo traer algo de una bd tomando como registros los parametros
#el parametro conocido se pone entre diamantes(porque?) de esta manera se pueden manejar mas rutas y hacerlas mas concretas
#tambien se asigna valoders por default a las rutas sin param y se puede validar el tipo de los params ejemplo <int:id>
@app.route('/validarruta/')
@app.route('/validarruta/<columna>/')
@app.route('/validarruta/<columna>/<int:id>')
def validarruta(columna = 'valor por default', id = ''):
    return f'el parametro es {columna}, {id}'

#Un template o plantilla es una herramienta muy útil para separar el diseño web de la programación de las funcionalidades de la página web.
#El poder de usas templates en un desarrollo web tiene la ventaja de separar las funciones: diseño y programación
#en render template se le da como primer parametro el template que va a renderizar, flask trabaja con jinja2 para renderizar templates
#no se da la ruta de tmplates/index... por default se sabe donde esta los templates en caso de que la carpeta cambie de nombre en app template folder
@app.route('/template')
def index():
    return render_template('index.html')

#mandamos variables a nuestro template como argumentos en render template 
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
    #metodo run levanta nuestro servidor por default en el puerto 5000 cambio con port 
    app.run(debug = True )