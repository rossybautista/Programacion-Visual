# Crea una función que dados dos números mostrara todos los números que hay entre ellos


def numerosEntre(num1, num2):
     
    if (num1 > num2):
 
        aux = num1
        num1 = num2
        num2 = aux
 
    for i in range(num1+1, num2):
        print(i)
 
numerosEntre(5,10)