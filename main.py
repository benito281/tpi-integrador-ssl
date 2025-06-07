from lexer import LexerTokens as tokens

lexer = tokens()  # Instancia de la clase LexerTokens
lexer.build()  # Construye el LEXER


def leer_json_teclado():
    print("Ingrese el JSON por teclado (Presione Ctrl+Z en Windows o Ctrl+D en Linux/Mac para terminar):")
    lineas = []
    try:
        while True:
            linea = input()
            lineas.append(linea)
    except EOFError:
        print("\nFin de entrada detectado.")
    return '\n'.join(lineas)


def leer_json_archivo(nombre_arch):
    try:
        with open(nombre_arch, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Archivo no encontrado: {nombre_arch}")
        return None


def principal():
    while True:
        try:
            opcion = input(
                "Seleccione una opción (1: Ingresar JSON por teclado, 2: Leer JSON desde archivo, 3: Salir): ")
            if opcion == '1':
                texto_json = leer_json_teclado()
                lexer.test(texto_json)

            elif opcion == '2':
                nombre_arch = input(
                    "Ingrese el nombre del archivo (ruta completa si no está en el mismo directorio): ")
                texto_json = leer_json_archivo(nombre_arch)
                if texto_json is None:
                    continue
                lexer.test(texto_json)

            elif opcion == '3':
                print("Saliendo...")
                break

            else:
                print("Opción no válida")
                continue

            # Preguntar si desea continuar luego de procesar JSON
            try:
                repetir = input(
                    "Ingrese 's' para volver al menú o presione Ctrl+Z para salir: ")
                if repetir.lower() != 's':
                    print("Saliendo del programa.")
                    break
            except EOFError:
                print("\nFin de entrada detectado. Saliendo...")
                break

        except EOFError:
            print("\nCaracter de fin de archivo ingresado. Saliendo del programa.")
            break


if __name__ == "__main__":
    principal()
