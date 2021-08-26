from wtforms import  Form 
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class CommentForm(Form):
    username = StringField('username', 
    [
        validators.Required(message='el username es requerido'),
        validators.length(min=4, max=25, message='ingrese un username valido!')
    ]
    )
    email = EmailField('Correo electronico')
    comment = TextField('Comentario')