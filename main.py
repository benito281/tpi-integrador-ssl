import os
import platform
from lexer import LexerTokens as tokens

lexer = tokens()  # Instancia de la clase LexerTokens
lexer.build()  # Construye el LEXER

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def leer_json_teclado():
    print("A continuación, deberá introducir el archivo JSON línea por línea.")
    print("Después de introducir cada línea presione ENTER, y luego presione")
    print("presione CTRL + Z en Windows o CTRL + D en Linux cuando haya")
    print("introducido todas las líneas que se deben analizar.\n")

    lineas = []
    try:
        while True:
            linea = input("Línea: ")
            lineas.append(linea)
    except EOFError:
        print("\n")
        return '\n'.join(lineas)

def leer_json_archivo(nombre_arch):
    try:
        with open(nombre_arch, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return None

def principal():
    while True:
        clear_screen()
        print("==================================================================")
        print("Presentación del lexer del grupo Los Hijos de Chomsky. El programa")
        print("cuenta con tres operaciones posibles:")
        print("1. Ingresar una entrada interactivamente por teclado.")
        print("2. Leer una entrada desde un archivo.")
        print("3. Salir.")
        print("==================================================================")

        try:
            opcion = input("Seleccione una opción: ")
            clear_screen()

            if opcion == '1':
                texto_json = leer_json_teclado()
                lexer.test(texto_json)

            elif opcion == '2':
                print("A continuación, deberá introducir el nombre del archivo JSON que se")
                print("desea analizar. Si este se encuentra en otra carpeta, recuerde que")
                print("debe especificar su ubicación.\n")
                nombre_arch = input("Nombre del archivo: ")
                texto_json = leer_json_archivo(nombre_arch)

                # Si no se introdujo ningún nombre de archivo debemos hacer
                # algo al respecto.
                if texto_json is not None:
                    print("-------------------------------------------------------------------")
                    lexer.test(texto_json)
                else:
                    print("No se introdujo el nombre de ningún archivo o este no existe.")

            elif opcion == '3':
                break

            else:
                print("Opción inválida.")
                continue

            # Preguntar si desea continuar luego de procesar el JSON.
            try:
                print("-------------------------------------------------------------------")
                print("Ingrese 'S' o 's' si desea volver al menú, y CTRL + Z (CTRL + D en")
                print("Linux) para salir del programa.")
                repetir = input("\nElección: ")

                # Elegimos qué hacer en función de la elección.
                if repetir.lower() != 's':
                    print("Saliendo del programa.")
                    break
            except EOFError:
                print("\nFin de entrada detectado. Saliendo...")
                break

        # Si se ingresa un caracter de fin de archivo debemos
        # abortar la ejecución del programa.
        except EOFError:
            print("\nCaracter de fin de archivo ingresado. Saliendo del programa.")
            break

if __name__ == "__main__":
    principal()
