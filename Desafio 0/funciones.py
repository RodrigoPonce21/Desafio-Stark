from data_stark import lista_personajes

opciones = [
    "A) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe",
    "B) Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo",
    "C) Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)",
    "D) Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)",
    "G) Calcular e informar cual es el superhéroe más y menos pesado",

]

def menu_principal(opciones):
    # Imprime el menú
    for menu in opciones:
        print(menu)

def superheroe_nombre():
    for personaje in lista_personajes:
        print(f"Nombre: {personaje['nombre']}")

def superheroe_altura():
    for personaje in lista_personajes:
        print(f"Nombre: {personaje['nombre']}, Altura: {personaje['altura']}")

def superheroe_maximo():
    max_altura = max(float(personaje["altura"]) for personaje in lista_personajes)
    max_personaje = next(personaje for personaje in lista_personajes if float(personaje["altura"]) == max_altura)
    print(f"El superhéroe más alto es: {max_personaje['nombre']}, con una altura de {max_altura}")

def superheroe_minimo():
    min_altura = min(float(personaje["altura"]) for personaje in lista_personajes)
    min_personaje = next(personaje for personaje in lista_personajes if float(personaje["altura"]) == min_altura)
    print(f"El superhéroe más bajo es: {min_personaje['nombre']}, con una altura de {min_altura}")

def altura_promedio():
    promedio = sum(float(personaje["altura"]) for personaje in lista_personajes) / len(lista_personajes)
    print(f"La altura promedio de los superhéroes es: {promedio}")

def superheroe_mas_y_menos_pesado():
    max_peso = max(float(personaje["peso"]) for personaje in lista_personajes)
    min_peso = min(float(personaje["peso"]) for personaje in lista_personajes)
    max_personaje = next(personaje for personaje in lista_personajes if float(personaje["peso"]) == max_peso)
    min_personaje = next(personaje for personaje in lista_personajes if float(personaje["peso"]) == min_peso)
    print(f"El superhéroe más pesado es: {max_personaje['nombre']}, con un peso de {max_peso}")
    print(f"El superhéroe menos pesado es: {min_personaje['nombre']}, con un peso de {min_peso}")