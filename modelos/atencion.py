class Atencion:
    def __init__(self, codigo, paciente, cita, fecha, motivo, observacion):
        self.codigo = codigo
        self.paciente = paciente
        self.cita = cita
        self.fecha = fecha
        self.motivo = motivo
        self.observacion = observacion

    def mostrar(self):
        print(f"\n{self.codigo} | Fecha: {self.fecha}")
        print(f"Paciente: {self.paciente.nombre_completo()}")
        print(f"Motivo: {self.motivo}")
        print(f"Observación: {self.observacion}")
