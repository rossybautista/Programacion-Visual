# Crea una función que calcule el factorial de un número pasado por parámetro

def factorial(num):
     
    resultado = num
 
    for i in range(num-1,1,-1):
        resultado = resultado * i
 
    return resultado
 
print(factorial(5))