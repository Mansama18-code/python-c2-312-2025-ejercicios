""""
Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada 
la carga determinar:
La suma acumulada de los números negativos.
La suma acumulada de los números positivos.
La cantidad de números negativos ingresados.
El promedio de los números positivos.
El número positivo más grande.
El porcentaje de números negativos ingresados, respecto del total de ingresos.
"""

#VARIABLES

cont_negativos = 0
cont_positivos = 0
sum_negativos = 0
sum_positivos = 0
prom_positivos = 0
positivo_mas_grande = 0
porcentaje_negativos = 0
total_numeros = 0

#INGRESO DE DATOS

condicion = True
while condicion == True:
    numeros = int(input('Ingresar Un Número: '))
    if numeros < 0:
        cont_negativos += 1
        sum_negativos += numeros
        total_numeros += 1
        print(f"El número {numeros} es negativo")
    elif numeros > 0:
        cont_positivos += 1
        sum_positivos += numeros
        total_numeros += 1
        if numeros > positivo_mas_grande:
            positivo_mas_grande = numeros
        print(f"El número {numeros} es positivo")
    else:
        print('El número es cero')

    pregunta = input('Desea ingresar otro número (S/N): ')
    while pregunta != 'S' and pregunta != 'N':
        print('Error, ingrese S o N')
        pregunta = input('Desea ingresar otro número (S/N): ')
        if pregunta == 'N':
            condicion = False
            break
        elif  pregunta == 'S':
            condicion = True
            break

#A
print('La suma acumulada de los números negativos es: ', sum_negativos)

#B
print('La suma acumulada de los números positivos es: ', sum_positivos)

#C
print('La cantidad de números negativos ingresados es: ', cont_negativos)

#D
if cont_positivos != 0:
    prom_positivos = sum_positivos / cont_positivos
    print('El promedio de los números positivos es: ', prom_positivos)
    #E
    print('El número positivo más grande es: ', positivo_mas_grande)

else: 
    print('No se ingresaron números positivos, por lo tanto no se calcula promedio ' \
    'ni el número positivo más grande.')

#F
if total_numeros != 0:
    porcentaje_negativos = (cont_negativos / total_numeros) * 100
    print('El porcentaje de números negativos ingresados respecto del total es: ', porcentaje_negativos, '%')

