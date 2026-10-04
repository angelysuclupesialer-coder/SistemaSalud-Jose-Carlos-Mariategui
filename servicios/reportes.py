from functools import reduce


class ReporteService:
    @staticmethod
    def filtrar_stock_bajo(medicamentos):
        return list(filter(lambda m: m.tiene_stock_bajo(), medicamentos))

    @staticmethod
    def nombres(pacientes):
        return list(map(lambda p: p.nombre_completo(), pacientes))

    @staticmethod
    def total_stock(medicamentos):
        return reduce(lambda total, m: total + m.stock, medicamentos, 0)
