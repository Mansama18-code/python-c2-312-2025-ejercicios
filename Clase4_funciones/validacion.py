#Validación
def validar_opciones(respuesta: str, mensaje_de_error: str, nombre: str) -> bool:
        """
        Esta función valida las opciones.
        Args:
            - respuesta del usuario (s/n) para continuar o no
        Return: 
            - un valor booleano de True o False

        """
        
        if respuesta == 'n':
            print("Terminamos")
            respuesta2 = False

        elif respuesta == 's':
            print("Continuamos")
            respuesta2 = True
                
        
        while respuesta != 'n' and respuesta != 's':
            respuesta = input(nombre + mensaje_de_error)
            if respuesta == "s":
                print("Continuamos")
                respuesta2 = True
                break
            elif respuesta == "n":
                print("Terminamos")
                respuesta2 = False
                break
        return respuesta2
