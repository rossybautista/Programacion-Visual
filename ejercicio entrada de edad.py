# Validar si es mayor de edad (18) puedes votar



""" 
if - elif - else
La entrada para menores de 4 años es gratuita.
La entrada para cualquier persona entre las edades de 4 y 18 años es de $50.
La entrada para cualquier persona mayor de 18 años es de $100.
"""
edad=int(input('ingresa tu edad:'))

if edad<4:
	precio=0
elif edad<18:
	precio=50
else:
	precio=100

print("La entrada te va a costar $" + str (precio))