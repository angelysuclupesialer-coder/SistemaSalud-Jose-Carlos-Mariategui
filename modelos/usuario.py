class Usuario:
    ROLES = {"PACIENTE", "PROFESIONAL", "ADMINISTRADOR"}

    def __init__(self, codigo, nombre_usuario, rol):
        if rol not in self.ROLES:
            raise ValueError("Rol no válido.")
        self.codigo = codigo
        self.nombre_usuario = nombre_usuario
        self.rol = rol
