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

