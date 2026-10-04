import tkinter as tk
from tkinter import messagebox
from main import cargar_datos_demo
from servicios.sistema_service import SistemaService


class SistemaGUI:
    """Interfaz orientada a eventos: los botones disparan handlers."""

    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Salud - José Carlos Mariátegui")
        self.root.geometry("600x500")
        self.sistema = SistemaService()
        cargar_datos_demo(self.sistema)

        tk.Label(
            root,
            text="Sistema Integral de Gestión y Atención",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        tk.Label(
            root,
            text="Puesto de Salud José Carlos Mariátegui - SJL"
        ).pack()

        botones = [
            ("Pacientes registrados", self.mostrar_pacientes),
            ("Citas registradas", self.mostrar_citas),
            ("Alertas de stock", self.mostrar_stock),
            ("Reportes", self.mostrar_reportes),
            ("Emergencia", self.alerta_emergencia),
            ("Salir", root.destroy),
        ]

        for texto, comando in botones:
            tk.Button(
                root, text=texto, width=35, command=comando
            ).pack(pady=6)

        self.salida = tk.Text(root, height=12, width=70)
        self.salida.pack(pady=10)

    def limpiar(self):
        self.salida.delete("1.0", tk.END)

    def mostrar_pacientes(self):
        self.limpiar()
        for paciente in self.sistema.pacientes:
            self.salida.insert(
                tk.END,
                f"{paciente.nombre_completo()} - DNI {paciente.dni[-4:].rjust(8, '*')}\n"
            )

    def mostrar_citas(self):
        self.limpiar()
        if not self.sistema.citas:
            self.salida.insert(tk.END, "No hay citas.\n")
            return
        for cita in self.sistema.citas:
            self.salida.insert(
                tk.END,
                f"{cita.codigo} | {cita.fecha} {cita.hora} | "
                f"{cita.profesional} | {cita.estado}\n"
            )

    def mostrar_stock(self):
        self.limpiar()
        bajos = self.sistema.medicamentos_bajo_stock()
        if not bajos:
            self.salida.insert(tk.END, "No hay medicamentos con stock bajo.\n")
        for medicamento in bajos:
            self.salida.insert(tk.END, f"{medicamento.nombre}: {medicamento.stock}\n")

    def mostrar_reportes(self):
        self.limpiar()
        self.salida.insert(
            tk.END,
            f"Pacientes: {len(self.sistema.pacientes)}\n"
            f"Citas: {len(self.sistema.citas)}\n"
            f"Atenciones: {len(self.sistema.atenciones)}\n"
            f"Teleorientaciones: {len(self.sistema.teleorientaciones)}\n"
            f"Emergencias: {len(self.sistema.emergencias)}\n"
            f"Referencias: {len(self.sistema.referencias)}\n"
        )

    def alerta_emergencia(self):
        messagebox.showwarning(
            "Emergencia",
            "Este sistema no diagnostica emergencias. "
            "Ante una situación grave, acuda inmediatamente "
            "al servicio de emergencia más cercano."
        )


if __name__ == "__main__":
    root = tk.Tk()
    SistemaGUI(root)
    root.mainloop()
