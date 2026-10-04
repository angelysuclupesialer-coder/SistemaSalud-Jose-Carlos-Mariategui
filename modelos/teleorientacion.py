class Teleorientacion:
    def __init__(self, codigo, paciente, fecha, motivo):
        self.codigo = codigo
        self.paciente = paciente
        self.fecha = fecha
        self.motivo = motivo
        self.estado = "PENDIENTE"

    def atender(self):
        self.estado = "ATENDIDA"
