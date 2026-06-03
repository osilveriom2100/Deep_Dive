# try, exept, finally
# try:
#     # codigo que puede generar una excepcion
# except ExceptionType: 
#     # codigo para manejar la excepcion
# finally:
#     # codigo que se ejecuta siempre, independientemente de si se genero una excepcion o no
# el bloque try se utiliza para envolver el código que puede generar una excepción. Si se genera una excepción dentro del bloque try, el flujo de ejecución se detiene y se busca un bloque except que pueda manejar esa excepción. Si se encuentra un bloque except que coincide con el tipo de excepción generada, se ejecuta el código dentro de ese bloque. Si no se encuentra ningún bloque except que maneje la excepción, la excepción se propaga hacia arriba en la pila de llamadas hasta que se encuentra un manejador adecuado o hasta que el programa termina con un error no manejado. El bloque finally se ejecuta siempre, independientemente de si se generó una excepción o no. Esto es útil para realizar tareas de limpieza o liberar recursos, como cerrar archivos o conexiones de red, incluso si ocurre una excepción.
# ejemplo de manejo de excepciones con try, except y finally    
try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print(f"Result: {result}")
except ValueError:      # maneja la excepcion de valor no valido al convertir la entrada a un entero ejemplo: si el usuario ingresa "abc" en lugar de un numero
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError: # maneja la excepcion de division por cero ejemplo: si el usuario ingresa 0 como numero, lo que causaria una division por cero
    print("Error: Division by zero is not allowed.")
finally:
    print("This block will always be executed, regardless of exceptions.")

# ejemplo con while loop y manejo de excepciones
while True:
    try:
        x = int(input("Enter a number: "))
        result = 10 / x
        print(f"Result: {result}")
        break  # sale del bucle si la entrada es valida y no se genera una excepcion
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# ejemplo con while loop continue y manejo de excepciones
while True:
    try:
        x = int(input("Enter a number: "))
        result = 10 / x
        print(f"Result: {result}")
        break  # sale del bucle si la entrada es valida y no se genera una excepcion
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue  # continua con la siguiente iteracion del bucle si se genera una excepcion de valor no valido
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        continue  # continua con la siguiente iteracion del bucle si se genera una excepcion de division por cero
    finally:
        print("This block will always be executed, regardless of exceptions.") # este bloque se ejecuta en cada iteracion del bucle, incluso si se genera una excepcion y se continua con la siguiente iteracion, lo que puede ser util para realizar tareas de limpieza o liberar recursos en cada iteracion del bucle.
