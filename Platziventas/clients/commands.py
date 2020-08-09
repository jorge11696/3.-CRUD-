import click

from clients.services import ClientService #Importamos las clases que necesitamos
from clients.models import Client

#Todas estas funciones todavia no son comandos de click, para convertirlos utilizaremos los decoradores
@click.group() #Convierte la funcion clients en otro decorador
def clients():#Nos servira para definir cual es el grupo al que pertenecen todas las demas funciones
    """Manages the clients lifecycle"""
    pass

@clients.command() #Comando
@click.option('-n','--name', #Para obtener parametros ctx,name,company etc le vamos a pedir ayuda a click para aque se los pida al usuario
              type=str, #Nombre abreviado y nombre completo,bastante comun, tipo string
              prompt=True, #Si no nos lo dan via patron abreviado dentro del comando queremos pedirselo al usuario
              help='The client name')#Linea de ayuda
@click.option('-c','--company',
              type=str,
              prompt=True,
              help='The client company')
@click.option('-e','--email',
              type=str,
              prompt=True,
              help='The client email')
@click.option('-p','--position',
              type=str,
              prompt=True,
              help='The client position')
@click.pass_contexts #vamos a pasarle el contexto porque esta funcion lo necesita
def create (ctx,name,company,email,position): #ctx:contexto que acabamos de inicializar como un diccionario vacio en archivo pv.py
    """Create a new client""" #Docsting
    client = Client(name,company,email,position) #Inicializamos nuestro cliente,como es nuevo no tiene uid, el sistema se lo generara solo
    client_service = ClientService(ctx.obj ['clients_table']) #inicializamos clientservice y nos importamos del contexto (ctx) el nombre de la tabla

    client_service.create_client(client) #Ultimo parentesis para pasar la referencia de nuestro cliente

@clients.command()
@click.pass_contexts
def list (ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['Clients_table']) #Referencia a nustro client service, cogemos e ctx y le pasamos el nombre d ela tabla

    client_list = client_service.list_clients()#Nos traemos nuestra lista de clientes

    click.echo(' ID  |  NAME  |  COMPANY  |  EMAIL  |  POSITION')
    click.echo('*' * 100)
#No utilizamos print sino click eko porque el comportamiento de print varia en dif sist. operativos y asi garantizamos que sea igual en todos los sist op.
    for client in clients:
        click.echo('{uid}  |  {name}  | {company}  |  {email}  |  {position}'.format(
            uid= client['uid'],
            name= client['name'],
            company= client['company'],
            email=client['email'],
            position = client['position']))

@clients.command()
@click.pass_contexts
def update(ctx,client_uid):
    """updates client"""
    client_service = ClientService(ctx.obj['clients_table'])

    client_list = client_service.list_clients()

    client = [client for client in client_list if client['uid']==client_uid]

    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)
        click.echo('Client updated')
    else:
        click.echo('Client not found')


def _update_client_flow(client):
    click.echo('Leave empty if you dont want to modify the value')

    client.name = click.prompt('New name', type=str, default=client.name)
    client.company = click.prompt('New company', type=str, default=client.company)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.position = click.prompt('New position', type=str, default=client.position)

@clients.command()
@click.pass_contexts
def delete (ctx,client_uid):
    """Deletes a client"""
    pass

all=clients
