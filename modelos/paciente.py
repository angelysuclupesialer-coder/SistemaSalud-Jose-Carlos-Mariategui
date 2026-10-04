from modelos.persona import Persona
from seguridad.seguridad import Seguridad


class Paciente(Persona):
    def __init__(self, codigo, dni, nombre, apellido, fecha_nacimiento, telefono):
        super().__init__(nombre, apellido, telefono)
        Seguridad.validar_dni(dni)
        self._codigo = codigo
        self._dni = dni
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def codigo(self):
        return self._codigo

    @property
    def dni(self):
        return self._dni

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    def mostrar_datos(self):
        print("\n--- DATOS DEL PACIENTE ---")
        print(f"Código: {self._codigo}")
        print(f"DNI: {Seguridad.enmascarar_dni(self._dni)}")
        print(f"Nombre: {self.nombre_completo()}")
        print(f"Fecha de nacimiento: {self._fecha_nacimiento}")
        print(f"Teléfono: {self._telefono}")
