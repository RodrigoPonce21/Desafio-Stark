from funciones import *

continuar = True

while continuar == True:
    menu_principal(opciones)
    opcion_elegida=input("Elija una opción: ")

    if opcion_elegida == "A" or opcion_elegida == "a":
        superheroes_genero("M")
        continuar = False
    elif opcion_elegida == "B" or opcion_elegida == "b":
        superheroes_genero("F")
        continuar = False
    elif opcion_elegida == "C" or opcion_elegida == "c":
        superhero_mas_alto_genero("M")
        continuar = False
    elif opcion_elegida == "D" or opcion_elegida == "d":
        superhero_mas_alto_genero("F")
        continuar = False
    elif opcion_elegida == "E" or opcion_elegida == "e":
        superhero_mas_bajo_genero("M")
        continuar = False
    elif opcion_elegida == "F" or opcion_elegida == "f":
        superhero_mas_bajo_genero("F")
        continuar = False
    elif opcion_elegida == "G" or opcion_elegida == "g":
        altura_promedio_genero("M")
        continuar = False
    elif opcion_elegida == "H" or opcion_elegida == "h":
        altura_promedio_genero("F")
        continuar = False
    elif opcion_elegida == "I" or opcion_elegida == "i":
        informar_nombre_superheroes()
        continuar = False
    elif opcion_elegida == "J" or opcion_elegida == "j":
        contar_colores("color_ojos")
        continuar = False
    elif opcion_elegida == "K" or opcion_elegida == "k":
        contar_colores("color_pelo")
        continuar = False
    elif opcion_elegida == "L" or opcion_elegida == "l":
        contar_inteligencia()
        continuar = False
    elif opcion_elegida == "M" or opcion_elegida == "m":
        agrupar_por_caracteristica("color_ojos", "Color de ojos")
        continuar = False
    elif opcion_elegida == "N" or opcion_elegida == "n":
        agrupar_por_caracteristica("color_pelo", "Color de pelo")
        continuar = False
    elif opcion_elegida == "O" or opcion_elegida == "o":
        agrupar_por_caracteristica("inteligencia", "Inteligencia")
        continuar = False