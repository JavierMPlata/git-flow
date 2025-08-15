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