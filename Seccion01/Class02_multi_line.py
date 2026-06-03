# python programming
# multi-line strings
# multi-line strings are created using triple quotes (''' or """)
# they can span multiple lines and preserve the formatting of the text 

# physical lines of code: son las líneas reales de código que escribimos en el editor. Cada línea de código se considera una línea física, incluso si es parte de una declaración o expresión que se extiende a varias líneas.  
# terminan con un salto de línea, lo que indica el final de una línea física. En Python, las líneas físicas pueden ser continuadas utilizando el carácter de barra invertida (\) o mediante la continuación de línea implícita dentro de paréntesis (), corchetes [] o llaves {}.   
# ejemplo de physical lines of code:
x = 10
y = 20
z = x + y

# logical lines of code: son las líneas de código que se ejecutan como una sola unidad lógica. Una declaración o expresión que se extiende a varias líneas físicas se considera una sola línea lógica.
# terminan con un salto de línea, lo que indica el final de una línea lógica. En Python, las líneas lógicas pueden ser continuadas utilizando el carácter de barra invertida (\) o mediante la continuación de línea implícita dentro de paréntesis (), corchetes [] o llaves {}.
# ejemplo de logical lines of code:
total = (x + y + z +
        30 + 40 + 50)

# line continuation: es el proceso de dividir una declaración o expresión en varias líneas físicas para mejorar la legibilidad del código. En Python, se puede usar el carácter de barra invertida (\) para indicar que una declaración o expresión continúa en la siguiente línea física.
# ejemplo de line continuation:
result = x + y + z + \
            30 + 40 + 50

# implicit line continuation: es el proceso de dividir una declaración o expresión en varias líneas físicas sin usar el carácter de barra invertida (\). En Python, se puede dividir una declaración o expresión en varias líneas físicas si está dentro de paréntesis (), corchetes [] o llaves {}. Esto se conoce como continuación de línea implícita.
# ejemplo de implicit line continuation:
numbers = [1, 2, 3,
            4, 5, 6,
            7, 8, 9]

# multi-line string: es una cadena de texto que se extiende a varias líneas físicas. En Python, se puede crear una cadena de texto de varias líneas utilizando triple comillas (''' o """). Las cadenas de texto de varias líneas pueden contener saltos de línea y espacios en blanco, y se preservan tal como se escriben en el código.
# ejemplo de multi-line string:
multi_line_string = """Esta es una cadena de texto
que se extiende a varias líneas.
Se pueden incluir saltos de línea y espacios en blanco."""

# tokenized: es el proceso de dividir el código fuente en unidades léxicas llamadas tokens. En Python, el proceso de tokenización se realiza durante la fase de análisis léxico del compilador, donde el código fuente se divide en tokens que representan palabras clave, identificadores, literales, operadores y otros elementos del lenguaje. La tokenización es un paso importante en la compilación y ejecución del código, ya que permite al intérprete o compilador entender la estructura y el significado del código fuente.
# ejemplo de tokenización:
# el siguiente código fuente se tokeniza en los siguientes tokens:
# x: identificador
# =: operador de asignación
# 10: literal entero
x = 10

# physical line vs logical line: la diferencia entre una línea física y una línea lógica es que una línea física es la línea real de código que escribimos en el editor, mientras que una línea lógica es la unidad de código que se ejecuta como una sola declaración o expresión. Una declaración o expresión que se extiende a varias líneas físicas se considera una sola línea lógica. Por ejemplo, en el siguiente código, las líneas físicas son las líneas individuales de código, mientras que la línea lógica es la declaración completa que se ejecuta como una sola unidad:
total = (x + y + z +
        30 + 40 + 50)

# Continuación de línea: implícita vs explícita
# Explicación breve:
# - Continuación explícita: se usa la barra invertida (\) al final de la línea para indicar
#   que la expresión continúa en la siguiente línea física. Es más frágil (no debe haber
#   espacios ni comentarios después de la barra) pero funciona fuera de paréntesis.
# - Continuación implícita: se encierra la expresión en paréntesis, corchetes o llaves
#   y Python continúa la expresión automáticamente en las líneas siguientes. Es más
#   legible y recomendable.

# --- Ejemplo explícito (barra invertida) ---
a = 1
b = 2
c = 3
result_explicit = a + b + c + \
                30 + 40 + 50

# Nota: la línea que termina en '\' no puede tener espacios finales ni un comentario
# después de la barra; de lo contrario provoca un error de sintaxis.

# --- Ejemplo implícito (paréntesis) ---
result_implicit = (a + b + c +
                30 + 40 + 50)

# Ambos producen el mismo valor, pero el estilo con paréntesis es más robusto.

# Pequeña demostración con una función (llamada normal, no relacionada con continuidad):
def add(a, b):
    return a + b

res = add(10, 20)

print("Result explicit:", result_explicit)
print("Result implicit:", result_implicit)
print("add(10,20) =", res)

