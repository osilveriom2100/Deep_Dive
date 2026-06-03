# Sección 01 — Resumen y ejemplos

Este README agrupa y explica los conceptos manejados en los archivos de la carpeta `Seccion01`. Está pensado para estudiantes: definiciones claras, cuándo usar cada cosa y ejemplos ejecutables en Python.

---

**Contenido**
- `Class01_hierarchy.py` — Tipos y jerarquía de datos básicos
- `Class02_multi_line.py` — Líneas físicas vs lógicas, continuación de línea y cadenas multilínea
- `Class03_multi_line02.py` — Ejemplos prácticos de listas, tuplas, diccionarios y cadenas multilínea
- `Class04_identifier_names.py` — Convenciones y reglas para nombres (identificadores)
- `Class05_conditions.py` — Condicionales `if` / `elif` / `else` y operador ternario
- `Class06_functions.py` — Funciones, argumentos, anotaciones, lambdas y funciones de orden superior
- `Class07_while_loop.py` — Bucles `while`, `break`, `continue` y patrones tipo `do-while`
- `Class08_try_exceptions.py` — Manejo de excepciones con `try` / `except` / `finally`
- `Class09_for_loop.py` — Bucles `for`, `range`, `enumerate` y manejo de excepciones en iteraciones
- `Class10_classes_part1.py` — Clases: `__init__`, `__str__`, `__repr__`, `__eq__` y ejemplos
- `class10_part2.py` — Getters/Setters, `@property`, property perezosa y benchmark

---

## Guía por archivo

**`Class01_hierarchy.py` — Tipos y jerarquía**
Explica tipos numéricos (int, float, complex, Decimal, Fraction), colecciones (list, tuple, set, frozenset, dict) y otros conceptos (callable, funciones, clases, singletons como None). Ejemplos y demostraciones de uso.

Código del archivo:

```python
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
```

---

**`Class02_multi_line.py` — Líneas físicas y lógicas, continuación y cadenas multilínea**

Explica la diferencia entre líneas físicas (líneas reales en el archivo) y líneas lógicas (declaraciones que pueden abarcar varias líneas físicas). Muestra continuación explícita con `\` e implícita con paréntesis, además de cadenas multilínea con triple comillas. Recomendación: usar continuación implícita (paréntesis) en vez de `\` cuando sea posible.

Código:

```python
# python programming
# multi-line strings
# multi-line strings are created using triple quotes (''' or """)
# they can span multiple lines and preserve the formatting of the text 

# physical lines of code: son las líneas reales de código que escribimos en el editor. Cada línea de código se considera una línea física, incluso si es parte de una declaración o expresión que se extiende a varias líneas.  
x = 10
y = 20
z = x + y

# logical lines of code: son las líneas de código que se ejecutan como una sola unidad lógica.
total = (x + y + z +
        30 + 40 + 50)

# line continuation: explícita con '\\' o implícita con paréntesis
result_explicit = a + b + c + \
                30 + 40 + 50

# implicit line continuation:
result_implicit = (a + b + c +
                30 + 40 + 50)

# multi-line string
multi_line_string = """Esta es una cadena de texto
que se extiende a varias líneas.
Se pueden incluir saltos de línea y espacios en blanco."""
print("Result explicit:", result_explicit)
print("Result implicit:", result_implicit)
```

---

**`Class03_multi_line02.py` — Ejemplos prácticos de contenedores y multilinea**

Muestra cómo escribir listas, tuplas y diccionarios en varias líneas, el uso de comentarios dentro de literales y ejemplos de cadenas multilínea dentro de funciones (con `textwrap.dedent` cuando convenga para limpiar indentación).

Código:

```python
# list
a = [1, 2, 3, 4, 5]

b = [1, 2,
    3, 4, 5]

c = [1, 2,
    3, 4, # esto es un comentario
    5]

# tuple
t = (1, 
    2, # esto es un comentario 
    3)

# dict
d = {
    'name': 'Luis', # esto es un comentario
    'age': 21,      # esto es un comentario
    'city': 'Madrid'
    }

import textwrap

def multiline_string_function():
    a = textwrap.dedent("""\
        Esto es una cadena de texto
        que abarca varias líneas.
        Se puede usar para escribir texto largo sin necesidad de concatenar cadenas.""")
    return a
print(multiline_string_function())
```

---

**`Class04_identifier_names.py` — Identificadores y convenciones (PEP 8)**

Explica reglas sintácticas para nombres (comenzar con letra o `_`, no usar palabras reservadas), convenciones de estilo: `snake_case` para variables y funciones, `CamelCase` para clases, mayúsculas para constantes. Explica `_` y `__` y name-mangling.

Código:

```python
mi_variable = 10

def calcular_suma(a, b):
    return a + b

