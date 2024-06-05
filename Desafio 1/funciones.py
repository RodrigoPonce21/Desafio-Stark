from data_stark import lista_personajes

opciones = [
    "A) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M",
    "B) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F",
    "C) Recorrer la lista y determinar cuál es el superhéroe más alto de género M",
    "D) Recorrer la lista y determinar cuál es el superhéroe más alto de género F",
    "E) Recorrer la lista y determinar cuál es el superhéroe más bajo de género M",
    "F) Recorrer la lista y determinar cuál es el superhéroe más bajo de género F",
    "G) Recorrer la lista y determinar la altura promedio de los superhéroes de género M",
    "H) Recorrer la lista y determinar la altura promedio de los superhéroes de género F",
    "I) Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)",
    "J) Determinar cuántos superhéroes tienen cada tipo de color de ojos",
    "K) Determinar cuántos superhéroes tienen cada tipo de color de pelo",
    "L) Determinar cuántos superhéroes tienen cada tipo de inteligencia",
    "M) Listar todos los superhéroes agrupados por color de ojos",
    "N) Listar todos los superhéroes agrupados por color de pelo",
    "O) Listar todos los superhéroes agrupados por tipo de inteligencia"
]

def menu_principal(opciones):
    # Imprime el menú
    for menu in opciones:
        print(menu)

def superheroes_genero(genero):
    for personaje in lista_personajes:
        if personaje["genero"] == genero:
            print(f"Nombre: {personaje['nombre']}")

def superhero_mas_alto_genero(genero):
    max_altura = max(float(personaje["altura"]) for personaje in lista_personajes if personaje["genero"] == genero)
    max_personaje = next(personaje for personaje in lista_personajes if float(personaje["altura"]) == max_altura and personaje["genero"] == genero)
    print(f"El superhéroe más alto del género {genero} es: {max_personaje['nombre']}, con una altura de {max_altura}")

def superhero_mas_bajo_genero(genero):
    min_altura = min(float(personaje["altura"]) for personaje in lista_personajes if personaje["genero"] == genero)
    min_personaje = next(personaje for personaje in lista_personajes if float(personaje["altura"]) == min_altura and personaje["genero"] == genero)
    print(f"El superhéroe más bajo del género {genero} es: {min_personaje['nombre']}, con una altura de {min_altura}")

def altura_promedio_genero(genero):
    promedio = sum(float(personaje["altura"]) for personaje in lista_personajes if personaje["genero"] == genero) / len([personaje for personaje in lista_personajes if personaje["genero"] == genero])
    print(f"La altura promedio de los superhéroes de género {genero} es: {promedio}")

def informar_nombre_superheroes():
    superhero_mas_alto_genero("M")
    superhero_mas_alto_genero("F")
    superhero_mas_bajo_genero("M")
    superhero_mas_alto_genero("F")

def contar_colores(tipo):
    colores = {}
    for personaje in lista_personajes:
        color = personaje[tipo].upper()
        if not color:
            color = "SIN PELO"
        if color in colores:
            colores[color] += 1
        else:
            colores[color] = 1
    for color, cantidad in colores.items():
        print(f"El color {color} se encuentra en {cantidad} superhéroes")

def contar_inteligencia():
    inteligencias = {}
    for personaje in lista_personajes:
        if personaje["inteligencia"] in inteligencias:
            inteligencias[personaje["inteligencia"]] += 1
        else:
            inteligencias[personaje["inteligencia"]] = 1
    for inteligencia, cantidad in inteligencias.items():
        if not inteligencia:
            inteligencia = "none"
        print(f"La inteligencia {inteligencia} se encuentra en {cantidad} superhéroes")

def agrupar_por_caracteristica(tipo, nombre_caracteristica):
    caracteristicas = {}
    for personaje in lista_personajes:
        valor = personaje[tipo]
        if tipo == "color_pelo" or tipo == "color_ojos":
            valor = valor.upper()
            if not valor:
                valor = "Sin color"
        if valor in caracteristicas:
            caracteristicas[valor].append(personaje["nombre"])
        else:
            caracteristicas[valor] = [personaje["nombre"]]
    for valor, nombres in caracteristicas.items():
        print(f"{nombre_caracteristica.capitalize()} {valor}: {', '.join(nombres)}")