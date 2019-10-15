#---diccionarios---
participantes = {
'nombre': 'Rossy',
'edad': 25,
'cursos': [' Python', 'React', 'Django'],
}
print(participantes['nombre'])
print(participantes['edad'])
print(participantes['cursos'])

participantes['telefono']=9811382148
participantes['ocupacion']= 'Developer'
print("==========")
print(participantes)


jugador = {}

jugador['nickname']='Rossy'
jugador['score']=0

print(jugador)

jugador['score']=60
print("El score actual de el jugador" + jugador['nickname'] + "es" str (jugador['score']))