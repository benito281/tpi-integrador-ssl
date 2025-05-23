import ply.lex as lex 

# definicion de tokens
tokens = ['LLA_A', 'LLA_C', 'CORCH_A', 'CORCH_C', 'COMILLAS', 'COMA', '2PUNTOS', 'STRING', 'INTEGER', 'BOOLEAN', 'DATE', 'FLOAT',
          'NOMBRE_TEAM', 'CALLE', 'CALLE', 'CIUDAD', 'PAIS', 'ACTIVO', 'FECHA_FIN', 'FECHA_INICIO',
          'UNIVERSIDAD', 'ALIANZA', 'CARRERA', 'ASIGNATURA', 'LINK', 'CARGO', 'ESTADO', 'IDENTIDAD', 'DIRECCION',
          'TAREA', 'EQUIPOS', 'INTEGRANTES', 'PROYECTOS', 'EDAD', 'FOTO', 'VIDEO', 'CONCLUSION'
          ]

# Expresiones regulares tokens simples
t_LLA_A = r'\{'
t_LLA_C = r'\}'
t_CORCH_A = r'\['
t_CORCH_C = r'\]'
t_COMA = r','
t_2PUNTOS = r':'
t_COMILLAS = r'"'

# Expresiones regulares para tokens especificos
def t_NOMBRE_TEAM(t):
    r'"nombre_equipo"'
    print('TOKEN ENCONTRADO: "nombre_equipo"')


def t_IDENTIDAD(t):
    r'"identidad_equipo"'
    print('TOKEN ENCONTRADO: "identidad_equipo"')


def t_LINK(t):
    r'"link"'
    print('TOKEN ENCONTRADO: "link"')


def t_ASIGNATURA(t):
    r'"asignatura"'
    print('TOKEN ENCONTRADO:"asignatura"')


def t_CARRERA(t):
    r'"carrera"'
    print('TOKEN ENCONTRADO: "carrera"')


def t_UNIVERSIDAD(t):
    r'"universidad_regional"'
    print('TOKEN ENCONTRADO: "universidad_regional')


def t_DIRECCION(t):
    r'"direccion"'
    print('TOKEN ENCONTRADO: "direccion"')


def t_CALLE(t):
    r'"calle"'
    print('TOKEN ENCONTRADO: "calle"')


def t_CIUDAD(t):
    r'"CIUDAD"'
    print('TOKEN ENCONTRADO: "ciudad"')


def t_PAIS(t):
    r'"pais"'
    print('TOKEN ENCONTRADO: "pais"')


def t_ACTIVO(t):
    r'"activo"'
    print('TOKEN ENCONTRADO: "activo"')


def t_FECHA_FIN(t):
    r'"fecha_fin'
    print('TOKEN ENCONTRADO: "fecha_fin"')


def t_FECHA_INICIO(t):
    r'"fecha_inicio"'
    print('TOKEN ENCONTRADO: "fecha_inicio"')


def t_ALIANZA(t):
    r'"alianza"'
    print('TOKEN ENCONTRADO: "alianza"')


def t_CARGO(t):
    r'"cargo"'
    print('TOKEN ENCONTRADO: "cargo"')


def t_ESTADO(t):
    r'"estado"'
    print('TOKEN ENCONTRADO: "estado"')


def t_VIDEO(t):
    r'"video"'
    print('TOKEN ENCONTRADO: "video"')


def t_EDAD(t):
    r'"edad"'
    print('TOKEN ENCONTRADO: "edad"')


def t_FOTO(t):
    r'"foto"'
    print('TOKEN ENCONTRADO: "foto"')


def t_CONCLUSION(t):
    r'"conclusion"'
    print('"TOKEN ENCONTRADO: conclusion"')


def t_INTEGER(t):
    r'\d+'
    print('"TOKEN ENCONTRADO: integer"')


def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    print('"TOKEN ENCONTRADO: string"')


def t_BOOLEAN(t):
    r'true|false'
    print('"TOKEN ENCONTRADO: boolean')


def t_FLOAT(t):
    r'\d+\. \d+'
    print('"TOKEN ENCONTRADO: float"')


def t_DATE(t):
    r'"\d{4}-\d{2}-\d{2}"'
    print('"TOKEN ENCONTRADO: date"')


t_ignore = ' \t\n\r'


def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()


def leer_json_teclado():
    print("Ingrese el JSON (Ctrl+Z para terminar):")
    lineas = []
    try:
        while True:
            linea = input()
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

        # Tokenizar el texto JSON
        lexer.input(texto_json)

        # Imprimir los tokens generados
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(f'TOKEN ENCONTRADO: {tok.type}')

        if opcion == '1':
            repetir = input("¿Desea ingresar otro JSON? (s/n): ")
            if repetir.lower() != 's':
                break


if __name__ == "__main__":
    principal()
