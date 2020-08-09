

class Person: #Definimos nuestra clase
    def __init__(self,name,age):  #Definimos nuestro primer metodo de inicializacion
        self.name = name  #self para tener referencias internas
        self.age = age

    def say_hello(self):
        print ('Hello, my name is {} and I am {} years old'.format(self.name,self.age))

if __name__ == '__main__':
    person = Person ('Jorge', 24)

    print ('Age: {}'.format(person.age))
    person.say_hello()
