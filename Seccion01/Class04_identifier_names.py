# Identifier Names
# 1. los identificadores son los nombres que se le asignan a las variables, funciones, clases, etc.
# 2. los identificadores deben seguir ciertas reglas:
# - deben comenzar con una letra (a-z, A-Z) o un guion bajo (_)
# - pueden contener letras, dígitos (0-9) y guiones bajos (_)
# - no pueden ser palabras reservadas de Python (como "if", "for", "while", etc.)
# 3. los identificadores deben ser descriptivos y significativos para facilitar la lectura del código.

# son case-sensitive, lo que significa que "variable" y "Variable" son identificadores diferentes.  
# convención de nombres:
# - para variables y funciones: se recomienda usar letras minúsculas y guiones bajos para separar palabras (ejemplo: "mi_variable", "calcular_suma")
# - para clases: se recomienda usar la convención de "CamelCase", donde cada palabra comienza con mayúscula (ejemplo: "MiClase", "Calculadora") 

# singles underscore (_) se utiliza para indicar que un identificador es privado o de uso interno, aunque esto es solo una convención y no impide el acceso a dicho identificador desde fuera de la clase o módulo.
# doble underscore (__) se utiliza para indicar que un identificador es privado y se realiza un name mangling, lo que significa que el nombre del identificador se modifica internamente para evitar conflictos con nombres de otras clases o módulos.  
# double underscore al principio y al final (__init__, __str__, etc.) se utilizan para métodos especiales o "magic methods" que tienen un significado específico en Python. 

# Ejemplos de identificadores válidos
mi_variable = 10
def calcular_suma(a, b):
    return a + b
class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre
# Ejemplos de identificadores no válidos
# 1variable = 10  # no puede comenzar con un dígito
# def calcular-suma(a, b):  # no puede contener guiones
#     return a + b
# class Mi Clase:  # no puede contener espacios
#     def __init__(self, nombre):
#         self.nombre = nombre

# other comventions from the PEP 8 (Python Enhancement Proposal 8) include:
# - para constantes: se recomienda usar letras mayúsculas y guiones bajos para separar palabras (ejemplo: "PI", "GRAVEDAD")
# - para módulos y paquetes: se recomienda usar letras minúsculas y guiones bajos para separar palabras (ejemplo: "mi_modulo", "mi_paquete")    
# - para métodos y atributos de clase: se recomienda usar letras minúsculas y guiones bajos para separar palabras (ejemplo: "mi_metodo", "mi_atributo") 
# - para variables de instancia: se recomienda usar letras minúsculas y guiones bajos para separar palabras (ejemplo: "mi_variable_instancia")  
# - para variables de clase: se recomienda usar letras minúsculas y guiones bajos para separar palabras (ejemplo: "mi_variable_clase")  
# - para variables globales: se recomienda usar letras minúsculas y guiones bajos para separar palabras (ejemplo: "mi_variable_global") 
# - para variables locales: se recomienda usar letras minúsculas y guiones bajos para separar palabras (ejemplo: "mi_variable_local")   
# - para funciones: se recomienda usar letras minúsculas y guiones bajos para separar palabras (ejemplo: "mi_funcion")
# - para clases: se recomienda usar la convención de "CamelCase", donde cada palabra comienza con mayúscula (ejemplo: "MiClase", "Calculadora") 
# - para métodos: se recomienda usar letras minúsculas y guiones bajos para separar palabras (ejemplo: "mi_metodo")
# - para atributos: se recomienda usar letras minúsculas y guiones bajos para separar palabras (ejemplo: "mi_atributo")
# - para constantes: se recomienda usar letras mayúsculas y guiones bajos para separar palabras (ejemplo: "PI", "GRAVEDAD") 
