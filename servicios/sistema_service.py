from servicios.reportes import ReporteService


class SistemaService:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.pacientes = []
            cls._instancia.profesionales = []
            cls._instancia.citas = []
            cls._instancia.atenciones = []
            cls._instancia.teleorientaciones = []
            cls._instancia.emergencias = []
            cls._instancia.referencias = []
            cls._instancia.medicamentos = []
            cls._instancia.insumos = []
        return cls._instancia

    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def buscar_paciente(self, dni):
        return next((p for p in self.pacientes if p.dni == dni), None)

    def registrar_cita(self, cita):
        self.citas.append(cita)

    def buscar_cita(self, codigo):
        return next((c for c in self.citas if c.codigo == codigo), None)

    def disponible(self, fecha, hora, profesional, excluir=None):
        return not any(
            c.fecha == fecha and c.hora == hora and c.profesional == profesional
            and c.estado != "CANCELADA" and c.codigo != excluir
            for c in self.citas
        )

    def registrar_atencion(self, atencion):
        self.atenciones.append(atencion)

    def medicamentos_bajo_stock(self):
        return ReporteService.filtrar_stock_bajo(self.medicamentos)

    def nombres_pacientes(self):
        return ReporteService.nombres(self.pacientes)
