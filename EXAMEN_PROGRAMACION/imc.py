#Escribe un programa llamado imc.py que pida al usuarui su peso (en kg) y estatura (en metros), calcule el índice de masa
#corporal y lo almacene en una variable e imprima por pantall la frase Tu índice de masa corporal es <imc> y tienes <rango>
#Y <rango> es la descripción del indice corporal.


personas = int(input( "personas: "))


while personas > 0:
    n = input("Su nombre por favor: ")
    e = int(input("Su edad en años por favor: "))
    a = float(input ("Su altura en metros por favor: "))
    est = a
    m = float (input("Su masa en kilogramos por favor :"))
    IMC = m / est**2
    if(e < 18):
        print("Usted es menor de edad")
    else:
        print("Usted es mayor de edad")
    print("IMC: " + str(IMC) )

    if IMC >= 0 and IMC <= 15.99 :
        print ("Delgadez severa")
    elif IMC >= 16.00 and IMC <= 16.99 :
        print ("Delgadez moderada")
    elif IMC >= 17.00 and IMC <= 18.49:
        print ("Delgadez leve")
    elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Normal")
    elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        print ("obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.00:
        print ("obesidad media")
    elif IMC >= 40.00:
        print ("obesidad morbida")
    personas = personas - 1
