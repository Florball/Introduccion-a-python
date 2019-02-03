# Introduccion a python

# Declarando variables
name = 'Flor'
surname = 'Ballinas'
value1 = 20
value2 = 7
birthday = '27 de agosto'
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
print('Hola, me llamo {} {}'.format(name, surname)) # Orden por defecto (implícito)
print('tengo {1} años y mi cumpleaños es el {0}'.format(birthday, age)) # Orden utilizando argumento posicional
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

# Método JOIN para concatenar
friends = ['Mario', 'Carlos', 'Luis', 'Julio', 'Bryan']
symbol = ', '
newStr = symbol.join(friends)
print(newStr)

# Operadores aritméticos
print('¡Ahora sumemos!')
firstValue = int(input('Ingresa un valor: '))
secondValue = int(input('Ingresa un segundo valor: '))
result = firstValue + secondValue
print('{} + {} = {}'.format(firstValue, secondValue, result))
