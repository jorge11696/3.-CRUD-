import sys #Para sair del loop

clients = [ #dos diccionarios
{
  'name': 'Pablo',
  'company': 'Google',
  'email': 'pablo@google.com',
  'position': 'Software engineer',
},
{
  'name': 'Ricardo',
  'company': 'Facebook',
  'email': 'ricardo@facebook.com',
  'position': 'Data engineer',
}
]

def create_client(client):
    global clients #para poder acceder a esta variable, redeclaramos la variable con global

    if client not in clients:
       clients.append(client)
    else:
        print('Client already is in the client\'s list')

def list_clients():
    for idx,client in enumerate(clients):#Enumerate para definir el indice cuando estamos iterando, recibiremos dos valores idx y cliente
        print('{uid} | {name} | {company} | {position}'.format(uid = idx, name=client['name'],company = client['company'], email=client['email'], position = client['position']))

def update_client(client_id, updated_client_name):
    global clients

    if len(clients) -1 >= client_id:
        clients[client_id]= updated_client_name
    else:
        print('Client is not in clients list')

def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break

    else:
        print('Client is not in clients list')

def search_client(client_name):
    for client in clients:
        if client ['name'] != client_name:
            continue
        else:
            return True


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print ('*' * 50)
    print ('What would you like to do today?')
    print ('[C]reate client')
    print('[L]ist clients')
    print ('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')

def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is de client {}?'.format(field_name))

        return field

def _get_client_name():
    client_name = None #Es la forma que utliza python para definir que no hay ningun valor
    while not client_name: #Mientras no escriban ningun nombre y presionen enter volvera a hacer la pregunta
        client_name = input ('What is the client name?')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit() #Salimos del sistema, lo declaramos al principio

    return client_name

def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
        }
    return client

if __name__ == '__main__':
    _print_welcome()
    command = input()
    command = command.upper()
    if command == 'C':
        client = _get_client_from_user()
        create_client(client)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'D':
        client_id = int( _get_client_field('id'))
        delete_client(client_id)
        list_clients()
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name) #Si nos retorna true es que encontraron al cliente

        if found: #En caso de que found sea true
            print('The client is in the client\'s list')
        else: # En caso de que sea false
            print('The client: {} is not in our client\'s list'.format(client_name))
    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client_name = _get_client_from_user()
        update_client(client_id,updated_client_name)
    else:
        print('Invalid command')
