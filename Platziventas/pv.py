import click

from clients import commands as clients_commands    #importamos los modulos del archivo comandos.py
#Del modulo clients,importa commands y llamalos client_commands

CLIENTS_TABLE = '.clients.csv'#Pasamos el nombre de la tabla, es decir el nombre del archivo que vamos a utilizar para poder guardar a todos nuestros clientes

@click.group() #para decirle a click que este es nuestro punto de entrada
@click.pass_context #Nos va a dar un objeto contexto
def cli(ctx): #Definimos nuestro punto de entrada
    ctx.obj = {} #Inicializamos objeto contexto como un diccionario vacio
    ctx.obj['clients_table'] = CLIENTS_TABLE#Añadimos .clients.csv alias CLIENTS_TABLE al contexto

cli.add_command(clients_commands.all)
#Dentro del modulo importado y llamado client_command, utilizamos la
#variable all que nosotros sabemos que es un alias hacia la funcion clients,
#haciendo mas legible el codigo para que no sea client_commands_clients
