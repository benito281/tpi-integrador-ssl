import ply.lex as lex

class LexerTokens(object):
        # Lista de tokens
        tokens = ('LLA_A', 'LLA_C', 'CORCH_A', 'CORCH_C', 'COMILLAS', 'COMA', '2PUNTOS', 'STRING', 'INTEGER', 'BOOLEAN', 'DATE', 'FLOAT',
          'NOMBRE_TEAM', 'CALLE', 'CIUDAD', 'PAIS', 'ACTIVO', 'FECHA_FIN', 'FECHA_INICIO',
          'UNIVERSIDAD', 'ALIANZA', 'CARRERA', 'ASIGNATURA', 'LINK', 'CARGO', 'ESTADO', 'IDENTIDAD', 'DIRECCION',
          'TAREA', 'EQUIPOS', 'INTEGRANTES', 'PROYECTOS', 'EDAD', 'FOTO', 'VIDEO', 'CONCLUSION', 'GUION','PUNTO', 'EMAIL'
        )
        # Expresiones regulares tokens simples
        t_LLA_A = r'\{'
        t_LLA_C = r'\}'
        t_CORCH_A = r'\['
        t_CORCH_C = r'\]'
        t_COMA = r','
        t_2PUNTOS = r':'
        t_COMILLAS = r'"'
        t_ignore_COMMENT = r'\#.*'
        t_GUION = r'-'
        t_PUNTO = r'.'
        


    # Expresiones regulares para tokens especificos
        def t_NOMBRE_TEAM(self,t):
            r'"nombre_equipo"'
            print('Token del tipo : nombre_equipo')


        def t_IDENTIDAD(self,t):
            r'"identidad_equipo"'
            print('Token del tipo : identidad_equipo')


        def t_LINK(self,t):
            r'"link"'
            print('Token del tipo : link')


        def t_ASIGNATURA(self,t):
            r'"asignatura"'
            print('Token del tipo : asignatura')


        def t_CARRERA(self,t):
            r'"carrera"'
            print('Token del tipo : carrera')


        def t_UNIVERSIDAD(self,t):
            r'"universidad_regional"'
            print('Token del tipo : universidad_regional')


        def t_DIRECCION(self,t):
            r'"direccion"'
            print('Token del tipo : "direccion"')


        def t_CALLE(self,t):
            r'"calle"'
            print('Token del tipo : calle')


        def t_CIUDAD(self,t):
            r'"CIUDAD"'
            print('Token del tipo : ciudad')


        def t_PAIS(self,t):
            r'"pais"'
            print('Token del tipo : pais')


        def t_ACTIVO(self,t):
            r'"activo"'
            print('Token del tipo : activo')


        def t_FECHA_FIN(self,t):
            r'"fecha_fin"'
            print('Token del tipo : fecha_fin')

        def t_FECHA_INICIO(self,t):
            r'"fecha_inicio"'
            print('Token del tipo : fecha_inicio')


        def t_ALIANZA(self,t):
            r'"alianza"'
            print('Token del tipo : alianza')


        def t_CARGO(self,t):
            r'"cargo"'
            print('Token del tipo : cargo')


        def t_ESTADO(self,t):
            r'"estado"'
            print('Token del tipo : estado')


        def t_VIDEO(self,t):
            r'"video"'
            print('Token del tipo : video')


        def t_EDAD(self,t):
            r'"edad"'
            print('Token del tipo : edad')


        def t_FOTO(self,t):
            r'"foto"'
            print('Token del tipo : foto')


        def t_CONCLUSION(self,t):
            r'"conclusion"'
            print('Token del tipo : conclusion')


        def t_INTEGER(self,t):
            r'\d+'
            print('Token del tipo : integer')

        def t_EMAIL(self,t):
            r'"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"'
            print('Token del tipo : EMAIL')

        def t_STRING(self,t):
            r'\"([^\\\n]|(\\.))*?\"'
            print('Token del tipo : string')


        def t_BOOLEAN(self,t):
            r'true|false'
            print('Token del tipo : boolean')


        def t_FLOAT(self,t):
            r'\d+\. \d+'
            print('Token del tipo : float')


        def t_DATE(self,t):
            r'"\d{4}-\d{2}-\d{2}"'
            print('Token del tipo : date')
        

        # Ignorar espacios y tabulaciones
        t_ignore = ' \t\n\r'

        # Manejo de errores
        def t_error(self,t):
            # Para calcular la columna, buscamos la última '\n' antes de la posición:
            last_cr = t.lexer.lexdata.rfind('\n', 0, t.lexpos)
            line = t.lexer.lineno #Linea donde se encontro el error
            if last_cr < 0:
                col = t.lexpos
            else:
                col = t.lexpos - last_cr - 1

            print(f"Caracter ilegal '{t.value[0]}' en línea {line}, columna {col}")

            t.lexer.skip(1)
        
        # Método para construir el lexer
        def build(self,**kwargs):
            self.lexer = lex.lex(module=self, **kwargs)
        
        # Método para probar el lexer
        def test(self, data):
            self.lexer.input(data)
            while True:
                tok = self.lexer.token()
                if not tok:
                    break
                print(f'TOKEN ENCONTRADO: {tok.type}\n')
            
            


