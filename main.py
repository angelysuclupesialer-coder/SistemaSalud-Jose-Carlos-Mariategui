from datetime import datetime
from modelos.paciente import Paciente
from modelos.profesional import Profesional
from modelos.cita import Cita
from modelos.atencion import Atencion
from modelos.teleorientacion import Teleorientacion
from modelos.emergencia import Emergencia
from modelos.medicamento import Medicamento
from modelos.insumo import Insumo
from modelos.referencia import Referencia
from modelos.usuario import Usuario
from servicios.sistema_service import SistemaService
from seguridad.seguridad import Seguridad


def leer_no_vacio(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: este dato es obligatorio.")


def leer_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                raise ValueError
            return valor
        except ValueError:
            texto = f"un número mayor o igual a {minimo}" if minimo is not None else "un número entero"
            print(f"Error: ingrese {texto}.")


def registrar_paciente(sistema):
    print("\n--- REGISTRO DE PACIENTE ---")
    codigo = leer_no_vacio("Código de historia clínica: ")
    dni = leer_no_vacio("DNI: ")
    Seguridad.validar_dni(dni)
    if sistema.buscar_paciente(dni):
        raise ValueError("Ya existe un paciente con ese DNI.")
    nombre = leer_no_vacio("Nombres: ")
    apellido = leer_no_vacio("Apellidos: ")
    fecha_nacimiento = leer_no_vacio("Fecha de nacimiento (DD/MM/AAAA): ")
    telefono = leer_no_vacio("Teléfono: ")
    paciente = Paciente(codigo, dni, nombre, apellido, fecha_nacimiento, telefono)
    sistema.registrar_paciente(paciente)
    print("Paciente registrado correctamente.")


def buscar_paciente(sistema):
    dni = leer_no_vacio("DNI a buscar: ")
    paciente = sistema.buscar_paciente(dni)
    if not paciente:
        raise ValueError("Paciente no encontrado.")
    paciente.mostrar_datos()


def actualizar_paciente(sistema):
    dni = leer_no_vacio("DNI del paciente: ")
    paciente = sistema.buscar_paciente(dni)
    if not paciente:
        raise ValueError("Paciente no encontrado.")
    telefono = leer_no_vacio("Nuevo teléfono: ")
    paciente.telefono = telefono
    print("Información actualizada correctamente.")


def solicitar_cita(sistema):
    print("\n--- SOLICITAR CITA DESDE CASA ---")
    dni = leer_no_vacio("DNI del paciente: ")
    paciente = sistema.buscar_paciente(dni)
    if not paciente:
        raise ValueError("Paciente no encontrado. Primero debe registrarse.")
    fecha = leer_no_vacio("Fecha (DD/MM/AAAA): ")
    hora = leer_no_vacio("Hora (HH:MM): ")
    tipo = leer_no_vacio("Tipo de atención: ")
    profesional = leer_no_vacio("Profesional/especialidad: ")
    if not sistema.disponible(fecha, hora, profesional):
        raise ValueError("El horario seleccionado no está disponible.")
    codigo = f"C{len(sistema.citas)+1:03d}"
    cita = Cita(codigo, paciente, fecha, hora, tipo, profesional)
    sistema.registrar_cita(cita)
    print(f"Cita {codigo} registrada y queda en estado PROGRAMADA.")


def listar_citas(sistema):
    print("\n--- CITAS REGISTRADAS ---")
    if not sistema.citas:
        print("No existen citas.")
        return
    for cita in sistema.citas:
        cita.mostrar()


def cambiar_cita(sistema, accion):
    codigo = leer_no_vacio("Código de cita: ")
    cita = sistema.buscar_cita(codigo)
    if not cita:
        raise ValueError("Cita no encontrada.")
    if accion == "cancelar":
        cita.cancelar()
        print("Cita cancelada.")
    else:
        fecha = leer_no_vacio("Nueva fecha (DD/MM/AAAA): ")
        hora = leer_no_vacio("Nueva hora (HH:MM): ")
        if not sistema.disponible(fecha, hora, cita.profesional, excluir=cita.codigo):
            raise ValueError("El nuevo horario no está disponible.")
        cita.reprogramar(fecha, hora)
        print("Cita reprogramada.")


def registrar_atencion(sistema):
    codigo_cita = leer_no_vacio("Código de cita atendida: ")
    cita = sistema.buscar_cita(codigo_cita)
    if not cita:
        raise ValueError("Cita no encontrada.")
    if cita.estado not in {"PROGRAMADA", "REPROGRAMADA", "CONFIRMADA"}:
        raise ValueError("La cita no puede registrarse como atendida en su estado actual.")
    motivo = leer_no_vacio("Motivo de consulta: ")
    observacion = leer_no_vacio("Observación general: ")
    codigo = f"A{len(sistema.atenciones)+1:03d}"
    atencion = Atencion(codigo, cita.paciente, cita, datetime.now().strftime("%d/%m/%Y"), motivo, observacion)
    sistema.registrar_atencion(atencion)
    cita.marcar_atendida()
    print("Atención registrada correctamente.")


def historial(sistema):
    dni = leer_no_vacio("DNI del paciente: ")
    paciente = sistema.buscar_paciente(dni)
    if not paciente:
        raise ValueError("Paciente no encontrado.")
    atenciones = [a for a in sistema.atenciones if a.paciente.dni == dni]
    print(f"\n--- HISTORIAL DE {paciente.nombre} {paciente.apellido} ---")
    if not atenciones:
        print("No existen atenciones registradas.")
    for atencion in atenciones:
        atencion.mostrar()


def teleorientacion(sistema):
    dni = leer_no_vacio("DNI del paciente: ")
    paciente = sistema.buscar_paciente(dni)
    if not paciente:
        raise ValueError("Paciente no encontrado.")
    motivo = leer_no_vacio("Motivo de la solicitud: ")
    codigo = f"T{len(sistema.teleorientaciones)+1:03d}"
    solicitud = Teleorientacion(codigo, paciente, datetime.now().strftime("%d/%m/%Y"), motivo)
    sistema.teleorientaciones.append(solicitud)
    print("Solicitud de teleorientación registrada.")
    print("Nota: si existe una emergencia o situación grave, debe buscar atención presencial inmediata.")


def registrar_emergencia(sistema):
    dni = leer_no_vacio("DNI del paciente: ")
    paciente = sistema.buscar_paciente(dni)
    if not paciente:
        raise ValueError("Paciente no encontrado.")
    descripcion = leer_no_vacio("Descripción breve de la situación reportada: ")
    codigo = f"E{len(sistema.emergencias)+1:03d}"
    emergencia = Emergencia(codigo, paciente, datetime.now().strftime("%d/%m/%Y %H:%M"), descripcion)
    sistema.emergencias.append(emergencia)
    emergencia.derivar()
    print("Caso registrado.")
    print("ALERTA: este módulo no diagnostica ni reemplaza la atención de emergencia. Acuda inmediatamente al servicio de emergencia más cercano.")


def registrar_referencia(sistema):
    dni = leer_no_vacio("DNI del paciente: ")
    paciente = sistema.buscar_paciente(dni)
    if not paciente:
        raise ValueError("Paciente no encontrado.")
    motivo = leer_no_vacio("Motivo de referencia: ")
    destino = leer_no_vacio("Establecimiento de destino: ")
    codigo = f"R{len(sistema.referencias)+1:03d}"
    referencia = Referencia(codigo, paciente, motivo, destino)
    sistema.referencias.append(referencia)
    print("Referencia registrada.")


def inventario(sistema):
    print("\n--- INVENTARIO ---")
    print("Medicamentos:")
    for item in sistema.medicamentos:
        item.mostrar()
    print("\nInsumos:")
    for item in sistema.insumos:
        item.mostrar()


def movimiento_medicamento(sistema, entrada):
    codigo = leer_no_vacio("Código del medicamento: ")
    medicamento = next((m for m in sistema.medicamentos if m.codigo == codigo), None)
    if not medicamento:
        raise ValueError("Medicamento no encontrado.")
    cantidad = leer_entero("Cantidad: ", 1)
    if entrada:
        medicamento.entrada(cantidad)
        print("Entrada registrada.")
    else:
        medicamento.salida(cantidad)
        print("Salida registrada.")


def reportes(sistema):
    print("\n--- REPORTES ---")
    print(f"Pacientes registrados: {len(sistema.pacientes)}")
    print(f"Citas registradas: {len(sistema.citas)}")
    print(f"Atenciones realizadas: {len(sistema.atenciones)}")
    print(f"Solicitudes de teleorientación: {len(sistema.teleorientaciones)}")
    print(f"Casos de emergencia registrados: {len(sistema.emergencias)}")
    print(f"Referencias: {len(sistema.referencias)}")
    nombres = sistema.nombres_pacientes()
    print("Pacientes:", ", ".join(nombres) if nombres else "ninguno")
    bajos = sistema.medicamentos_bajo_stock()
    print("Medicamentos con bajo stock:", ", ".join(m.nombre for m in bajos) if bajos else "ninguno")


def cargar_datos_demo(sistema):
    if sistema.pacientes:
        return
    p = Paciente("HC001", "74563218", "Juan", "Pérez", "15/05/1990", "987654321")
    p2 = Paciente("HC002", "70123456", "María", "Gómez", "21/08/1985", "986123456")
    sistema.registrar_paciente(p)
    sistema.registrar_paciente(p2)
    sistema.medicamentos.extend([
        Medicamento("M001", "Paracetamol", "L001", "31/12/2027", 10, 20),
        Medicamento("M002", "Amoxicilina", "L002", "30/06/2027", 50, 20),
        Medicamento("M003", "Ibuprofeno", "L003", "15/09/2027", 5, 15),
    ])
    sistema.insumos.extend([
        Insumo("I001", "Guantes", 100, 30),
        Insumo("I002", "Gasas", 20, 25),
    ])
    sistema.profesionales.extend([
        Profesional("PR001", "Ana", "Torres", "999111222", "Medicina General"),
        Profesional("PR002", "Luis", "Ramos", "999333444", "Odontología"),
    ])


def menu():
    print("""
========================================================
 SISTEMA INTEGRAL DE GESTIÓN Y ATENCIÓN
 Puesto de Salud José Carlos Mariátegui - SJL
========================================================
 1. Registrar paciente
 2. Buscar paciente
 3. Actualizar paciente
 4. Solicitar cita desde casa
 5. Consultar citas
 6. Cancelar cita
 7. Reprogramar cita
 8. Registrar atención
 9. Consultar historial de atenciones
10. Solicitar teleorientación
11. Registrar emergencia
12. Registrar referencia
13. Consultar inventario
14. Registrar entrada de medicamento
15. Registrar salida de medicamento
16. Ver alertas de bajo stock
17. Generar reportes
18. Ver profesionales
19. Salir
""")


def main():
    sistema = SistemaService()
    cargar_datos_demo(sistema)

    while True:
        menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            acciones = {
                1: lambda: registrar_paciente(sistema),
                2: lambda: buscar_paciente(sistema),
                3: lambda: actualizar_paciente(sistema),
                4: lambda: solicitar_cita(sistema),
                5: lambda: listar_citas(sistema),
                6: lambda: cambiar_cita(sistema, "cancelar"),
                7: lambda: cambiar_cita(sistema, "reprogramar"),
                8: lambda: registrar_atencion(sistema),
                9: lambda: historial(sistema),
                10: lambda: teleorientacion(sistema),
                11: lambda: registrar_emergencia(sistema),
                12: lambda: registrar_referencia(sistema),
                13: lambda: inventario(sistema),
                14: lambda: movimiento_medicamento(sistema, True),
                15: lambda: movimiento_medicamento(sistema, False),
                16: lambda: [m.mostrar() for m in sistema.medicamentos_bajo_stock()],
                17: lambda: reportes(sistema),
                18: lambda: [p.mostrar_datos() for p in sistema.profesionales],
                19: lambda: "SALIR",
            }
            if opcion not in acciones:
                print("Opción no válida.")
                continue
            resultado = acciones[opcion]()
            if resultado == "SALIR":
                print("Gracias por utilizar el sistema.")
                break
        except (ValueError, TypeError) as error:
            print(f"\nError controlado: {error}")


if __name__ == "__main__":
    main()
