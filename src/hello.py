# Introduccion a python

# Declarando variables
name = 'Flor'
surname = 'Ballinas'
value1 = 20
value2 = 7
birthday = '27/08'
age = value1 + value2

# Listas en Python
from collections import deque # Usando collections.deque
weekdays = deque(['strawberry', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday'])

# Métodos para las listas
# Añadiendo elemento al final
weekdays.append('saturday')
# Eliminando último elemento añadido (derecho)
weekdays.pop()
# Eliminando el primero elemento (izquierdo)
weekdays.popleft()

# Imprimiendo str, variables y tipo de variable
print('hello world')
print(name + ' ' + surname)
# Dando formato a los strings
print('Hola, me llamo {} {}'.format(name, surname)) # Por defecto
print('tengo {1} años y mi cumpleaños es el {0}'.format(birthday, age)) # Utilizando marcadores de posicion
# Impriendo lista 
print(weekdays)
print(type(weekdays))

# Condicionales
if value1 > value2 : 
  print('El primer valor es mayor que el segundo valor')
elif value1 == value2 :
  print('Ambos valores son iguales')
else:
  print('El primer valor es menor que el segundo valor')

# Buscando un elemento en la lista weekdays
if 'monday' in weekdays :
  print('Se encontró monday en la lista')
else :
  print('No se encontró monday en la lista')

# If anidado
positiveNumbers = [-4, -2, 0, 2, 4]

