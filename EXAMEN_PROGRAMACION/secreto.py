#Escribe un programa llamada secreto.py que almacene una palabra en una variable y pregunte al usuario por la palabra e
#imprima por pantala si la plalabra introducida por el usuario coincide con la guardada en la variable sin tener encuenta 
#mayúsculas y minúsculas.


secreto = "riverdale"
palabra = input("Ingresa tu palabra secreta: ")
if secreto == palabra:
    print("Es correcto")
else:
    print("es incorrecto")