
from lexer import LexerTokens as mytokens

lexer = mytokens()
lexer.build() #Construye el LEXER

def leer_json_teclado():
    print("Ingrese el JSON (Presione ENTER y escriba FIN, luego enter):")
    lineas = []
    try:
        while True:
            linea = input()
            if linea.strip().upper() == 'FIN': #Ayuda a poder terminar de analizar lo que esta en consola
                break
            lineas.append(linea)
    except EOFError:
        pass
    return '\n'.join(lineas)




def leer_json_archivo(nombre_arch):
    try:
        with open(nombre_arch, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Archivo no encontrado: {nombre_arch}")
        return None


# Función principal
def principal():
    while True:
        opcion = input(
            "Seleccione una opción (1: Ingresar JSON por teclado, 2: Leer JSON desde archivo, 3: Salir): ")
        if opcion == '1':
            texto_json = leer_json_teclado()
        elif opcion == '2':
            nombre_arch = input(
                "Ingrese el nombre del archivo (ruta completa si no está en el mismo directorio): ")
            texto_json = leer_json_archivo(nombre_arch)
            if texto_json is None:
                continue
        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida")
            continue

        # Tokenizar el texto JSON mostrar mensaje
        lexer.test(texto_json)
        


        if opcion == '1':
            repetir = input("¿Desea ingresar otro JSON? (s/n): ")
            if repetir.lower() != 's':
                break


if __name__ == "__main__":
    principal()
