#Escribe un programa llamado diccionario.py que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un
#diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

nombre = input('¿Cómo te llamas? ')
años = input('¿Cuántos años tienes? ')
dirección = input('¿Cuál es tu dirección? ')
teléfono = input('¿Cuál es tu número de teléfono? ')
persona = {'nombre': nombre, 'años': años, 'dirección': dirección, 'teléfono': teléfono}
print(persona['nombre'], 'tiene', persona['años'], 'años, vive en', persona['dirección'], 'y su número de teléfono es', persona['teléfono'])