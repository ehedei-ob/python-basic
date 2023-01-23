class Alumno:
    def __init__(self, nombre, nota):
        super().__init__()
        self.nombre = nombre
        self.nota = nota


    def imprimir(self):
        print(f'El nombre del alumno es {self.nombre} y su nota final es de {self.nota}')

    def resultado(self):
        resultado = 'El alumno ha suspendido' if self.nota < 5 else 'El alumno ha aprobado'
        print(resultado)


alumno1 = Alumno('Pedro', 4)
alumno2 = Alumno('Pepita', 8)

alumno1.imprimir()
alumno1.resultado()

alumno2.imprimir()
alumno2.resultado()
