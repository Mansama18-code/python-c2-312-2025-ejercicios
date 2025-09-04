#Acumulador

acumulador = 0
valor = None
x = True

while x == True:
    #valor = input("Ingrese un valor")
    valor = int (valor)
    acumulador += valor
    print (f"El acumulador es: {acumulador}")
    valor += 1
    if valor == 20: 
        x = False
    
print (f"El acumulador final es: {acumulador}")
'''
while valor == None or edad > 98 or edad < 18: 
    edad_str = input("Ingrese su edad: ")
    if edad_str.isdigit():
        edad = int(edad_str)
        if edad >= 18:
            print("Eres mayor de edad.")
        else:
            print("Eres menor de edad.")

print(type(edad), edad)'''