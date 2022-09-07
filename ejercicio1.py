#esto es un comentario para poder programar mucho mejor con la gente 
# if 5 > 3:
    #print("5 es mayor que a 3")


#variables es un tipo de dato

#x = 5
#y = "chacchito feliz"

#print(x, y)

email = "chanchitofeliz@correo.com"

#print(email)

miVariable = "chanchito"
apellido = "feliz"

#print(miVariable, apellido)

#multiples variables 

a,b,c = "lala", "lele", "lili"

#print(a,b,c)

valor1 = valor2 = valor3 = 'chanchitofeliz'

#print(valor1,valor2,valor3)

inicio = "hola "
final = "mundo"

#print(inicio + final)


palabra = 'hola mundo'#string
oracion = "hola mundo" #string

entero = 20 # intenger
decimal = 10.2 #tipo float
complejo = 1j 

#print(entero,oracion,palabra,oracion,complejo)

#listas 

lista = ["hola mundo",2,3]
lista2 = lista.copy()
lista.append("chanchito triste") #agrega contenido a la lista
#lista.clear()#elimina todo lo de dentro de un lista
#print(lista, lista2.count(2)) #cuenta cuantas veces se repite un valor asignado
#print(len(lista)) #muestra la longitud de la lista 


#print(lista[2])

#como eleminar elementos de una lista 
#lista.pop()#eliminar el ultimo elemento de un lista
#lista.remove(2)#elimina un elemento que tu selecciones

lista.reverse() 
#print(lista)

#tuplas una vez creadas no se pueden elimininar y no son modificables 
tupla = ('gola',"mundo","somos una tupla")
listaDeTupla = list(tupla) # lo que hice fue copiar la tupla y transfromarla a una lista 
listaDeTupla.append("chanchitox")
#print(listaDeTupla)

rango = range(6)
#print(range)


#Diccionarios 

diccionario = {
    "nombre": "chanchito feliz",
    "raza": "persa",
    "edad": 5
}
#print(diccionario)
#print(diccionario["edad"])
#print(diccionario["nombre"])
#print(diccionario.get('nombre'))
diccionario["nombre"] = "firulais" #cambiar el nombre de la variable
print(diccionario)

diccionario["llora"] = "si"
print(diccionario)

diccionario.pop("llora")
print(diccionario)