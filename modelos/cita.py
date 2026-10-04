class Cita:
    ESTADOS_VALIDOS = {"PROGRAMADA", "CONFIRMADA", "REPROGRAMADA", "ATENDIDA", "CANCELADA"}

    def __init__(self, codigo, paciente, fecha, hora, tipo_atencion, profesional):
        self.codigo = codigo
        self.paciente = paciente
        self.fecha = fecha
        self.hora = hora
        self.tipo_atencion = tipo_atencion
        self.profesional = profesional
        self.estado = "PROGRAMADA"

    def confirmar(self):
        self.estado = "CONFIRMADA"

    def cancelar(self):
        self.estado = "CANCELADA"

    def reprogramar(self, nueva_fecha, nueva_hora):
        self.fecha = nueva_fecha
        self.hora = nueva_hora
        self.estado = "REPROGRAMADA"

    def marcar_atendida(self):
        self.estado = "ATENDIDA"

    def mostrar(self):
        print(
            f"{self.codigo} | {self.paciente.nombre_completo()} | "
            f"{self.fecha} {self.hora} | {self.tipo_atencion} | "
            f"{self.profesional} | {self.estado}"
        )
