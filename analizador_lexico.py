class Tokens:
    def __init__(self,t):
        self.tokens = ['LLA_A', 'LLA_C', 'CORCH_A', 'CORCH_C', 'COMILLAS', 'COMA', '2PUNTOS', 'STRING', 'INTEGER', 'BOOLEAN', 'DATE', 'FLOAT',
          'NOMBRE_TEAM', 'CALLE', 'CIUDAD', 'PAIS', 'ACTIVO', 'FECHA_FIN', 'FECHA_INICIO',
          'UNIVERSIDAD', 'ALIANZA', 'CARRERA', 'ASIGNATURA', 'LINK', 'CARGO', 'ESTADO', 'IDENTIDAD', 'DIRECCION',
          'TAREA', 'EQUIPOS', 'INTEGRANTES', 'PROYECTOS', 'EDAD', 'FOTO', 'VIDEO', 'CONCLUSION'
          ]
        # Expresiones regulares tokens simples
        self.t_LLA_A = r'\{'
        self.t_LLA_C = r'\}'
        self.t_CORCH_A = r'\['
        self.t_CORCH_C = r'\]'
        self.t_COMA = r','
        self.t_2PUNTOS = r':'
        self.t_COMILLAS = r'"'        
        self.t_ignore = ' \t\n\r'
        self.t_TAREA = r'"tarea"'
        self.t_EQUIPOS = r'"equipos"'
        self.t_INTEGRANTES = r'"integrantes"'
        self.t_PROYECTOS = r'"proyectos"'
        self.t_ignore_COMMENT = r'\#.*'


    # Expresiones regulares para tokens especificos
    def t_NOMBRE_TEAM(self,t):
        r'"nombre_equipo"'
        print('TOKEN ENCONTRADO: "nombre_equipo"')


    def t_IDENTIDAD(self,t):
        r'"identidad_equipo"'
        print('TOKEN ENCONTRADO: "identidad_equipo"')


    def t_LINK(self,t):
        r'"link"'
        print('TOKEN ENCONTRADO: "link"')


    def t_ASIGNATURA(self,t):
        r'"asignatura"'
        print('TOKEN ENCONTRADO:"asignatura"')


    def t_CARRERA(self,t):
        r'"carrera"'
        print('TOKEN ENCONTRADO: "carrera"')


    def t_UNIVERSIDAD(self,t):
        r'"universidad_regional"'
        print('TOKEN ENCONTRADO: "universidad_regional"')


    def t_DIRECCION(self,t):
        r'"direccion"'
        print('TOKEN ENCONTRADO: "direccion"')


    def t_CALLE(self,t):
        r'"calle"'
        print('TOKEN ENCONTRADO: "calle"')


    def t_CIUDAD(self,t):
        r'"CIUDAD"'
        print('TOKEN ENCONTRADO: "ciudad"')


    def t_PAIS(self,t):
        r'"pais"'
        print('TOKEN ENCONTRADO: "pais"')


    def t_ACTIVO(self,t):
        r'"activo"'
        print('TOKEN ENCONTRADO: "activo"')


    def t_FECHA_FIN(self,t):
        r'"fecha_fin'
        print('TOKEN ENCONTRADO: "fecha_fin"')

    def t_FECHA_INICIO(self,t):
        r'"fecha_inicio"'
        print('TOKEN ENCONTRADO: "fecha_inicio"')


    def t_ALIANZA(self,t):
        r'"alianza"'
        print('TOKEN ENCONTRADO: "alianza"')


    def t_CARGO(self,t):
        r'"cargo"'
        print('TOKEN ENCONTRADO: "cargo"')


    def t_ESTADO(self,t):
        r'"estado"'
        print('TOKEN ENCONTRADO: "estado"')


    def t_VIDEO(self,t):
        r'"video"'
        print('TOKEN ENCONTRADO: "video"')


    def t_EDAD(self,t):
        r'"edad"'
        print('TOKEN ENCONTRADO: "edad"')


    def t_FOTO(self,t):
        r'"foto"'
        print('TOKEN ENCONTRADO: "foto"')


    def t_CONCLUSION(self,t):
        r'"conclusion"'
        print('"TOKEN ENCONTRADO: conclusion"')


    def t_INTEGER(self,t):
        r'\d+'
        print('"TOKEN ENCONTRADO: integer"')


    def t_STRING(self,t):
        r'\"([^\\\n]|(\\.))*?\"'
        print('"TOKEN ENCONTRADO: string"')


    def t_BOOLEAN(self,t):
        r'true|false'
        print('"TOKEN ENCONTRADO: boolean')


    def t_FLOAT(self,t):
        r'\d+\. \d+'
        print('"TOKEN ENCONTRADO: float"')


    def t_DATE(self,t):
        r'"\d{4}-\d{2}-\d{2}"'
        print('"TOKEN ENCONTRADO: date"')


    # Manejo de errores
    @staticmethod
    def t_error(self,t):
        print(f"Caracter ilegal '{t.value[0]}'")
        t.lexer.skip(1)

