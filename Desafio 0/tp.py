from funciones import *

continuar = True

while continuar == True:
    menu_principal(opciones)
    opcion_elegida=input("Elija una opcion: ")

    if opcion_elegida == "A" or opcion_elegida == "a":
        superheroe_nombre()
        continuar = False
    elif opcion_elegida == "B" or opcion_elegida == "b":
        superheroe_altura()
        continuar = False
    elif opcion_elegida == "C" or opcion_elegida == "c":
        altura_promedio()
        continuar = False
    elif opcion_elegida == "D" or opcion_elegida == "d":
        superheroe_maximo()
        superheroe_minimo()
        continuar = False
    elif opcion_elegida == "E" or opcion_elegida == "e":
        superheroe_mas_y_menos_pesado()
        continuar = False
    elif opcion_elegida == "H" or opcion_elegida == "h":
        print("El código ya está ordenado en funciones")
        continuar = False