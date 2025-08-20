print("Hello, World!")
# Esto es una función que imprime 'Hello, World!'
def hello_world():
    print("Hello, World!")
# Esto es una condición que verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    hello_world()

    # Solicita la edad al usuario y verifica si es mayor o menor de edad
    edad = int(input("Introduce tu edad: "))
    if edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")

# crea un menu
def menu():
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")
    opcion = int(input("Selecciona una opción: "))
    return opcion       

# Bucle principal del menú
while True:
    opcion = menu()
    if opcion == 1:
        print("Has seleccionado la opción 1.")
    elif opcion == 2:
        print("Has seleccionado la opción 2.")
    elif opcion == 3:
        print("Has seleccionado la opción 3.")
    elif opcion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, selecciona otra opción.")

# preguntar el nombre
nombre = input("¿Cuál es tu nombre? ")
print("Hola, " + nombre + "!")
