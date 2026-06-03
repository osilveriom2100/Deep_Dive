# setter & getter
# setter es un método que se utiliza para establecer el valor de un atributo privado de una clase. Un atributo privado es un atributo que no se puede acceder directamente desde fuera de la clase, sino que se accede a través de métodos getter y setter. El método setter se utiliza para asignar un valor a un atributo privado, mientras que el método getter se utiliza para obtener el valor de un atributo  
# privado. La sintaxis para definir un método setter es la siguiente:
# class ClassName:
#     def set_attribute(self, value):
#         self.__attribute = value
# La sintaxis para definir un método getter es la siguiente:
# class ClassName:
#     def get_attribute(self):
#         return self.__attribute


# en python no existe el concepto de atributos privados como en otros lenguajes de programación, pero se puede simular utilizando el prefijo __ para indicar que un atributo es privado. Al definir un atributo con el prefijo __, se indica que no se debe acceder directamente a ese atributo desde fuera de la clase, sino que se debe utilizar métodos getter y setter para acceder y modificar su valor. Esto ayuda a proteger los datos de la clase y a mantener la encapsulación, lo que es un principio fundamental de la programación orientada a objetos. 
class Rectangle:
    def __init__(self, width, height):
        self.__width = width  # el atributo width se define como privado utilizando el prefijo __ para indicar que no se puede acceder directamente desde fuera de la clase.
        self.__height = height  # el atributo height también se define como privado.
    
    def area(self):
        return self.__width * self.__height
    
    def set_width(self, width):  # este es un método setter que permite establecer el valor del atributo privado __width.
        self.__width = width
    
    def get_width(self):  # este es un método getter que permite obtener el valor del atributo privado __width.
        return self.__width
    
    def set_height(self, height):  # este es un método setter que permite establecer el valor del atributo privado __height.
        self.__height = height
    
    def get_height(self):  # este es un método getter que permite obtener el valor del atributo privado __height.
        return self.__height
    
rect = Rectangle(5, 3)
print(f"Width: {rect.get_width()}, Height: {rect.get_height()}, Area: {rect.area()}")  # al llamar a los métodos getter get_width() y get_height(), se obtiene el valor de los atributos privados __width y __height, respectivamente, lo que permite calcular el área del rectángulo utilizando el método area(). Luego, al llamar a los métodos setter set_width() y set_height(), se pueden modificar los valores de los atributos privados, lo que a su vez afecta el resultado del cálculo del área. Esto demuestra cómo se puede utilizar la encapsulación para proteger los datos de la clase y controlar el acceso a ellos a través de métodos getter y setter. 

# se usa getters y setters para controlar el acceso a los atributos de una clase, lo que permite validar los datos antes de asignarlos a los atributos, realizar cálculos adicionales o ejecutar código adicional cuando se accede o modifica un atributo. Esto ayuda a mantener la integridad de los datos y a garantizar que los atributos de la clase se utilicen de manera adecuada. Además, el uso de getters y setters también facilita la refactorización del código, ya que se puede cambiar la implementación interna de la clase sin afectar el código que utiliza la clase, siempre y cuando se mantengan las interfaces de los métodos getter y setter.
# por lo que si no se necesita realizar validaciones o cálculos adicionales al acceder o modificar los atributos de una clase, se puede optar por no utilizar getters y setters y acceder directamente a los atributos de la clase. Sin embargo, es importante tener en cuenta que esto puede comprometer la encapsulación y la integridad de los datos, ya que no se tiene control sobre cómo se acceden o modifican los atributos. Por lo tanto, es recomendable utilizar getters y setters cuando sea necesario para garantizar un diseño de clase robusto y mantenible.
# otra opción para controlar el acceso a los atributos de una clase es utilizar propiedades (properties) en lugar de métodos getter y setter. Las propiedades permiten definir métodos que se comportan como atributos, lo que facilita el acceso a los atributos de la clase sin necesidad de llamar explícitamente a los métodos getter y setter. Esto puede hacer que el código sea más limpio y legible, al tiempo que mantiene la encapsulación y el control sobre el acceso a los atributos. La sintaxis para definir una propiedad es la siguiente:
# class ClassName:  
#     @property
#     def attribute(self):
#         return self.__attribute
#     @attribute.setter
#     def attribute(self, value):
#         self.__attribute = value

# cuando usar getters y setters o propiedades depende del diseño de la clase y de las necesidades específicas del proyecto. Si se necesita realizar validaciones o cálculos adicionales al acceder o modificar los atributos de una clase, es recomendable utilizar getters y setters para controlar el acceso a los atributos. Por otro lado, si se desea un código más limpio y legible sin sacrificar la encapsulación, las propiedades pueden ser una buena opción. En general, es importante considerar el equilibrio entre la simplicidad del código y la necesidad de control sobre el acceso a los atributos al decidir cuándo usar getters y setters o propiedades en una clase.
# ejemplo de una clase con propiedades
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    
    def area(self):
        return self.__width * self.__height
    
    @property
    def width(self):  # este método se define como una propiedad utilizando el decorador @property, lo que permite acceder al atributo __width como si fuera un atributo normal.
        return self.__width
    
    @width.setter
    def width(self, width):  # este método se define como un setter para la propiedad width utilizando el decorador @width.setter, lo que permite modificar el valor del atributo __width de manera controlada.
        self.__width = width
    
    @property
    def height(self):  # este método se define como una propiedad para el atributo __height.
        return self.__height
    
    @height.setter
    def height(self, height):  # este método se define como un setter para la propiedad height.
        self.__height = height


# Ejemplos adicionales: property perezosa (caché) y benchmark simple
class Expensive:
    def __init__(self, n):
        self.n = n
        self._cache = None

    def compute(self):
        total = 0
        for i in range(self.n):
            total += i
        return total

    # acceso via método explícito (getter estilo)
    def get_value(self):
        return self.compute()

    # acceso via property (recalcula cada vez)
    @property
    def value(self):
        return self.compute()

    # property perezosa: calcula la primera vez y guarda en caché
    @property
    def value_cached(self):
        if self._cache is None:
            self._cache = self.compute()
        return self._cache


def _benchmark():
    import time

    repeats = 2000
    e = Expensive(2000)

    # medir llamada a método
    t0 = time.perf_counter()
    for _ in range(repeats):
        _ = e.get_value()
    t_method = time.perf_counter() - t0

    # medir property (recalcula)
    t0 = time.perf_counter()
    for _ in range(repeats):
        _ = e.value
    t_property = time.perf_counter() - t0

    # medir property perezosa (primera acceso hace el trabajo, luego es rápido)
    # for fairness, reset object so cached value is empty
    e2 = Expensive(2000)
    # primer acceso (carga)
    t0 = time.perf_counter()
    _ = e2.value_cached
    t_first_cached = time.perf_counter() - t0
    # accesos repetidos posteriores
    t0 = time.perf_counter()
    for _ in range(repeats):
        _ = e2.value_cached
    t_cached = time.perf_counter() - t0

    print('\nBenchmark (repeats=%d, n=2000):' % repeats)
    print('method get_value:    %.4f s' % t_method)
    print('property value:      %.4f s' % t_property)
    print('first cached access: %.4f s' % t_first_cached)
    print('repeated cached:     %.4f s' % t_cached)


if __name__ == '__main__':
    _benchmark()