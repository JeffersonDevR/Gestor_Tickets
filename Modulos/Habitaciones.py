class Habitacion:
    """
    Clase que representa una habitación del hotel.
    """
    def __init__(self, numero, tipo, tarifa):
        """
        Inicializa un nuevo objeto Habitacion.

        Args:
            numero (str): El número de la habitación.
            tipo (str): El tipo de habitación (ej. Sencilla, Doble, Suite).
            tarifa (float): El precio por noche.
        """
        self.numero = numero
        self.tipo = tipo
        self.tarifa = float(tarifa)
        self.estado = "disponible"  # Por defecto, una habitación siempre está disponible al crearla.

    def mostrar_info(self):
        """
        Imprime la información detallada de la habitación.
        """
        print(f"Habitación {self.numero} | Tipo: {self.tipo} | Tarifa: ${self.tarifa:,.2f} | Estado: {self.estado}")

    def cambiar_estado(self, nuevo_estado):
        """
        Cambia el estado de la habitación.

        Args:
            nuevo_estado (str): El nuevo estado ('disponible', 'ocupada', 'mantenimiento').
        """
        if nuevo_estado in ["disponible", "ocupada", "mantenimiento"]:
            self.estado = nuevo_estado
            print(f"Habitación {self.numero} ahora está '{nuevo_estado}'.")
        else:
            print("Estado no válido. Use: 'disponible', 'ocupada' o 'mantenimiento'.")


class GestorHabitaciones:
    """
    Clase para gestionar el conjunto de habitaciones del hotel.
    """
    def __init__(self):
        """
        Inicializa el gestor de habitaciones.
        """
        self.habitaciones = []

    def agregar_habitacion(self, numero, tipo, tarifa):
        """
        Agrega una nueva habitación al hotel.

        Args:
            numero (str): Número de la nueva habitación.
            tipo (str): Tipo de la nueva habitación.
            tarifa (float): Tarifa de la nueva habitación.
        """
        # Verifica si ya existe una habitación con el mismo número.
        if any(h.numero == numero for h in self.habitaciones):
            print(f"La habitación {numero} ya está registrada.")
            return

        nueva_habitacion = Habitacion(numero, tipo, tarifa)
        self.habitaciones.append(nueva_habitacion)
        print(f"Habitación {numero} registrada correctamente.")

    def mostrar_todas(self):
        """
        Muestra la información de todas las habitaciones registradas.
        """
        if not self.habitaciones:
            print("No hay habitaciones registradas.")
        else:
            print("\n--- Listado de habitaciones ---")
            for hab in self.habitaciones:
                hab.mostrar_info()

    def buscar_por_estado(self, estado):
        """
        Busca y muestra habitaciones por un estado específico.

        Args:
            estado (str): El estado a buscar.

        Returns:
            list: Una lista de habitaciones que coinciden con el estado.
        """
        return [h for h in self.habitaciones if h.estado == estado]

    def buscar_por_tipo(self, tipo):
        """
        Busca y muestra habitaciones por un tipo específico.

        Args:
            tipo (str): El tipo de habitación a buscar.

        Returns:
            list: Una lista de habitaciones que coinciden con el tipo.
        """
        return [h for h in self.habitaciones if h.tipo.lower() == tipo.lower()]

    def ordenar_por_tarifa(self):
        """
        Devuelve una lista de habitaciones ordenadas por tarifa.

        Returns:
            list: Lista de habitaciones ordenadas.
        """
        return sorted(self.habitaciones, key=lambda x: x.tarifa)