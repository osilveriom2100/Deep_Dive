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

# definicion de una funcon con varios argumentos
def my_function(a, 
                b, # esto es un comentario 
                c
                ):
    return a + b + c

# implicitamente, el salto de linea se produce al usar la barra invertida \
a = 1
b = 2
c = 3
if a > 0 and \
    b > 0 and \
    c > 0:
    print("Todos los números son positivos")

# multiline string
# los espacios en blanco al inicio de cada línea se incluyen en la cadena resultante, por lo que es importante tener cuidado con la indentación al usar esta sintaxis.  
multiline_string = """Esto es una cadena de texto
que abarca varias líneas.
Se puede usar para escribir texto largo sin necesidad de concatenar cadenas."""
print(multiline_string)

# multiline string en una función
# al igual que con cualquier otra cadena de texto, los espacios en blanco al inicio de cada línea se incluyen en la cadena resultante, por lo que es importante tener cuidado con la indentación al usar esta sintaxis dentro de una función.
# en este caso, la cadena resultante tendrá espacios en blanco al inicio de cada línea debido a la indentación de la función.
# se puede quitar la indentacion simplemente no indentando la cadena, pero esto puede afectar la legibilidad del código.
# otra opción es usar la función textwrap.dedent() del módulo textwrap para eliminar los espacios en blanco al inicio de cada línea de la cadena resultante, lo que permite mantener la legibilidad del código sin afectar el resultado final.
import textwrap
def multiline_string_function():
    a = textwrap.dedent("""\
        Esto es una cadena de texto
        que abarca varias líneas.
        Se puede usar para escribir texto largo sin necesidad de concatenar cadenas.""")
    return a
print(multiline_string_function())

def multiline_string_function():
    a = """Esto es una cadena de texto
    que abarca varias líneas.
    Se puede usar para escribir texto largo sin necesidad de concatenar cadenas."""
    return a
print(multiline_string_function())