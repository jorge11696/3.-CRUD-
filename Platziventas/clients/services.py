#Guardaremos nuestra logica de negocio, abrir achivos , escribir etc
import csv
import os

from clients.models import Client #Clients.models es el modulo que queremos y vamos a importarnos a nuestro cliente

class ClientService:

    def __init__(self,table_name):#Esta clase recibe el nombre de la tabla en donde guardarse,que es el nombre del archivo en donde lo vamos a guardar,es nuestro archivo csv
        self.table_name = table_name #Nos lo guardamos en una variable de instancia

    def create_client(self,client):
        with open(self.table_name, mode='a') as f: # self.table_name es el archiov que va a abrir, en modo append, por lo que añadiremos cuando llegue un nuevo cliente al final del objeto
            writer = csv.DictWriter(f,fieldnames=Client.schema()) #f recibe el archivo. Parte de dictwriter es poner los fieldnames,es decir cuales son las columnas dentro de nuestra estructura tabular. Como no queremos ponerlas directamente podemos preguntarle al modelo cuales son sus columnas (from clients.models import Client)
#client.schema()=utilizamos nuestro cliente y su metodo estatico schema
            writer.writerow(client.to_dict()) #Escribimos una nueva fila dentro de nuestro estructura tabular, dentro del csv. Y como dictwriter necesita diccionarios podemos decir que el client que recibimos como parametro lo convertimos en un diccionario

    def list_clients(self):
        with open(self.table_name,mode='r') as f: #Abrimos nuestro archivo con referencia a nuestra tabla, en modo read.
            reader = csv.DictReader(f,fieldnames=Client.schema())#Generamos reader, recibe el file (f)

            return list(reader)#Para convertirlo en lista de clientes

    def update_client(self,updated_client):#Recibe como parametro a un cliente ya actualizado
        clients = self.list_clients() #Obtenemos nuestra lista de clientes
#Utilizaremos una variable auxiliar para ciclar entre estos clientes y unicamente tomar al cliente que se modifico, y reemplazarlo. Los demas clientes tomarlos como estan
        updated_clients = []
        for client in clients:
            if client ['uid'] == updated_client.uid: #Si nuestro cliente tiene el mismo id que nuestro cliente que ha sido actualizado:
                updated_clients.append(updated_client.to_dict())#Añadimos el cliente actualizado. To dict para convertirlo en diccionario
            else:
                updated_clients.append(client)#Si no ha sido actualizado lo metemos como está
        self._save_to_disk(updated_clients)#Le pasamos los clientes actualizados

    def _save_to_disk(self,clients): #Guardamos a disco generando tabla temporal
        tmp_table_name = self.table_name + '.tmp'
        with open(tmp_table_name,mode='w') as f:
            writer = csv.DictWriter(f, fieldnames = Client.schema())
            writer.writerows(clients)

        os.remove(self.table_name) #Removemos archivo y renombramos tabla temporal para que unicamente nos quede la referencia original
        os.remove(tmp_table_name, self.table_name)
