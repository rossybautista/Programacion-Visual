print('''
programa de operaciones aritmeticas
Teclee una operacion, ejem: suma, resta, division, multiplicación
y dos números que desee evaluar
''')


operacion = input("Teclee la operacion:")
num1 = int(input("Teclee el primer numero"))
num2 = int(input("Teclee el segundo numero"))

if operacion == "suma":
	resultado=num1 + num2
elif operacion == "resta":
	resultado=num1 - num2
elif operacion == "division":
	resultado =num1/num2
else:
	resultado=num1 * num2


	print("El resultado de la operacion" + operacion + "es" + resultado)
	print("El resultado de la opreacion {0} es {1}").formant (opreacion, resultado)