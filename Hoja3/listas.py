'''
3. Crea una lista, pide al usuario definir cuantos elementos va a tener
y haz que la rellene de números dinámicamente.
Tiene prohibido escribir cualquier cosa que no sean enteros.
'''

tamanio=int(input("Introduzca la longitud de tu lista:) "))
lista = []
for i in range(0, tamanio):
    numero= int(input("Introduce tu numero: "))
    lista.append(numero)

print(len(lista))
