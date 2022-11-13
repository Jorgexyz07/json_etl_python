# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json


def serializar():
    print("Funcion que genera un archivo JSON")
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    # json_data = {...}

    #1° Armo el JSON que contendrá una lista: {"name": "value",... "name":[{"name": "value",...}]}
    
    json_data ={"nombre": "Jorge", "apellido": "Juarez", "DNI": "34754171", "Lista_prendas": [{"Zapatillas": "4", "Remeras": "12"}]  }
   
    
    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina

    #2° Abro un archivo para almacenar mi JSON como OBJETO (1 sola línea)

    with open("mi_json.json", "w") as jsonfile:
        data = [json_data]                      #Archivo JSON creado ante
        json.dump(data, jsonfile, indent=4)     

        #.dump (a, b, c) se utiliza para guardar los objetos en un archivo, SERIELIZACIÓN
        # a es la variable que usa como entrada
        # b el archivo donde va a cargar en formato JSON OBJETO la variable cargada
        # c es la indentación que tiene el archivo jsonfile

        #print (data)       Visualizo lo almacenado

        
    # Observe el archivo y verifique que se almaceno lo deseado

    

def deserializar():
    print("Funcion que lee un archivo JSON")
    # JSON Deserialize
    # Basado en la función  anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()

    #1°Abro y leo el archivo("r")

    with open("mi_json.json", "r") as jsonfile:
        json_data = json.load(jsonfile)         
        
        #creo la variable json_data donde voy a guardar el archivo jsonfile antes creado
        
    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado

    json_string = json.dumps(json_data, indent=4)

    #.dumps(a, b) convierte en tipo STRING al OBJETO JSON (1 sola linea) creado, DESEREIALIZACIÓN   
    #a nombre del OBJETO creado (la variable donde se guardo)
    #b es la indentación que tendrá el JSON convertido a STRING

    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en la función anterior

    print("Mostrar el contenido del archivo mi_json")
    print(json_string)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    serializar()
    deserializar()

    print("terminamos")