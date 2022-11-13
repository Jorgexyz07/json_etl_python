# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
import requests
import numpy as np

import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".


    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    #1° Realizo un requests para acceder y utilizar datos desde una página web

    response = requests.get("https://jsonplaceholder.typicode.com/todos")

    #Guardo la información de la página en una variable, en este caso response

    #2° Convierto la información adquirido a formato json 

    data = response.json()

    #.json me permite convertir la variable donde se guardo la información a formato JSON
    
    #Otra forma de obtener el objeto JSON, un poco más extensa
    #data = json.loads(response.text)

    #3° Verifio los datos obtenidos, imprimo mediante json.dumps (STRING)

    print("Verifico los datos obtenidos:\n", json.dumps(data, indent=4))

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    #Por compresión genero una lista a partir de mi JSON para ordenar los usuarios
    #y ver cuántos títulos completo

    lista = [x["userId"] if x["completed"] == True else 0 for x in data]

    #x["userId"] es mi salida 1, es decir al cual voy a ponerle la condición
    #x["completed"] es la condición que impongo
    #else que pasa si no se cumple la condición
    #for x in data bucle donde se irá recorriendo para ver si cumple la condición

    #Genero dos listas vacías para almacenar los usuarios y títulos de c/u
    #Antes de generar un bucle for

    usuarios = []

    titulos = []

    for i in range (1,11):  #arranco en 1 y termino en 10
        print("El usuario", i, "completo", lista.count(i), "títulos") #.count() me contabiliza la cantidad de títulos completos de ese usuario a partir de la variable lista
        usuarios.append(i)              #agrego el usuario a la lista
        cant_titulos = lista.count(i)   #contabilizo la cant de títulos de ese usuario
        titulos.append(cant_titulos)    #cargo la cant de títulos a la lista títulos

    print(usuarios)     #Verifico los usuarios
    print(titulos)      #Verifico la cantidad de títulos


    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

    #Ahora grafico los datos recolectados en un gráfico de barras

    #1° Genero la figura

    fig = plt.figure()      #.figure crea la figura

    #2° Generó el gráfico y configuró un título

    fig.suptitle("Gráfico de barras", fontsize = 16)    #Configuración título
    ax = fig.add_subplot()                              #Creación gráfico

    #3° Determino el tipo de gráfico y configuro el gráfico
    ax.bar(usuarios, titulos)           #usuarios eje horizontal, titulos eje vertical
    ax.set_facecolor("whitesmoke")      #Color del fondo del gráfico
    ax.set_ylabel("Cantidad de títulos")#Etiqueta eje y
    ax.set_xlabel("Usuarios")           #Etiqueta eje x
    plt.show()                          #Muestro el gráfico


    


    print("terminamos")