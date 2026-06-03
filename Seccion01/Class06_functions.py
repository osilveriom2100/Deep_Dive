# functions
# son bloques de código reutilizables que realizan una tarea específica.
# se definen utilizando la palabra clave "def" seguida del nombre de la función y paréntesis que pueden contener parámetros (opcional), y luego dos puntos (:). El código dentro de la función debe estar indentado.
# la sintaxis básica para definir una función es:
# def function_name(parameters):
#     # code block
#     return value (opcional)

# mandar a llmar packages y módulos
# un módulo es un archivo que contiene definiciones y declaraciones de Python, como funciones, clases, variables, etc. Un paquete es una colección de módulos organizados en un directorio que contiene un archivo "__init__.py" para indicar que es un paquete.
# para importar un módulo o paquete se utiliza la palabra clave "import" seguida del nombre del módulo o paquete. También se pueden importar funciones, clases o variables específicas de un módulo utilizando la sintaxis "from module_name import function_name".
# ejemplos de funciones 
def greet(name):
    return f"Hello, {name}!"
def add(a, b):
    return a + b

# ejemplo de importar un módulo
import math
print(math.sqrt(16))  # imprime la raíz cuadrada de 16
# ejemplo de importar una función específica de un módulo
from math import sqrt
print(sqrt(25))  # imprime la raíz cuadrada de 25

# en una funcion se puede especificar un valor por defecto para un parámetro, lo que significa que si no se proporciona un valor para ese parámetro al llamar a la función, se utilizará el valor por defecto. Esto se hace asignando un valor al parámetro en la definición de la función.
def greet(name="World"):
    return f"Hello, {name}!"    
print(greet())  # imprime "Hello, World!" porque no se proporciona un valor para el parámetro "name"

# también se pueden usar argumentos posicionales y argumentos con nombre al llamar a una función. Los argumentos posicionales se asignan a los parámetros en el orden en que se proporcionan, mientras que los argumentos con nombre se asignan a los parámetros utilizando su nombre.
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
print(greet("Alice"))  # imprime "Hello, Alice!" porque se proporciona un valor para el parámetro "name" y se utiliza el valor por defecto para el parámetro "greeting"
print(greet("Bob", greeting="Hi"))  # imprime "Hi, Bob!" porque se proporciona un valor para el parámetro "name" y se proporciona un valor específico para el parámetro "greeting" utilizando un argumento con nombre

# puden especificar que tipo de dato se espera para los parámetros utilizando anotaciones de tipo, lo que puede ayudar a mejorar la legibilidad del código y facilitar la detección de errores. Las anotaciones de tipo no son obligatorias y no afectan el comportamiento del programa, pero pueden ser útiles para documentar el código y proporcionar información adicional a los desarrolladores.
# name: str indica que se espera que el parámetro "name" sea de tipo cadena (string), 
# greeting: str = "Hello" indica que se espera que el parámetro "greeting" sea de tipo cadena y tiene un valor por defecto de "Hello", y 
# -> str indica que la función devuelve un valor de tipo cadena. 
# en caso de que se proporcione un valor para el parámetro "greeting" que no sea una cadena, o si la función devuelve un valor que no sea una cadena, esto no generará un error en tiempo de ejecución, pero puede ser confuso para los desarrolladores que lean el código y puede dificultar la detección de errores. Por lo tanto, es importante utilizar las anotaciones de tipo de manera consistente y asegurarse de que los valores proporcionados para los parámetros y los valores devueltos por la función coincidan con las anotaciones de tipo especificadas.
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"
print(greet("Charlie"))  # imprime "Hello, Charlie!" porque se proporciona un valor para el parámetro "name" y se utiliza el valor por defecto para el parámetro "greeting"
print(greet("Dave", greeting="Hi"))  # imprime "Hi, Dave!" porque se proporciona un valor para el parámetro "name" y se proporciona un valor específico para el parámetro "greeting" utilizando un argumento con nombre 

# definir una funcion dentro de otra funcion
# esto se conoce como funciones anidadas o funciones internas, y puede ser útil para organizar el código y evitar la contaminación del espacio de nombres global. Las funciones internas pueden acceder a las variables y parámetros de la función externa, lo que permite compartir información entre las funciones.
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function
add_five = outer_function(5)  # crea una función interna que suma 5 a su argumento
print(add_five(10))  # imprime 15 porque la función interna suma 5 a 10

# tambien se puede mandar a llamar una función dentro de otra función, lo que se conoce como funciones recursivas. Las funciones recursivas son aquellas que se llaman a sí mismas, ya sea directa o indirectamente, para resolver un problema dividiéndolo en subproblemas más pequeños. Es importante tener una condición de terminación para evitar que la función se llame a sí misma indefinidamente.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # imprime 120 porque el factorial de 5 es 5 * 4 * 3 * 2 * 1 = 120

# funciones se conoce como recursión indirecta, donde una función llama a otra función, que a su vez llama a la primera función. En este caso, function_1 llama a function_2, y function_2 imprime un mensaje. Aunque no hay una llamada directa a sí misma, se puede considerar que ambas funciones están involucradas en un proceso recursivo. 
def function_1():
    return function_2()
def function_2():
    print("Hello from function_2!")
function_1()  # imprime "Hello from function_2!" porque function_1 llama a function_2, que imprime el mensaje.

# se puede asginar una función a una variable, lo que permite llamar a la función utilizando el nombre de la variable. Esto se conoce como funciones de primera clase, y es una característica importante de Python que permite tratar las funciones como objetos de primera clase.
def greet(name):
    return f"Hello, {name}!"
greet_function = greet  # asigna la función "greet" a la variable "greet_function"
print(greet_function("Eve"))  # imprime "Hello, Eve!" porque se llama a la función utilizando el nombre de la variable "greet_function" 

# también se pueden pasar funciones como argumentos a otras funciones, lo que permite crear funciones de orden superior que pueden operar en otras funciones. Esto es útil para crear funciones más flexibles y reutilizables.
def apply_function(func, value):
    return func(value)  
def square(x):
    return x * x
print(apply_function(square, 5))  # imprime 25 porque la función "apply_function" llama a la función "square" con el valor 5, lo que devuelve 25    

# labda functions
# son funciones anónimas, es decir, funciones que no tienen un nombre. Se definen utilizando la palabra clave "lambda" seguida de los parámetros, dos puntos (:) y el cuerpo de la función. Las funciones lambda son útiles para crear funciones simples y concisas que se pueden usar en lugares donde se espera una función, como en funciones de orden superior o en expresiones de filtrado.
# la sintaxis básica para definir una función lambda es:
# lambda parameters: expression
# ejemplo de función lambda que suma dos números
add = lambda x, y: x + y
print(add(3, 4))  # imprime 7 porque la función lambda suma 3 y 4, lo que devuelve 7
# ejemplo de función lambda que filtra una lista de números para obtener solo los números pares
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # imprime [2, 4, 6] porque la función lambda filtra los números pares de la lista "numbers", lo que devuelve una nueva lista con los números pares.    
