
def maximo():
    max_num = float("-inf")
    min_num= float("inf")
    cantidad = 0
    acum = 0
    acum2 = 0
    cantidad2 = 0
    print(max_num, min_num)
    respuesta = 's'

    while respuesta:
        numero= input("Ingrese un numero: ")
        numero = float(numero)

        #determino máximo
        if numero > max_num and numero > 50:
            max_num = numero
            cantidad += 1
            acum += numero

        # determino mínimo
        if numero < min_num or numero < -200:
            min_num = numero
            cantidad2 += 1
            acum2 += numero

        respuesta = input("¿Desea continuar? (s/n): ")
        if respuesta == 'n':
                print("Terminamos")
                respuesta = False
                break
        
        while respuesta != 'n' and respuesta != 's':
            respuesta = input("Por favor, ingrese una respuesta válida desea continuar? (s/n): ")
            if respuesta == "s":
                print("Continuamos")
                respuesta = True
                break
            elif respuesta == "n":
                print("Terminamos")
                respuesta = False
                break
        
        

        

        """"
        
        
        match respuesta:
            case 's':
                respuesta = True
            case 'n':
                respuesta = False
            case _:
                respuesta = input("Volvé a Ingresar (s/n): ")

        while respuesta != 's' and respuesta != 'n':
        
        
            print('PORFAVOR INGRESÁ la letra s o  la letra n')
            respuesta = input("Volvé a Ingresar (s/n): ")
            if respuesta == 's':
                respuesta = True
                break
            else:
                respuesta = False
                break
        """


        
        
        

        
    print("El máximo es", max_num, 'se repitió', cantidad, 'veces y el acumulado es', acum)
    print("El mínimo es", min_num, 'se repitió', cantidad2, 'veces y el acumulado es', acum2)


