
PASSWORD = '12345'

def password_required(func):
    def wrapper():
        password = input('Cual es tu contraseña?')

        if password == PASSWORD:
            return func()

        else:
            print('La contraseña es incorrecta')

    return wrapper

@password_required #decorador
def needs_passwors():
    print ('La constraseña es correcta')

def upper(func):
    def wrapper(*args, **kwargs): # args y kwargs son los argumentos que tienen keyworda, que tienen nombre, la estrella es una expansion. estamos recibiendo una lista, solo quiero los parametros tal cual son
        result = func(*args, **kwargs)
        return result.upper() #MAYUSCULAS
    return wrapper

@upper
def say_my_name(name):
    return'Hola, {}'.format(name)


if __name__ == '__main__':
    print(say_my_name('Jorge'))
