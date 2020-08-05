from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class Miclaseform(Form):
    username = StringField('username',
                [
                    validators.Required(message='Ingrese el usuario'),
                    validators.length(min=4,max=25, message='Ingrese un usuario valido.')
                ]
                )
    email = EmailField('Correo electronico',
                [
                    validators.Required(message='Ingrese el email'),
                    validators.Email(message='Ingrese un email valido.')
                ])
    comment = TextField('Comentario')
