import ply.lex as lex


class LexerTokens:
    # Lista de tokens
    tokens = (
        'LLA_A', 'LLA_C', 'CORCH_A', 'CORCH_C', 'COMILLAS', 'COMA', '2PUNTOS',
        'STRING', 'INTEGER', 'BOOLEAN', 'DATE', 'FLOAT', 'EMAIL',
        'NOMBRE_TEAM', 'CALLE', 'CIUDAD', 'PAIS', 'ACTIVO', 'FECHA_FIN', 'FECHA_INICIO',
        'UNIVERSIDAD', 'ALIANZA', 'CARRERA', 'ASIGNATURA', 'LINK', 'CARGO', 'ESTADO', 'IDENTIDAD', 'DIRECCION',
        'TAREA', 'EQUIPOS', 'INTEGRANTES', 'PROYECTOS', 'EDAD', 'FOTO', 'VIDEO', 'CONCLUSION', 'PUNTO'
    )

    # Tokens simples
    t_LLA_A = r'\{'
    t_LLA_C = r'\}'
    t_CORCH_A = r'\['
    t_CORCH_C = r'\]'
    t_COMA = r','
    t_2PUNTOS = r':'
    t_COMILLAS = r'"'
    #t_GUION = r'-'
    t_PUNTO = r'\.'

    # Expresiones regulares para tokens especificos
    def t_NOMBRE_TEAM(self, t):
        r'"nombre_equipo"'
        print('-> Token especifico encontrado: nombre_equipo')

    def t_NOMBRE(self, t):
        r'"nombre"'
        print('-> Token especifico encontrado: nombre')

    def t_IDENTIDAD(self, t):
        r'"identidad_equipo"'
        print('-> Token especifico encontrado: identidad_equipo')

    def t_LINK(self, t):
        r'"link"'
        print('-> Token especifico encontrado: link')

    def t_ASIGNATURA(self, t):
        r'"asignatura"'
        print('-> Token especifico encontrado: asignatura')

    def t_CARRERA(self, t):
        r'"carrera"'
        print('-> Token especifico encontrado: carrera')

    def t_UNIVERSIDAD(self, t):
        r'"universidad_regional"'
        print('-> Token especifico encontrado: universidad_regional')

    def t_DIRECCION(self, t):
        r'"direccion"'
        print('-> Token especifico encontrado: direccion')

    def t_CALLE(self, t):
        r'"calle"'
        print('-> Token especifico encontrado: calle')

    def t_CIUDAD(self, t):
        r'"CIUDAD"'
        print('-> Token especifico encontrado: ciudad')

    def t_PAIS(self, t):
        r'"pais"'
        print('-> Token especifico encontrado: pais')

    def t_ACTIVO(self, t):
        r'"activo"'
        print('-> Token especifico encontrado: activo')

    def t_FECHA_FIN(self, t):
        r'"fecha_fin"'
        print('-> Token especifico encontrado: fecha_fin')

    def t_FECHA_INICIO(self, t):
        r'"fecha_inicio"'
        print('-> Token especifico encontrado: fecha_inicio')

    def t_ALIANZA(self, t):
        r'"alianza"'
        print('-> Token especifico encontrado: alianza')

    def t_CARGO(self, t):
        r'"cargo"'
        print('-> Token especifico encontrado: cargo')

    def t_ESTADO(self, t):
        r'"estado"'
        print('-> Token especifico encontrado: estado')

    def t_VIDEO(self, t):
        r'"video"'
        print('-> Token especifico encontrado: video')

    def t_EDAD(self, t):
        r'"edad"'
        print('-> Token especifico encontrado: edad')

    def t_FOTO(self, t):
        r'"foto"'
        print('-> Token especifico encontrado: foto')

    def t_CONCLUSION(self, t):
        r'"conclusion"'
        print('-> Token especifico encontrado: conclusion')

    # Tokens con valores

    def t_DATE(self, t):
        r'"(19[0-9]{2}|20[0-9]{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])"'
        t.value = t.value.strip('"')
        return t

    def t_EMAIL(self, t):
        r'"[a-zA-Z0-9+%]+@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)+"'
        t.value = t.value.strip('"')
        return t

    def t_FLOAT(self, t):
        r'\d+\.\d+'
        t.value = float(t.value)
        if t.value < 0:
            print("Error: El número flotante no puede ser negativo.")
        else:
            print('-> Token especifico encontrado: float')
        return t

    def t_INTEGER(self, t):
        r'\d+'
        return t

    def t_BOOLEAN(self, t):
        r'true|false'
        return t

    def t_STRING(self, t):
        r'"([^\\\n]|(\\.))*?"'
        t.value = t.value.strip('"')
        return t

    # Ignorar espacios y tabulaciones
    t_ignore = ' \t\n\r'

    # Manejo de errores
    def t_error(self, t):
        last_cr = t.lexer.lexdata.rfind('\n', 0, t.lexpos)
        line = t.lexer.lineno
        col = t.lexpos if last_cr < 0 else t.lexpos - last_cr - 1
        print(f"Caracter ilegal '{t.value[0]}' en línea {line}, columna {col}")
        t.lexer.skip(1)

    # Construir el lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Método de prueba
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(f'Token simple : {tok.type} encontrado')
