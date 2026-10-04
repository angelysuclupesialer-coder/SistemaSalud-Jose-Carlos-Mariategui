class Medicamento:
    def __init__(self, codigo, nombre, lote, vencimiento, stock, stock_minimo):
        self.codigo = codigo
        self.nombre = nombre
        self.lote = lote
        self.vencimiento = vencimiento
        self.stock = stock
        self.stock_minimo = stock_minimo

    def tiene_stock_bajo(self):
        return self.stock <= self.stock_minimo

    def entrada(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        self.stock += cantidad

    def salida(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        if cantidad > self.stock:
            raise ValueError("Stock insuficiente.")
        self.stock -= cantidad

    def mostrar(self):
        estado = "STOCK BAJO" if self.tiene_stock_bajo() else "STOCK NORMAL"
        print(f"{self.codigo} | {self.nombre} | Stock: {self.stock} | {estado}")
