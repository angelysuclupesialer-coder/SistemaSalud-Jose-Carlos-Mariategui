class Seguridad:
    @staticmethod
    def validar_dni(dni):
        if not dni.isdigit():
            raise ValueError("El DNI debe contener solamente números.")
        if len(dni) != 8:
            raise ValueError("El DNI debe tener 8 dígitos.")
        return True

    @staticmethod
    def enmascarar_dni(dni):
        return "****" + dni[-4:]
