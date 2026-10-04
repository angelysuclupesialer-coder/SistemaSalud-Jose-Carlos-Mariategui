class Persona:
    def __init__(self, nombre, apellido, telefono):
        self._nombre = nombre
        self._apellido = apellido
        self._telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if not valor.strip():
            raise ValueError("El teléfono no puede estar vacío.")
        self._telefono = valor

    def nombre_completo(self):
        return f"{self._nombre} {self._apellido}"

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre_completo()}")
        print(f"Teléfono: {self._telefono}")
