# Sistema Integral de Gestión y Atención - Puesto de Salud José Carlos Mariátegui

Proyecto académico en Python 3.x.

## Casos incluidos
- Registro y consulta de pacientes.
- Solicitud de cita desde casa.
- Consulta, cancelación y reprogramación de citas.
- Registro e historial de atenciones.
- Teleorientación.
- Emergencia presencial: el personal registra el caso, se inicia atención y, si corresponde, se crea una referencia. No se genera una cita de emergencia.
- Referencia a otro establecimiento.
- Profesionales de salud.
- Medicamentos e insumos.
- Entradas, salidas y alertas de stock.
- Reportes.
- Protección básica de datos con validación y enmascaramiento de DNI.
- POO, herencia, encapsulamiento y polimorfismo.
- Enum para estados.
- Programación funcional con map, filter y reduce.
- Patrón Singleton.
- Manejo de excepciones.
- Pruebas automatizadas con pytest.

## Ejecutar
python main.py

## Pruebas
python -m pytest -q

Los datos incluidos son ficticios y solo se usan para demostración académica.

## Funcionalidades del módulo de pacientes

El sistema permite registrar pacientes, consultar sus datos,
validar el DNI y proteger parcialmente la información personal.

## Gestión de citas

El sistema permite organizar y registrar las citas de los pacientes,
facilitando el control de la atención médica.

## Gestión de historias clínicas

El sistema permite almacenar y consultar información relacionada
con la historia clínica de los pacientes.

## Seguridad de la información

El sistema considera medidas básicas para proteger los datos
personales de los pacientes y mantener la información organizada.