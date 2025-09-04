from .Funciones_operaciones import *
from .validacion import validar_opciones

def activar_calculadora():
    
    contador = 0
    contador2 = 0
    respuesta2 = True
    mensaje_de_error = "Por favor, ingrese una respuesta válida desea continuar? (s/n): "
    #opcion = int(input('Ingresar la operación que quiere hacer: 1. Resta. 2. Suma: '))
    nombre = input('Ingrese su nombre: ')
    while respuesta2 == True:
        
        opcion = input(nombre + 'Ingresar la opción a calcular: \n- Para Resta. \n+ Para Suma: \n tipo Paso de valor: \n')

    
        a = input('ingresar valor de a: ')
        a = int(a)

        b = input('ingresar valor de b: ')
        b = int(b)

        match opcion:
            #case 1:
            case '-':
                resultado = restar(a, b)
                contador += 1
            #case 2:
            case '+':
                resultado = sumar(a, b)
                contador += 1
            case 'tipo':
                a2 = a
                
                b2 = b + 1
                print(f'EL ESPACIO DE MEMORIA PARA a ES: {id(a)} para a2 {id(a2)}y para b ES: {id(b)} para b2 {id(b2)}')
                b = b + 1
                print(f'EL ESPACIO DE MEMORIA PARA a ES: {id(a)} para a2 {id(a2)}y para b ES: {id(b)} para b2 {id(b2)}')

            case _:
                resultado = 0
                contador2 += 1
                print('Error, ingrese una operación válida')


        respuesta = input("¿Desea continuar? (s/n): ")
        respuesta2 = validar_opciones(respuesta, mensaje_de_error, nombre)
        

        print(f'La Suma es: {resultado}')

    print(f'Se realizaron {contador} operaciones de suma y resta. Las operaciones no validas fueron de {contador2}')
    print()
    #otra_variable = suma
    #print(f'El espacio de memoria de la variable {suma} es {id(suma)} y si añadimos en otra variables es: {id(otra_variable)}')



   