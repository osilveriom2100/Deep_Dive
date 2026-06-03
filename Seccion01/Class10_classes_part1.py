# Classes
# Las clases son plantillas para crear objetos. Un objeto es una instancia de una clase. Las clases pueden tener atributos (variables) y métodos (funciones).
# La sintaxis para definir una clase es la siguiente:
# class ClassName:
#     # atributos y métodos de la clase
# Para crear una instancia de una clase, se utiliza la siguiente sintaxis:
# object_name = ClassName()
# Ejemplo de una clase simple
class Rectangle:
    def __init__(self, width, height):  # el método __init__ es un método especial que se llama automáticamente cuando se crea una instancia de la clase. Se utiliza para inicializar los atributos de la clase.
        self.width = width  # self se refiere a la instancia actual de la clase y se utiliza para acceder a los atributos y métodos de la clase.
        self.height = height
    def area(self):  # este es un método de la clase que calcula el área del rectángulo utilizando los atributos width y height.
        return self.width * self.height
    
# el primer parametro del método __init__ y de cualquier método de la clase debe ser self, que es una referencia a la instancia actual de la clase. Esto permite acceder a los atributos y métodos de la clase desde dentro de los métodos. Al crear una instancia de la clase Rectangle, se pasan los valores para width y height, que se asignan a los atributos correspondientes de la instancia. Luego, al llamar al método area() en la instancia, se calcula el área del rectángulo utilizando los valores de width y height almacenados en esa instancia.
# cabe decir que el nombre self es solo una convención y se puede usar cualquier otro nombre para el primer parámetro de los métodos de la clase, pero es recomendable seguir esta convención para mantener la claridad y consistencia en el código.

# Crear una instancia de la clase Rectangle
rect = Rectangle(5, 3)
print(f"Width: {rect.width}, Height: {rect.height}, Area: {rect.area()}")  # accedemos a los atributos width y height de la instancia rect y llamamos al método area() para calcular el área del rectángulo.
# str en una instancia de una clase
print(str(rect))  # al convertir la instancia rect a una cadena de texto utilizando str(), se obtiene una representación de la instancia que incluye el tipo de objeto y su dirección en memoria, lo que no es muy útil para entender el contenido de la instancia. Para obtener una representación más legible y significativa de la instancia, se puede definir el método __str__ en la clase, como se muestra en el siguiente ejemplo. Al definir el método __str__, se puede personalizar la forma en que se representa la instancia como una cadena de texto, lo que facilita la comprensión del contenido de la instancia al imprimirla o convertirla a una cadena.


# str en una clase
# el método __str__ es un método especial que se llama cuando se convierte una instancia de la clase a una cadena de texto, por ejemplo, al imprimir la instancia. Se utiliza para definir cómo se representa la instancia como una cadena de texto.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def __str__(self):  # este método define cómo se representa la instancia de la clase como una cadena de texto.
        return f"Rectangle(width={self.width}, height={self.height})"
rect = Rectangle(5, 3)
print(rect)  # al imprimir la instancia rect, se llama al método __str__ para obtener la representación en cadena de texto de la instancia, que en este caso será "Rectangle(width=5, height=3)". Esto hace que la salida sea más legible y fácil de entender.  

# repr en una clase
# el método __repr__ es otro método especial que se llama para obtener una representación oficial de la instancia de la clase, que se utiliza principalmente para depuración y desarrollo. La diferencia entre __str__ y __repr__ es que __str__ se utiliza para obtener una representación legible y amigable de la instancia, mientras que __repr__ se utiliza para obtener una representación más detallada y precisa de la instancia, que puede incluir información adicional como el tipo de objeto y su dirección en memoria.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    def __repr__(self):  # este método define cómo se representa la instancia de la clase para propósitos de depuración y desarrollo.
        return f"Rectangle(width={self.width}, height={self.height}, area={self.area()})"
rect = Rectangle(5, 3)
print(repr(rect))  # al llamar a repr(rect), se obtiene la representación oficial de la instancia rect, que en este caso será "Rectangle(width=5, height=3, area=15)". Esto proporciona información adicional sobre la instancia, como el área calculada utilizando el método area(), lo que puede ser útil para depuración y desarrollo.   

# eq en una clase
# el método __eq__ es un método especial que se llama para comparar dos instancias de la clase utilizando el operador de igualdad (==). Se utiliza para definir cómo se comparan las instancias de la clase en términos de igualdad. Por defecto, el método __eq__ compara las instancias por su identidad (es decir, si son el mismo objeto en memoria), pero al definir el método __eq__, se puede personalizar la forma en que se comparan las instancias, por ejemplo, comparando sus atributos en lugar de su identidad.
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
    def __eq__(self, other):  # este método define cómo se comparan las instancias de la clase para determinar si son iguales.
        if isinstance(other, Rectangle):  # verifica si el objeto other es una instancia de la clase Rectangle antes de comparar sus atributos.
            return self.width == other.width and self.height == other.height  # compara los atributos width y height de ambas instancias para determinar si son iguales.
        return NotImplemented  # devuelve NotImplemented si el objeto other no es una instancia de la clase Rectangle, lo que indica que la comparación no es compatible entre los dos objetos. 
    
rect1 = Rectangle(5, 3)
rect2 = Rectangle(5, 3)
rect3 = Rectangle(4, 2)
print(rect1 == rect2)  # al comparar rect1 y rect2 utilizando el operador de igualdad (==), se llama al método __eq__ para determinar si las dos instancias son iguales. En este caso, como rect1 y rect2 tienen los mismos valores para width y height, el resultado será True.
print(rect1 == rect3)  # al comparar rect1 y rect3 utilizando el operador de igualdad (==), se llama al método __eq__ para determinar si las dos instancias son iguales. En este caso, como rect1 y rect3 tienen diferentes valores para width y height, el resultado será False.   


