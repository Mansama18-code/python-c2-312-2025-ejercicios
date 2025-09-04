from .auxiliares import (
    sumar_fila, obtener_totales_marcas, obtener_indice_minimo,
    obtener_indice_maximo, obtener_cantidad_deposito_almacenamiento_2,
    inicializar_matriz
)
from .mostrar_datos import (
    mostrar_matriz, mostrar_dato, generar_encabezado_separador,
    mostrar_dato_porcentual
)
from .ordenamiento import selection_sort

import random as rd

# 1 - Obtener existencias: para ello deberá crear una función que cargue la existencia de
#     cada smartphone en todos los depósitos.
def pp_obtener_existencias(matriz: list[list]) -> None:
    inicializar_matriz(matriz)
    mostrar_matriz(matriz)
    

# 2 - Calcular por cada depósito la cantidad total de unidades almacenadas entre todos los
#         smartphones.
def pp_mostrar_suma_fila(matriz: list[list], fila: int, campo_suma: str) -> float:
    suma = sumar_fila(matriz, fila)
    mensaje = f'La cantidad total de {campo_suma} es de {suma}'
    print(mensaje)

# 3 - Nombre del smartphone que almaceno menos unidades en cada depósito.
def pp_obtener_menos_unidades_totales(matriz: list[list]):
    
    if matriz and matriz[0]:
        indice_menor = None
    
        for indice in range(len(matriz[1])):
            if indice_menor == None or matriz[1][indice] < matriz[1][indice_menor]:
                indice_menor = indice
        
        marca = matriz[0][indice_menor]
        cantidad = matriz[1][indice_menor]
        texto = f'La marca que menos unidades tiene es {marca} con '\
            f'{cantidad} unidades y está en el deposito N° {indice_menor+1}'
        print(texto)
    else:
        print('La matriz no esta inicializada')

# 4 - Máxima cantidad de unidades almacenados de cada smartphone.
def pp_obtener_minimo_smartphones(matriz: list[list], indice_fila: int = 1) -> None:
    matriz_cantidades = obtener_totales_marcas(matriz)
    indice_minimo = obtener_indice_minimo(matriz_cantidades, indice_fila)
    mensaje = f'La marca con menos cantidad de unidades es {matriz_cantidades[0][indice_minimo]} '\
        f'con {matriz_cantidades[1][indice_minimo]} unidades'
    print(mensaje)

# 5 - Depósito con mayor recaudación, teniendo en cuenta que disponemos de un vector
#        con los valores por unidad de cada marca de smartphone.
def pp_obtener_mayor_recaudacion(matriz: list[list], indice_fila: int = -1):
    indice_maximo = obtener_indice_maximo(matriz, indice_fila)
    mensaje = f'El deposito con mayor recaudacion es el deposito N° {indice_maximo + 1} de la marca {matriz[0][indice_maximo]} '\
        f'con $ {matriz[3][indice_maximo]:.2f}'
    print(mensaje)

# 6 - Cantidad de depósitos que hayan almacenado más de 50000 unidades entre las 4 marcas de
#        smartphone.
def pp_mostrar_depositos_mayores_de(matriz: list[list], fila: int, mas_de: int):
    indices_depos = obtener_cantidad_deposito_almacenamiento_2(matriz, fila, mas_de)
    cantidad = len(indices_depos)
    
    mensaje = f'Hay {cantidad} de depositos con mas de {mas_de} unidades de smartphones'
    print(mensaje)
    
    encabezado = '| Indice Actual | Deposito |    Marca   | Cantidad | Precio Unit  |     Ganancias    |'
    encabezado = generar_encabezado_separador(encabezado)
    print(encabezado)
    for indice in indices_depos:
        mostrar_dato(matriz, indice)

# 7 - Porcentaje de unidades de cada marca de smartphone sobre el total de unidades 
#        almacenadas. Además mostrar la marca del smartphone con el máximo porcentaje 
#        sobre el total almacenado.
def pp_obtener_porcentaje_por_marca(matriz: list[list]) -> None:
    matriz_cantidades = obtener_totales_marcas(matriz)
    cantidad_total_celu = sumar_fila(matriz_cantidades, 1)
    porcentajes = []
    matriz_cantidades.append(porcentajes)
    
    for cantidad in matriz_cantidades[1]:    
        porcentaje_actual = cantidad * 100 / cantidad_total_celu
        matriz_cantidades[2].append(porcentaje_actual)
    
    
    # Porcentaje de unidades de cada marca de smartphone sobre el total de unidades 
    #almacenadas
    cant_columnas = len(matriz_cantidades[0])
    
    encabezado = '|    Marca   |   Canti  | Porcent  | '
    encabezado = generar_encabezado_separador(encabezado)
    print(encabezado)
    
    for indice_columna in range(cant_columnas):
        mostrar_dato_porcentual(matriz_cantidades, indice_columna)
    
    indice_maximo = obtener_indice_maximo(matriz_cantidades, 2)
    
    print('\nDatos del smartphone con mayor porcentaje de unidades:')
    
    encabezado = '|    Marca   |   Canti  | Porcent  | '
    encabezado = generar_encabezado_separador(encabezado)
    print(encabezado)
    mostrar_dato_porcentual(matriz_cantidades, indice_maximo)

def pp_ordenar_matriz_mostrar(matriz: list[list], fila_ordenar: int):
    selection_sort(matriz, fila_ordenar)
    mostrar_matriz(matriz)