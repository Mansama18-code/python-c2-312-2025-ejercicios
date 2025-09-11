
def funcion_recursiva(valor_tope: int):#8, 
    print("Funcion recursiva llamada con n =", valor_tope)
    if valor_tope <= 1:
        print("Caso base alcanzado con n =", valor_tope)
        resultado = valor_tope #1
    else:
        resultado =  valor_tope + funcion_recursiva(valor_tope - 1) #7, #6, 5, 4, 3, 2, 1
        print(f'EL VALOR DE RESULTADO ES: {resultado} en el llamado de la función # {valor_tope}')
    return resultado 

def sumar_naturales(numero: int, valor_inicial: int) -> int:
    
    if valor_inicial != numero: #NUMERO ES EL NUMERO NATURAL TOPE
        #print(f"LLAMADO NUMERO: {otro_numero}, Valor de partida: {otro_numero} y numero a sumar es {numero}")
        resultado = valor_inicial + sumar_naturales(numero, valor_inicial+1)
        #FORMULA PARA COTEJAR LA SUMATORIA (numero * (numero + 1))/2 
    else: 
        #print(f"ULTIMO LLAMADO {otro_numero}")
        resultado = valor_inicial

    print(f'EL VALOR DE RESULTADO ES: {resultado} en el llamado de la función # {valor_inicial}')
    return resultado

"""


"""

def sumar_digitos(numero: int) -> int:
   
    numero_str = str(numero)
    tamano_numero = len(numero_str ) - 1
    if tamano_numero < 1: 
        resultado = int(numero_str[tamano_numero])
    else: 
        resultado = int(numero_str[tamano_numero]) + sumar_digitos(int(numero_str[tamano_numero - 1]))
    return resultado 
    
    
    

def suma_digitos(numero):
    if numero < 10:
        return numero
    else:
        print(numero %10, numero //10)
        return numero % 10 + suma_digitos(numero // 10)
        
