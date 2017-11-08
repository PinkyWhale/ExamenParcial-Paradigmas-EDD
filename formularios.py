from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField
from wtforms.validators import DataRequired,EqualTo,Regexp,Length

#En este archivo .py se encuentran todas las clases utilizadas en el proyecto.
#Las siguientes clases sirven para validar campos y obtener parametros.
#Estas funciones posees en el campo de validacion las expresiones regulares. Estas sirven para poder filtrar los caracteres a la hora de prosesarlos.
class SearchCliente(FlaskForm):
    parametro = StringField('Escriba el Nombre del Cliente: ', validators=[Length(min=3, max=100, message="Debe ingresar como minimo 3 caracteres."),DataRequired(message="Debe escribir valor")])

class SearchProd(FlaskForm):
    parametro = StringField('Escriba el Nombre del Producto: ', validators=[Length(min=3, max=100, message="Debe ingresar como minimo 3 caracteres."),DataRequired(message="Debe escribir un valor")])

class SearchCant(FlaskForm):
    parametro = StringField('Escriba la Cantidad que Stock que desea buscar: ', validators=[DataRequired(message="Debe escribir un valor."),Regexp(regex="\d+", message="Solo nùmeros enteros por favor")])

class SearchPrecio(FlaskForm):
    parametro = StringField('Escriba el Precio que busca: ', validators=[DataRequired(message="Debe escribir un valor."),Regexp(regex="^(\d|-)?(\d|,)*\.?\d*$", message="Ingrese un precio valido")])
    

#Clases para validar usuarios y contraseñas.
class Checkeo_Log(FlaskForm):
    name = StringField('Usuario:', validators=[DataRequired(message="Debe escribir un nombre de usuario")])
    password = PasswordField('Contraseña:', validators=[DataRequired(message="Debe escribir una contraseña")])


#clase para el nuevo usuario y checkeo de contraseñas.
class CreaUsuario(FlaskForm):
    name = StringField('Usuario:', validators=[DataRequired(message="Debe escribir un nombre de usuario")])
    pass1 = PasswordField('Contraseña:', validators=[DataRequired(message="Debe escribir una contraseña")])
    pass2 = PasswordField('Repita Contraseña:', validators=[DataRequired(message="Debe escribir de nuevo su contraseña"),EqualTo('pass1', message='Las contraseñas deben coincidir')])
