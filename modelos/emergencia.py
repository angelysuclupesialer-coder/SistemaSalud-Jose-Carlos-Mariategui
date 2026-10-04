from modelos.enums import EstadoEmergencia

class Emergencia:
    def __init__(self, codigo, paciente, fecha, descripcion):
        self.codigo = codigo
        self.paciente = paciente
        self.fecha = fecha
        self.descripcion = descripcion
        self.estado = EstadoEmergencia.REPORTADA

    def iniciar_atencion(self):
        self.estado = EstadoEmergencia.EN_ATENCION

    def derivar(self):
        self.estado = EstadoEmergencia.DERIVADA

    def marcar_atendida(self):
        self.estado = EstadoEmergencia.ATENDIDA

    def mostrar(self):
        print(f"{self.codigo} | {self.paciente.nombre_completo()} | {self.fecha} | {self.descripcion} | {self.estado.value}")
