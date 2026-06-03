# python type hierarchy

# number: es un tipo de dato que representa valores numéricos, como enteros (int) y números de punto flotante (float).
num_int = 42  # ejemplo: int
num_float = 3.1415  # ejemplo: float

# integral: es un tipo de dato que representa números enteros, sin parte decimal. En Python, se representa con el tipo de dato int.
integral_example = -7  # int (integral)

# integer: es un tipo de dato que representa números enteros, sin parte decimal. En Python, se representa con el tipo de dato int.
# boolean: es un tipo de dato que representa valores de verdad, es decir, True (verdadero) y False (falso). En Python, se representa con el tipo de dato bool.
is_active = True  # bool (boolean)


# non-integral: es un tipo de dato que representa números que pueden tener una parte decimal, como los números de punto flotante (float) en Python.

# float: es un tipo de dato que representa números de punto flotante, es decir, números que pueden tener una parte decimal. En Python, se representa con el tipo de dato float. 
# ejemplo float
pi = 3.14
# complex: es un tipo de dato que representa números complejos, que consisten en una parte real y una parte imaginaria. En Python, se representa con el tipo de dato complex.   
# ejemplo complex
z = 1 + 2j
# decimal: es un tipo de dato que representa números decimales con una precisión fija. En Python, se puede utilizar el módulo decimal para trabajar con números decimales de alta precisión.    
# ejemplo decimal (usa el módulo decimal)
from decimal import Decimal
price = Decimal('19.99')
# fraction: es un tipo de dato que representa números racionales como una fracción, con un numerador y un denominador. En Python, se puede utilizar el módulo fractions para trabajar con fracciones.   
# ejemplo fraction
from fractions import Fraction
half = Fraction(1, 2)

# collection: es un tipo de dato que representa un conjunto de elementos, como listas, tuplas, conjuntos y diccionarios en Python.


# sequence: es un tipo de dato que representa una colección ordenada de elementos, como listas y tuplas en Python.
# mutable sequence: es un tipo de dato que representa una colección ordenada de elementos que se pueden modificar, como las listas en Python.
# list: es un tipo de dato que representa una colección ordenada de elementos que se pueden modificar. En Python, se representa con el tipo de dato list.

# ejemplo list (mutable sequence)
sample_list = [1, 2, 3]
sample_list.append(4)

# immutable sequence: es un tipo de dato que representa una colección ordenada de elementos que no se pueden modificar, como las tuplas en Python.
# tuple: es un tipo de dato que representa una colección ordenada de elementos que no se pueden modificar. En Python, se representa con el tipo de dato tuple.  
# string: es un tipo de dato que representa una secuencia de caracteres. En Python, se representa con el tipo de dato str.  

# ejemplo tuple (immutable)
sample_tuple = (1, 2, 3)

# ejemplo string
greeting = 'hola'

# set: es un tipo de dato que representa una colección no ordenada de elementos únicos. En Python, se representa con el tipo de dato set.
# mutable set: es un tipo de dato que representa una colección no ordenada de elementos únicos que se pueden modificar, como los conjuntos en Python.
# frozenset: es un tipo de dato que representa una colección no ordenada de elementos únicos que no se pueden modificar, como los conjuntos congelados en Python. En Python, se representa con el tipo de dato frozenset.   

# ejemplo set / frozenset
unique_set = {1, 2, 3}
frozen = frozenset({1, 2, 3})

# mapping: es un tipo de dato que representa una colección de pares clave-valor, como los diccionarios en Python.
# dict: es un tipo de dato que representa una colección de pares clave-valor. En Python, se representa con el tipo de dato dict.

# ejemplo dict (mapping)
student = {'name': 'Luis', 'age': 21}

# callable: es un tipo de dato que representa objetos que se pueden llamar, como funciones, métodos y clases en Python.

# ejemplo callable: función y clase
def doble(x):
	return x * 2

class MiClase:
	def __call__(self, v):
		return v + 1

callable_instance = MiClase()

# user-defined function: es un tipo de dato que representa una función definida por el usuario. En Python, se puede crear una función utilizando la palabra clave def.
# generator function: es un tipo de dato que representa una función que devuelve un generador, que es un objeto iterable que produce una secuencia de valores. En Python, se puede crear una función generadora utilizando la palabra clave def y la declaración yield.
# class: es un tipo de dato que representa una plantilla para crear objetos. En Python, se puede crear una clase utilizando la palabra clave class. 
# instance method: es un tipo de dato que representa un método que se puede llamar en una instancia de una clase. En Python, se define un método dentro de una clase utilizando la palabra clave def.
# class instance: es un tipo de dato que representa un objeto creado a partir de una clase. En Python, se puede crear una instancia de una clase llamando a la clase como si fuera una función, pasando los argumentos necesarios para inicializar el objeto.   
# ejemplo user-defined function y generator
def my_function(x, y):
	return x + y

def my_generator(n):
	for i in range(n):
		yield i

gen = my_generator(3)

# ejemplo class, instance, instance method
class Animal:
	def __init__(self, especie):
		self.especie = especie

	def sonido(self):
		return f"sonido de {self.especie}"

animal = Animal('gato')

# built-in function: es un tipo de dato que representa una función incorporada en Python, como print() o len(). Estas funciones están disponibles de forma predeterminada y no requieren importación. En Python, se representan con el tipo de dato builtin_function_or_method. 
# built-in method: es un tipo de dato que representa un método incorporado en Python, como append() para listas o keys() para diccionarios. Estas funciones están disponibles de forma predeterminada y no requieren importación. En Python, se representan con el tipo de dato builtin_function_or_method. 

# ejemplo built-in function / method
builtin_example = len  # función incorporada
sample_list.append(5)  # método incorporado en lista

# singletons: es un tipo de dato que representa objetos únicos en Python, como None, True y False. Estos objetos son instancias de sus respectivas clases y se utilizan para representar valores especiales en el lenguaje. En Python, se representan con el tipo de dato NoneType para None, bool para True y False.   
# None: es un tipo de dato que representa la ausencia de valor o la falta de un valor. En Python, se representa con el tipo de dato NoneType.
# notimplemented: es un tipo de dato que representa una función o método que aún no ha sido implementado. En Python, se representa con el tipo de dato NotImplementedType.  
# ellipsis: es un tipo de dato que representa una elipsis, que es un marcador de posición para indicar que falta código o que se debe completar algo. En Python, se representa con el tipo de dato EllipsisType.    

# ejemplo singletons
none_example = None
notimpl_example = NotImplemented
ellipsis_example = ...

if __name__ == '__main__':
	# Demostración rápida de algunos valores y tipos
	print('num_int', num_int, type(num_int))
	print('num_float', num_float, type(num_float))
	print('integral_example', integral_example, type(integral_example))
	print('is_active', is_active, type(is_active))
	print('pi', pi, type(pi))
	print('z', z, type(z))
	print('price', price, type(price))
	print('half', half, type(half))
	print('sample_list', sample_list)
	print('sample_tuple', sample_tuple)
	print('greeting', greeting)
	print('unique_set', unique_set)
	print('frozen', frozen)
	print('student', student)
	print('doble(3)', doble(3))
	print('callable_instance(4)', callable_instance(4))
	print('next gen ->', next(gen))
	print('animal.sonido()', animal.sonido())
	print('builtin_example(lst)', builtin_example(sample_list))
	print('none_example', none_example)
	print('notimpl_example', notimpl_example)
	print('ellipsis_example', ellipsis_example)

