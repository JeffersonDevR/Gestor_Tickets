from Habitaciones import GestorHabitaciones, Habitacion
class Reserva:
    def __init__(self, cliente, habitacion, fecha, hora):
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha = fecha
        self.hora = hora

    def __str__(self):
        return (f"Cliente: {self.cliente} | "
                f"Habitación: {self.habitacion.numero} | "
                f"Fecha: {self.fecha} | Hora: {self.hora}")


class GestorReservas:
    def __init__(self, gestor_habitaciones):
        self.lista_reservas = []
        self.gestor_habitaciones = gestor_habitaciones

    def crear_reserva(self, cliente, numero_habitacion, fecha, hora):
        habitacion = self.gestor_habitaciones.buscar_habitacion(numero_habitacion)

        if habitacion is None:
            print("No existe una habitación con ese número.")
            return

        if habitacion.estado != "disponible":
            print("La habitación seleccionada no está disponible.")
            return

        nueva_reserva = Reserva(cliente, habitacion, fecha, hora)
        self.lista_reservas.append(nueva_reserva)
        habitacion.cambiar_estado("ocupada")
        print(f"Reserva creada correctamente para {cliente} en la habitación {numero_habitacion}.")

    def cancelar_reserva(self, numero_habitacion):
        for reserva in self.lista_reservas:
            if reserva.habitacion.numero == numero_habitacion:
                self.lista_reservas.remove(reserva)
                reserva.habitacion.cambiar_estado("disponible")
                print(f"Reserva de la habitación {numero_habitacion} ha sido cancelada.")
                return
        print("No se encontró una reserva con ese número de habitación.")

    def modificar_reserva(self, numero_habitacion, nuevo_cliente=None, nueva_fecha=None, nueva_hora=None, nueva_habitacion_numero=None):
        for reserva in self.lista_reservas:
            if reserva.habitacion.numero == numero_habitacion:
                print(f"Reserva encontrada: {reserva}")

                if nuevo_cliente:
                    reserva.cliente = nuevo_cliente
                if nueva_fecha:
                    reserva.fecha = nueva_fecha
                if nueva_hora:
                    reserva.hora = nueva_hora

                if nueva_habitacion_numero:
                    habitacion_nueva = self.gestor_habitaciones.buscar_habitacion(nueva_habitacion_numero)
                    if habitacion_nueva is None:
                        print("No existe una habitación con ese número.")
                        return
                    if habitacion_nueva.estado != "disponible":
                        print("La nueva habitación no está disponible.")
                        return

                    reserva.habitacion.cambiar_estado("disponible")
                    reserva.habitacion = habitacion_nueva
                    habitacion_nueva.cambiar_estado("ocupada")

                print("Reserva modificada correctamente.")
                return

        print("No se encontró una reserva con ese número de habitación.")

    def mostrar_reservas(self):
        if not self.lista_reservas:
            print("No hay reservas registradas.")
        else:
            print("\n=== LISTA DE RESERVAS ===")
            for reserva in self.lista_reservas:
                print(reserva)
