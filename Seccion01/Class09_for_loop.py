# for loop
# for variable in iterable:
#     # codigo a ejecutar en cada iteracion del bucle
# el bucle for se utiliza para iterar sobre una secuencia de elementos, como una lista, tupla, cadena o cualquier objeto iterable. En cada iteracion del bucle, la variable toma el valor del siguiente elemento en la secuencia y se ejecuta el bloque de codigo dentro del bucle. El bucle for se detiene cuando se han iterado todos los elementos de la secuencia.
# ejemplo de for loop con una lista 
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# ejemplo de for loop con una cadena
for char in "hello":
    print(char) 
# ejemplo de for loop con range
for i in range(5):      # range(5) genera una secuencia de numeros del 0 al 4, por lo que el bucle se ejecuta 5 veces con i tomando los valores 0, 1, 2, 3 y 4 en cada iteracion
    print(i)

# loop con try, except y finally
for i in range(5):
    try:
        result = 10 / (i-3)  # esto generara una excepcion de division por cero cuando i sea igual a 3
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        continue  # continua con la siguiente iteracion del bucle si se genera una excepcion de division por cero
    finally:
        print("This block will always be executed, regardless of exceptions.")
    print("This line will be executed after the try-except-finally block in each iteration of the loop.")

# uso de index en un for loop
s = "hello"
i = 0
for char in s:
    print(f"Index: {i}, Character: {char}")
    i += 1

# uso de len y range para iterar con index en un for loop
s = "hello"
for i in range(len(s)):
    print(f"Index: {i}, Character: {s[i]}")

# uso de enumerate para iterar con index en un for loop
s = "hello"
for i, char in enumerate(s):    # enumerate(s) devuelve un iterador que produce tuplas de la forma (index, element) para cada elemento en la secuencia s, lo que permite iterar sobre los caracteres de la cadena s junto con sus indices correspondientes de manera mas sencilla y legible.
    print(f"Index: {i}, Character: {char}")