class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre
```

---

**`Class05_conditions.py` — Condicionales**

Muestra `if` / `elif` / `else`, condiciones anidadas y el operador ternario en una línea `x if cond else y`.

Código:

```python
age = 18
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You are exactly 18 years old.")
else:
    print("You are an adult.")

# operador ternario
is_raining = True
weather = "rainy" if is_raining else "sunny"
print(f"The weather is {weather}.")
```

---

**`Class06_functions.py` — Funciones y conceptos asociados**

Cubre definición de funciones con `def`, argumentos por posición y por nombre, valores por defecto, anotaciones de tipo (explicativas), funciones anidadas, recursión, asignar funciones a variables, pasar funciones como argumentos y funciones lambda. Importante: las anotaciones no son validación automática, son documentación.

Código (fragmento):

```python
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

# función que devuelve función (closure)
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_five = outer_function(5)
print(add_five(10))

# lambda
add = lambda x, y: x + y
print(add(3, 4))
```

---

**`Class07_while_loop.py` — Bucle `while`**

Explica la estructura `while`, la importancia de cambiar la condición dentro del bucle para evitar bucles infinitos, uso de `break` y `continue` y patrón para simular `do-while`.

Código:

```python
i = 1
while i <= 5:
    print(i)
    i += 1

# do-while simulado
i = 1
while True:
    print(i)
    i += 1
    if i > 5:
        break
```

---

**`Class08_try_exceptions.py` — Manejo de excepciones**

Muestra `try` / `except` para capturar `ValueError` y `ZeroDivisionError`, y `finally` para limpieza. Recomienda atrapar excepciones específicas en lugar de `except:` general.

Código:

```python
try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print(f"Result: {result}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("This block will always be executed, regardless of exceptions.")
```

---

**`Class09_for_loop.py` — Bucle `for` y utilidades**

Cubre iteración sobre listas, cadenas, `range`, uso de `enumerate` para índices y ejemplos de manejo de excepciones dentro del bucle.

Código:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)

for i, char in enumerate("hello"):
    print(i, char)
```

---

**`Class10_classes_part1.py` — Clases en Python**

Introduce `class`, `__init__`, `self`, métodos, y la sobreescritura de métodos especiales: `__str__`, `__repr__`, `__eq__`. Importancia: `__str__` para representación legible, `__repr__` para debug y `__eq__` para comparar contenido.

Código (fragmento):

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height}, area={self.area()})"
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        return NotImplemented
```

---

**`class10_part2.py` — Getters/Setters y `@property` (incluye benchmark)**

Explica la diferencia entre usar métodos `get_`/`set_` explícitos y `@property` en Python. `@property` permite exponer una API de atributo mientras ejecuta lógica detrás de escena, ideal para mantener compatibilidad cuando cambias la implementación interna.

Además incluye un ejemplo de `property` perezosa (caché) y un pequeño benchmark que compara el coste de llamar a un método, acceder a una property que recalcula y acceder a una property perezosa.

Código (fragmento):

```python
class Expensive:
    def __init__(self, n):
        self.n = n
        self._cache = None

    def compute(self):
        total = 0
        for i in range(self.n):
            total += i
        return total

    def get_value(self):
        return self.compute()

    @property
    def value(self):
        return self.compute()

    @property
    def value_cached(self):
        if self._cache is None:
            self._cache = self.compute()
        return self._cache
```

Explicación breve del benchmark: se ejecutan muchas repeticiones y se mide el tiempo de cada forma de acceso; se muestra que la primera carga de la propiedad perezosa equivale al coste del cálculo, pero accesos repetidos posteriores son muy rápidos debido a la caché.

---

## Cómo usar estos ejemplos

1. Abre una terminal en la raíz del proyecto (`Deep_Dive`).
2. Activa tu entorno virtual si lo usas.
3. Ejecuta cualquiera de los archivos dentro de `Seccion01`, por ejemplo:

```bash
python -m Seccion01.Class01_hierarchy
python -m Seccion01.class10_part2
```

Nota: los nombres de módulo son sensibles a mayúsculas si importas por módulo; en Windows la importación puede ser tolerante, pero es buen hábito mantener coincidencia exacta.

---

## Siguientes pasos recomendados para estudiantes

- Ejecuta cada archivo y modifica los ejemplos para experimentar (p. ej. cambia `n` en `Expensive` para ver efecto en el benchmark).
- Trata de convertir algunos getters/setters manuales a `@property` para ver la diferencia en la sintaxis cliente.
- Revisa PEP 8 para convenciones de nombres y estilo.

---

Si quieres, puedo:
- Añadir un README en la raíz del proyecto con instrucciones de instalación del entorno virtual.
- Generar notebooks con explicaciones interactivas.
- Extraer cada archivo completo en sub-secciones más detalladas.

