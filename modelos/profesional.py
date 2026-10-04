from modelos.persona import Persona


class Profesional(Persona):
    def __init__(self, codigo, nombre, apellido, telefono, especialidad):
        super().__init__(nombre, apellido, telefono)
        self._codigo = codigo
        self._especialidad = especialidad

    @property
    def codigo(self):
        return self._codigo

    @property
    def especialidad(self):
        return self._especialidad

    def mostrar_datos(self):
        print(f"{self._codigo} | {self.nombre_completo()} | {self._especialidad}")
