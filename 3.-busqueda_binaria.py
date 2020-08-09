import random

def binary_search(data,target,low,high): #indice bajo y alto
    if low > high: #Ya recorrimos toda la lista y no esta el numero
        return False

    mid=(low + high) // 2 #Encontrar el indice de la mitad, con dobe // para eliminar los decimales

    if target == data[mid]: # Si el numero a buscar esta en el indice medio
        return True

    elif target < data[mid]: #Si el numero a encontrar es menor que el indice medio
        return binary_search(data,target,low, mid -1) #Dado que target esta en el indice bajo, ya nuestro indice allto sera el medio menos 1, ya que el medio se verifico

    else:
        return binary_search(data,target, mid +1, high)

if __name__ == '__main__':
    data = [random.randint(0,100) for i in range(10)] #list comprehension

    #sort modifica directamente la variable,sorted no.
    data.sort()
    print (data)

    target = int(input('What number would you like to find?'))
    found = binary_search(data,target,0,len(data)-1) #target=lo que queremos buscar. len nos da la cantidad total de elementos pero tenemos que empezar a contar desde el indice 0 por eso restamos 1
    print(found)
