class Insumo:
    def __init__(self, codigo, nombre, cantidad, cantidad_minima):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.cantidad_minima = cantidad_minima

    def tiene_stock_bajo(self):
        return self.cantidad <= self.cantidad_minima

    def mostrar(self):
        estado = "STOCK BAJO" if self.tiene_stock_bajo() else "STOCK NORMAL"
        print(f"{self.codigo} | {self.nombre} | Cantidad: {self.cantidad} | {estado}")
