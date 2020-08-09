import sys #Para sair del loop

clients = ['pablo','ricardo']

def create_client(client_name):
    global clients #para poder acceder a esta variable, redeclaramos la variable con global

    if client_name not in clients:
       clients.append(client_name)
    else:
        print('Client already is in the client\'s list')

def list_clients():
    for idx,client in enumerate(clients):#Enumerate para definir el indice cuando estamos iterando, recibiremos dos valores idx y cliente
        print('{}: {}'.format(idx,client))

def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name) #Posicion donde se encuentra el nombre del cliente que queremos modificar
        clients[index] = updated_client_name #Modificamos valores mediante indice
    else:
        print('Client is not in clients list')

def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name) #Con remove podemos eliminar valor de lista sin saber su indice
    else:
        print('Client is not in clients list')

def search_client(client_name):
    for client in clients:
        if client != client_name:
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

if __name__ == '__main__':
    _print_welcome()
    command = input()
    command = command.upper()
    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name) #Si nos retorna true es que encontraron al cliente

        if found: #En caso de que found sea true
            print('The client is in the client\'s list')
        else: # En caso de que sea false
            print('The client: {} is not in our client\'s list'.format(client_name))
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input ('What is the updated client name?: ')
        update_client(client_name, updated_client_name)
    else:
        print('Invalid command')
