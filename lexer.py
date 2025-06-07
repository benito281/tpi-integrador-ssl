import ply.lex as lex

class LexerTokens:
    # Lista de tokens.
    tokens = (
        'LLA_A', 'LLA_C', 'CORCH_A', 'CORCH_C', 'COMILLAS', 'COMA', '2PUNTOS',
        'STRING', 'INTEGER', 'BOOLEAN', 'DATE', 'FLOAT', 'EMAIL',
        'NOMBRE_TEAM', 'CALLE', 'CIUDAD', 'PAIS', 'ACTIVO', 'FECHA_FIN', 'FECHA_INICIO',
        'UNIVERSIDAD', 'ALIANZA', 'CARRERA', 'ASIGNATURA', 'LINK', 'CARGO', 'ESTADO', 'IDENTIDAD', 'DIRECCION',
        'TAREA', 'EQUIPOS', 'INTEGRANTES', 'PROYECTOS', 'EDAD', 'FOTO', 'VIDEO', 'CONCLUSION', 'PUNTO'
    )

    # Tokens simples.
    t_LLA_A = r'\{'
    t_LLA_C = r'\}'
    t_CORCH_A = r'\['
    t_CORCH_C = r'\]'
    t_COMA = r','
    t_2PUNTOS = r':'
    t_COMILLAS = r'"'
    #t_GUION = r'-'
    t_PUNTO = r'\.'

    # Expresiones regulares para tokens específicos.
    def t_NOMBRE_TEAM(self, t):
        r'"nombre_equipo"'
        print('\n-> Token específico encontrado: nombre_equipo')

    def t_NOMBRE(self, t):
        r'"nombre"'
        print('\n-> Token específico encontrado: nombre')

    def t_IDENTIDAD(self, t):
        r'"identidad_equipo"'
        print('\n-> Token específico encontrado: identidad_equipo')

    def t_LINK(self, t):
        r'"link"'
        print('\n-> Token específico encontrado: link')

    def t_ASIGNATURA(self, t):
        r'"asignatura"'
        print('\n-> Token específico encontrado: asignatura')

    def t_CARRERA(self, t):
        r'"carrera"'
        print('\n-> Token específico encontrado: carrera')

    def t_UNIVERSIDAD(self, t):
        r'"universidad_regional"'
        print('\n-> Token específico encontrado: universidad_regional')

    def t_DIRECCION(self, t):
        r'"direccion"'
        print('\n-> Token específico encontrado: direccion')

    def t_CALLE(self, t):
        r'"calle"'
        print('\n-> Token específico encontrado: calle')

    def t_CIUDAD(self, t):
        r'"CIUDAD"'
        print('\n-> Token específico encontrado: ciudad')

    def t_PAIS(self, t):
        r'"pais"'
        print('\n-> Token específico encontrado: pais')

    def t_ACTIVO(self, t):
        r'"activo"'
        print('\n-> Token específico encontrado: activo')

    def t_FECHA_FIN(self, t):
        r'"fecha_fin"'
        print('\n-> Token específico encontrado: fecha_fin')

    def t_FECHA_INICIO(self, t):
        r'"fecha_inicio"'
        print('\n-> Token específico encontrado: fecha_inicio')

    def t_ALIANZA(self, t):
        r'"alianza"'
        print('\n-> Token específico encontrado: alianza')

    def t_CARGO(self, t):
        r'"cargo"'
        print('\n-> Token específico encontrado: cargo')

    def t_ESTADO(self, t):
        r'"estado"'
        print('\n-> Token específico encontrado: estado')

    def t_VIDEO(self, t):
        r'"video"'
        print('\n-> Token específico encontrado: video')

    def t_EDAD(self, t):
        r'"edad"'
        print('\n-> Token específico encontrado: edad')

    def t_FOTO(self, t):
        r'"foto"'
        print('\n-> Token específico encontrado: foto')

    def t_CONCLUSION(self, t):
        r'"conclusion"'
        print('\n-> Token específico encontrado: conclusion')

    # Tokens con valores.
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
            print('\n-> Token específico encontrado: float')
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

    # Ignorar espacios y tabulaciones.
    t_ignore = ' \t\n\r'

    # Manejo de errores.
    def t_error(self, t):
        last_cr = t.lexer.lexdata.rfind('\n', 0, t.lexpos)
        line = t.lexer.lineno
        col = t.lexpos if last_cr < 0 else t.lexpos - last_cr - 1
        print(f"Caracter ilegal '{t.value[0]}' en línea {line}, columna {col}")
        t.lexer.skip(1)

    # Construir el lexer.
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Método de prueba.
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(f'---> Token simple encontrado: {tok.type}')
