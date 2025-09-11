#Importar Paquetes
from Clase4_funciones.validacion import validar_valor_incial
from Clase6_funciones_recursivas.funcion_recursiva import sumar_naturales, funcion_recursiva, sumar_digitos

"""
n = int(input("Ingrese el numero a sumar:"))
valor_incial = int(input("Ingrese el valor incial:"))

#resultado2 = funcion_recursiva(n)
if validar_valor_incial(valor_incial, n) == True:
    print("INICIA EL PRIMER LLAMADO de LA FUNCION")
    resultado = sumar_naturales(n,valor_incial)
    
else: 
    resultado = n

print(f'El resultado de la suma de el numero natural {n} es: {resultado}')
"""

print(sumar_digitos(111))

