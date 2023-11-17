# Se utilizan las librerías "os" y "requests" para el funcionamienro correcto del código.
# La librería requests se ha instalado previamente.

import os
import json
import requests

# Función "def para almacenar lois datos que se ingresan del pokemon"

def obtencion_datos_pokemon(nombre_pokemon):
    url_base = "https://pokeapi.co/api/v2/pokemon/"
    url_pokemon = f"{url_base}{nombre_pokemon.lower()}"
    
    respuesta = requests.get(url_pokemon)

    if respuesta.status_code == 404: # Se mostrará el correspondiente código de error si no existe información sobre el pokemon.
        print(f"No se encontró información para el Pokémon {nombre_pokemon}.")
        return None

    datos_pokemon = respuesta.json()
    return datos_pokemon

# Aquí se almacenarán los datos generales del pokemon.

def mostrar_info_pokemon(datos_pokemon):
    imagen_url = datos_pokemon['sprites']['front_default']
    peso = datos_pokemon['weight']
    tamaño = datos_pokemon['height']
    movimientos = [movimiento['move']['name'] for movimiento in datos_pokemon['moves']]
    habilidades = [habilidad['ability']['name'] for habilidad in datos_pokemon['abilities']]
    tipos = [tipo['type']['name'] for tipo in datos_pokemon['types']]

# Esta sección será para mostrar al usuario la información que se ha generado.
    print(f"Imagen: {imagen_url}")
    print(f"Peso: {peso}")
    print(f"Tamaño: {tamaño}")
    print(f"Movimientos: {', '.join(movimientos)}")
    print(f"Habilidades: {', '.join(habilidades)}")
    print(f"Tipos: {', '.join(tipos)}")

    return imagen_url

def guardar_en_json(datos_pokemon, imagen_url, carpeta="pokedex"):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    nombre_pokemon = datos_pokemon['name']
    archivo_json = os.path.join(carpeta, f"{nombre_pokemon}.json")

    with open(archivo_json, 'w') as archivo:
        datos_a_guardar = {
            'nombre': nombre_pokemon,
            'imagen': imagen_url,
            'datos': datos_pokemon
        }
        json.dump(datos_a_guardar, archivo, indent=4)

    print(f"La información del Pokémon {nombre_pokemon} se ha guardado en {archivo_json}.")

def main():
    nombre_pokemon = input("Introduce el nombre de un Pokémon: ")
    
    datos_pokemon = obtencion_datos_pokemon(nombre_pokemon)
    
    if datos_pokemon:
        imagen_url = mostrar_info_pokemon(datos_pokemon)
        guardar_en_json(datos_pokemon, imagen_url)

if __name__ == "__main__":
    main()
