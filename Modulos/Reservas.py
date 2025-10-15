from datetime import datetime

class Reserva:
    """
    Clase que representa una reserva en el hotel.
    """
    def __init__(self, cliente, habitacion, fecha_inicio, fecha_fin):
        """
        Inicializa un nuevo objeto Reserva.

        Args:
            cliente (Cliente): El objeto del cliente que realiza la reserva.
            habitacion (Habitacion): El objeto de la habitación que se reserva.
            fecha_inicio (datetime): La fecha de inicio de la reserva.
            fecha_fin (datetime): La fecha de fin de la reserva.
        """
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = "activa"  # Otros estados: 'cancelada', 'completada'

    def __str__(self):
        """
        Devuelve una representación en cadena de la reserva.
        """
        return (f"Reserva para {self.cliente.nombre} en la habitación {self.habitacion.numero} "
                f"del {self.fecha_inicio.strftime('%Y-%m-%d')} al {self.fecha_fin.strftime('%Y-%m-%d')}. "
                f"Estado: {self.estado}.")


class GestorReservas:
    """
    Clase para gestionar todas las reservas del hotel.
    """
    def __init__(self, gestor_habitaciones):
        """
        Inicializa el gestor de reservas.

        Args:
            gestor_habitaciones (GestorHabitaciones): El gestor de habitaciones para verificar disponibilidad.
        """
        self.reservas = []
        self.gestor_habitaciones = gestor_habitaciones

    def crear_reserva(self, cliente, numero_habitacion, fecha_inicio, fecha_fin):
        """
        Crea una nueva reserva.

        Args:
            cliente (Cliente): El cliente que hace la reserva.
            numero_habitacion (str): El número de la habitación a reservar.
            fecha_inicio (datetime): Fecha de inicio de la reserva.
            fecha_fin (datetime): Fecha de fin de la reserva.

        Returns:
            Reserva: El objeto de la reserva creada o None si no se pudo crear.
        """
        # Busca la habitación por su número.
        habitacion_a_reservar = next((h for h in self.gestor_habitaciones.habitaciones if h.numero == numero_habitacion), None)

        if not habitacion_a_reservar:
            print(f"La habitación {numero_habitacion} no existe.")
            return None

        if habitacion_a_reservar.estado != "disponible":
            print(f"La habitación {numero_habitacion} no está disponible.")
            return None

        # Crea la reserva y la añade a la lista.
        nueva_reserva = Reserva(cliente, habitacion_a_reservar, fecha_inicio, fecha_fin)
        self.reservas.append(nueva_reserva)

        # Actualiza el estado de la habitación y el historial del cliente.
        habitacion_a_reservar.cambiar_estado("ocupada")
        cliente.historial_de_reservas.append(nueva_reserva)

        print("Reserva creada con éxito.")
        return nueva_reserva

    def cancelar_reserva(self, reserva):
        """
        Cancela una reserva existente.

        Args:
            reserva (Reserva): La reserva a cancelar.
        """
        reserva.estado = "cancelada"
        reserva.habitacion.cambiar_estado("disponible")
        print(f"Reserva para {reserva.cliente.nombre} en la habitación {reserva.habitacion.numero} ha sido cancelada.")

    def mostrar_reservas_activas(self):
        """
        Muestra todas las reservas que están actualmente activas.
        """
        reservas_activas = [r for r in self.reservas if r.estado == "activa"]
        if not reservas_activas:
            print("No hay reservas activas en este momento.")
        else:
            print("\n--- Reservas Activas ---")
            for reserva in reservas_activas:
                print(reserva)