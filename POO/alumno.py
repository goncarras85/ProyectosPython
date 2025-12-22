from persona import Persona
class Alumno(Persona):

    def __init__(self,dni,nombre,edad,curso,nota):
        super().__init__(dni,nombre,edad)
        self.curso = curso
        self.nota = nota

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self,curso):
        self._curso = curso

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self,nota):
        if nota >= 0 and nota <= 10:
            self._nota = nota
        else:
            self._nota = -1
            print("Nota incorrecta")

    def mostrar(self):
        return super().mostrar() + " " + self.curso + " " + str(self.nota)


