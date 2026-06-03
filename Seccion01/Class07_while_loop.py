# While Loop
# while condition:
#     # code to execute
# el bucle while se ejecuta mientras la condición sea verdadera. Si la condición es falsa desde el principio, el código dentro del bucle no se ejecutará en absoluto. Es importante asegurarse de que la condición eventualmente se vuelva falsa para evitar un bucle infinito.
# ejemplo de un bucle while que imprime los números del 1 al 5
i = 1
while i <= 5:
    print(i)
    i += 1  # incrementa i en 1 en cada iteración para evitar un bucle infinito
# también se puede usar la declaración break para salir de un bucle while antes de que la condición se vuelva falsa. Esto puede ser útil para salir de un bucle en función de una condición específica o para evitar un bucle infinito.
# ejemplo de un bucle while que imprime los números del 1 al 5, pero sale del bucle si el número es igual a 3
i = 1
while i <= 5:
    if i == 3:
        break  # sale del bucle si i es igual a 3
    print(i)
    i += 1  # incrementa i en 1 en cada iteración para evitar un bucle infinito
# también se puede usar la declaración continue para saltar a la siguiente iteración del bucle while sin ejecutar el código restante en la iteración actual. Esto puede ser útil para omitir ciertas iteraciones en función de una condición específica.
# ejemplo de un bucle while que imprime los números del 1 al 5, pero omite el número 3
i = 1
while i <= 5:
    if i == 3:
        i += 1  # incrementa i en 1 para evitar un bucle infinito
        continue  # salta a la siguiente iteración si i es igual a 3
    print(i)
    i += 1  # incrementa i en 1 en cada iteración para evitar un bucle infinito 

# para hacer un do while loop en python, se puede usar un bucle while con una condición que siempre sea verdadera, y luego usar una declaración break para salir del bucle cuando se cumpla la condición de terminación. Esto simula el comportamiento de un do while loop, donde el código dentro del bucle se ejecuta al menos una vez antes de verificar la condición de terminación.
# ejemplo de un do while loop que imprime los números del 1 al 5
i = 1
while True:  # condición siempre verdadera para simular un do while loop
    print(i)
    i += 1  # incrementa i en 1 en cada iteración para evitar un bucle infinito
    if i > 5:
        break  # sale del bucle si i es mayor que 5

# ejemplo
min_length = 2
while True:
    name = input("Enter your name: ")
    if len(name) >= min_length and name.isprintable() and name.isalpha(): 
        # verifica que el nombre tenga al menos min_length caracteres, que sea imprimible y que solo contenga letras
        print(f"Hello, {name}!")
        break  # sale del bucle si el nombre tiene al menos min_length caracteres
    else:
        print(f"Name must be at least {min_length} characters long. Please try again.")