# implicit line continuation es la forma recomendada de escribir código que se extiende a varias líneas, ya que es más legible y menos propensa a errores que la continuación explícita con barra invertida. Sin embargo, la continuación explícita puede ser útil en casos donde no se pueden usar paréntesis, como en declaraciones de importación o en algunos casos de asignación. En general, es importante seguir las convenciones de estilo de código de Python (PEP 8) para mantener un código limpio y legible.
# expresssions enclosed by: son expresiones que están encerradas por paréntesis (), corchetes [] o llaves {}. En Python, estas expresiones pueden extenderse a varias líneas físicas sin necesidad de usar el carácter de barra invertida (\) para indicar la continuación de línea. Esto se conoce como continuación de línea implícita y es una forma recomendada de escribir código que se extiende a varias líneas, ya que mejora la legibilidad y reduce la posibilidad de errores. Por ejemplo, en el siguiente código, la expresión dentro de los paréntesis se extiende a varias líneas físicas sin necesidad de usar la barra invertida:
# [] list iterals, list comprehensions, generator expressions
# ejemplo
my_list = [
    1, 2, 3,    # los espacios después de las comas son opcionales, pero mejoran la legibilidad
    4, 5, 6,    # se pueden incluir saltos de línea y espacios en blanco dentro de los corchetes, y se preservan tal como se escriben en el código
    7, 8, 9     # los comentarios también son permitidos dentro de los corchetes, pero deben estar en líneas separadas para evitar errores de sintaxis
]
# () tuple literals, generator expressions, parenthesized expressions
# ejemplo
my_tuple = (
    1, 2, 3,    # los espacios después de las comas son opcionales, pero mejoran la legibilidad
    4, 5, 6,    # se pueden incluir saltos de línea y espacios en blanco dentro de los paréntesis, y se preservan tal como se escriben en el código
    7, 8, 9     # los comentarios también son permitidos dentro de los paréntesis, pero deben estar en líneas separadas para evitar errores de sintaxis
)

# {} dict literals, set literals, dict comprehensions, set comprehensions
# ejemplo
my_dict = {
    'a': 1, 'b': 2, 'c': 3,    # los espacios después de las comas son opcionales, pero mejoran la legibilidad
    'd': 4, 'e': 5, 'f': 6,    # se pueden incluir saltos de línea y espacios en blanco dentro de las llaves, y se preservan tal como se escriben en el código
    'g': 7, 'h': 8, 'i': 9     # los comentarios también son permitidos dentro de las llaves, pero deben estar en líneas separadas para evitar errores de sintaxis
}

# ejemplo de expresión entre paréntesis: para un ciclo for dentro de una comprensión de lista
squares = [
    x**2 
    for x in range(10)  # la expresión dentro de los corchetes se extiende a varias líneas físicas sin necesidad de usar la barra invertida
]

# ejemplo de expresión entre paréntesis: para una expresión aritmética compleja en función de retorno
def complex_calculation(a, 
                        b,  # la expresión dentro de los paréntesis se extiende a varias líneas físicas sin necesidad de usar la barra invertida 
                        c):
    return (
        a * b + c - 
        (a / b) + 
        (b ** 2) - 
        (c % a)
    )  # la expresión dentro de los paréntesis se extiende a varias líneas físicas sin necesidad de usar la barra invertida 

# explicit line continuation es el proceso de dividir una declaración o expresión en varias líneas físicas utilizando el carácter de barra invertida (\) para indicar que la declaración o expresión continúa en la siguiente línea física. Por ejemplo, en el siguiente código, la declaración se divide en varias líneas físicas utilizando la barra invertida:
# no pueden haber espacios ni comentarios después de la barra invertida, de lo contrario se produce un error de sintaxis
result = a + b + c + \
            30 + 40 + 50

# Multi-line strings son cadenas de texto que se extienden a varias líneas físicas. En Python, se pueden crear utilizando triple comillas (''' o """). Las cadenas de texto de varias líneas pueden contener saltos de línea y espacios en blanco, y se preservan tal como se escriben en el código. Por ejemplo, en el siguiente código, se crea una cadena de texto de varias líneas utilizando triple comillas:
multi_line_string = """Esta es una cadena de texto
que se extiende a varias líneas.
Se pueden incluir saltos de línea y espacios en blanco."""
# los espacios y saltos de línea dentro de la cadena se preservan tal como se escriben en el código, lo que permite crear cadenas de texto con formato específico. Las cadenas de texto de varias líneas son útiles para escribir mensajes largos, documentación o cualquier texto que requiera un formato específico.
# tambien se usar \n, \t, etc. para incluir caracteres especiales dentro de la cadena de texto de varias líneas, lo que permite un mayor control sobre el formato del texto. Por ejemplo:
multi_line_string_with_special_chars = """Esta es una cadena de texto
que se extiende a varias líneas.\nSe pueden incluir saltos de línea y espacios en blanco.\tTambién se pueden incluir tabulaciones."""
# multi-line-strings no son comentarios, aunque pueden contener comentarios dentro de la cadena de texto. Sin embargo, los comentarios dentro de una cadena de texto no se consideran comentarios reales y no serán ignorados por el intérprete de Python. En cambio, se tratarán como parte del contenido de la cadena de texto. Por ejemplo:
multi_line_string_with_comment = """Esta es una cadena de texto
que se extiende a varias líneas.
# Este es un comentario dentro de la cadena de texto, pero no es un comentario real y se incluirá en el contenido de la cadena.
Se pueden incluir saltos de línea y espacios en blanco."""
# aunque el texto "# Este es un comentario dentro de la cadena de texto, pero no es un comentario real y se incluirá en el contenido de la cadena." parece un comentario, en realidad es parte del contenido de la cadena de texto y no será ignorado por el intérprete de Python. Por lo tanto, es importante tener cuidado al incluir comentarios dentro de cadenas de texto para evitar confusiones.

