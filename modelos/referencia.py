class Referencia:
    def __init__(self, codigo, paciente, motivo, destino):
        self.codigo = codigo
        self.paciente = paciente
        self.motivo = motivo
        self.destino = destino
        self.estado = "PENDIENTE"

    def marcar_enviada(self):
        self.estado = "ENVIADA"
