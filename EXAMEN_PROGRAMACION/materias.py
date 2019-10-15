#Escribir un programa llamado materias.py que pida el numero de asignaturas que se desean agregar,Que pida el nombre de las asignaturas dadas y las almacene en una lista y la muestre por pantalla.


numero = int(input("cuantas materias deseas introducir: "))

if numero < 1:
    print("¡Teclee por lo menos una!")
else:
    lista = []
    for i in range(numero):
        print("Escriba el nombre de la materia", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("Tus materias son:", lista)