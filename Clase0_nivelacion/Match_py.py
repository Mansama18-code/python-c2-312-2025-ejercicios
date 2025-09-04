hora = 8
match hora:
    case 8:
        print("Desayuno")
    case 14:
        print("Comida")
    case 21:
        print("Cena")
    case _:
        print("No toca comer")
# Desayuno


mes = 4
match mes:
    case 12 | 1 | 2: print("Verano")
    case 3 | 4 | 5: print("Otoño")
    case 6 | 7 | 8: print("Invierno")
    case 9 | 10 | 11: print("Primavera")
    case _: print("Error")
# Otoño


coordenada = (0, 1)
match coordenada:
    case (0, 0):
        print("Coordenada en origen")
    case (x, 0):
        print(f"Coordenada en eje x: {x}")
    case (0, y):
        print(f"Coordenada en eje y: {y}")
    case (x, y):
        print(f"Coordenada en: {x}, {y}")
    case _:
        print("Error")

# Coordenada en eje y: 1