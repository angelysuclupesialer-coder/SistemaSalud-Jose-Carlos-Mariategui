import pytest
from modelos.paciente import Paciente
from modelos.medicamento import Medicamento
from modelos.cita import Cita
from servicios.sistema_service import SistemaService
from servicios.reportes import ReporteService


def test_validar_dni():
    paciente = Paciente("HC01", "74563218", "Ana", "Pérez", "01/01/2000", "999999999")
    assert paciente.dni == "74563218"


def test_dni_invalido():
    with pytest.raises(ValueError):
        Paciente("HC01", "123", "Ana", "Pérez", "01/01/2000", "999999999")


def test_stock_insuficiente():
    medicamento = Medicamento("M1", "Paracetamol", "L1", "31/12/2027", 5, 2)
    with pytest.raises(ValueError):
        medicamento.salida(10)


def test_filter_stock_bajo():
    medicamentos = [
        Medicamento("M1", "A", "L1", "31/12/2027", 5, 10),
        Medicamento("M2", "B", "L2", "31/12/2027", 50, 10),
    ]
    bajos = ReporteService.filtrar_stock_bajo(medicamentos)
    assert len(bajos) == 1
    assert bajos[0].nombre == "A"


def test_disponibilidad_cita():
    sistema = SistemaService()
    sistema.pacientes.clear()
    sistema.citas.clear()
    paciente = Paciente("HC02", "70123456", "Luis", "Ramos", "01/01/1990", "988888888")
    cita = Cita("C1", paciente, "10/10/2026", "09:00", "Medicina General", "Ana Torres")
    sistema.registrar_cita(cita)
    assert sistema.disponible("10/10/2026", "09:00", "Ana Torres") is False
