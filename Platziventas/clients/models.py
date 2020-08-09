import uuid

class Client:

    def __init__(self,name,company,email,position,uid=None): #inicializamos nuestro cliente con init, importante primer parametro de todos los metodos llevan keyword self
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4() #Si nos mandan el parametro uid vamos a utilizar dicho, de lo contrario utilizamos el modulo uuid de python que nos permite generar uid unicas

    def to_dict(self):
        return vars(self) #La funcion global vars checkea que es lo que regresa el metodo _dict y nos permite acceder a un diccionario de nuestro objeto porque para poder escribirlo a disco en csv necesitamos convertirlo a diccionario y con ester metodo lo convierte

    @staticmethod #Un metodo estatico se puede ejecutar sin necesidad de una instancia de clase. En este caso vamos a declarar el esquema que definimos para que se pueda guardar en la base de datos.
    def schema(): #No tiene keyword self porque no necesita una instancia
        return ['name', 'company', 'email', 'position', 'uid'] #Regresa una lista de variables que existen en este objeto
#Ya tenemos listo nuestro primer objeto
