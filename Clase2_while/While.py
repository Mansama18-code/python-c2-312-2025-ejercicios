'''#Ejemplo de encuesta.

encuestas = 0
contador_a = 0
contador_b = 0
contador_invalida = 0

while encuestas < 14:
    respuesta = input("Que producto prefiere (a o b)?: ")
    encuestas += 1
    match respuesta:
         case "a":
              contador_a += 1

         case "b":
              contador_b += 1

         case _:
              contador_invalida = contador_invalida + 1
              print ("Respuesta no válida")
              encuestas -= 1
              
    
porcentaje_a = (contador_a * 100) / encuestas
porcentaje_b = (contador_b * 100) / encuestas

print (f"Porcentaje de personas que eligen el producto A: {porcentaje_a}")
print (f"Porcentaje de personas que eligen el producto B: {porcentaje_b}")
print (f"LAS RESPUESTA NO VALIDAD SON: {contador_invalida}")
print (f"Total de Encuestas: {encuestas}")
'''

#Bool
total_notas = 0
alumnos_registrados = 0

while alumnos_registrados < 10:
     nota = input("Ingrese su nota: ")
      
     total_notas += int(nota) # Acumulador 
     alumnos_registrados += 1 # Contador
       
         

promedio = total_notas / alumnos_registrados

print (f"El promedio de las notas es: {promedio}")