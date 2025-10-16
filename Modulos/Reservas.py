from Habitaciones import GestorHabitaciones

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

        if not habitacion.disponible:
            print("La habitación seleccionada no está disponible.")
            return

        nueva_reserva = Reserva(cliente, habitacion, fecha, hora)
        self.lista_reservas.append(nueva_reserva)
        habitacion.cambiar_disponibilidad(False)
        print(f"Reserva creada correctamente para {cliente} en la habitación {numero_habitacion}.")

    def cancelar_reserva(self, numero_habitacion):
        for reserva in self.lista_reservas:
            if reserva.habitacion.numero == numero_habitacion:
                self.lista_reservas.remove(reserva)
                reserva.habitacion.cambiar_disponibilidad(True)
                print(f"Reserva de la habitación {numero_habitacion} ha sido cancelada.")
                return
        print("No se encontró una reserva con ese número de habitación.")

    def modificar_reserva(self, numero_habitacion):
        for reserva in self.lista_reservas:
            if reserva.habitacion.numero == numero_habitacion:
                print(f"Reserva encontrada: {reserva}")

                nuevo_cliente = input("Nuevo nombre del cliente (dejar vacío para mantener): ")
                nueva_fecha = input("Nueva fecha (dejar vacío para mantener): ")
                nueva_hora = input("Nueva hora (dejar vacío para mantener): ")
                nueva_habitacion = input("Nuevo número de habitación (dejar vacío para mantener): ")

                if nuevo_cliente:
                    reserva.cliente = nuevo_cliente
                if nueva_fecha:
                    reserva.fecha = nueva_fecha
                if nueva_hora:
                    reserva.hora = nueva_hora

                if nueva_habitacion:
                    habitacion_nueva = self.gestor_habitaciones.buscar_habitacion(nueva_habitacion)
                    if habitacion_nueva is None:
                        print("No existe una habitación con ese número.")
                        return
                    if not habitacion_nueva.disponible:
                        print("La nueva habitación no está disponible.")
                        return

                    reserva.habitacion.cambiar_disponibilidad(True)
                    reserva.habitacion = habitacion_nueva
                    habitacion_nueva.cambiar_disponibilidad(False)

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


def menu_reservas():
    gestor_habitaciones = GestorHabitaciones()
    gestor_reservas = GestorReservas(gestor_habitaciones)

    # Habitaciones de ejemplo
    gestor_habitaciones.agregar_habitacion("001", "Sencilla", 100)
    gestor_habitaciones.agregar_habitacion("002", "Doble", 180)
    gestor_habitaciones.agregar_habitacion("003", "Suite", 250)

    while True:
        print("\n=== MENÚ DE RESERVAS ===")
        print("1. Crear reserva")
        print("2. Modificar reserva")
        print("3. Cancelar reserva")
        print("4. Mostrar reservas")
        print("5. Mostrar habitaciones")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cliente = input("Nombre del cliente: ")
            numero = input("Número de habitación: ")
            fecha = input("Fecha (DD-MM-AAAA): ")
            hora = input("Hora (HH:MM): ")
            gestor_reservas.crear_reserva(cliente, numero, fecha, hora)

        elif opcion == "2":
            numero = input("Número de habitación a modificar: ")
            gestor_reservas.modificar_reserva(numero)

        elif opcion == "3":
            numero = input("Número de habitación a cancelar: ")
            gestor_reservas.cancelar_reserva(numero)

        elif opcion == "4":
            gestor_reservas.mostrar_reservas()

        elif opcion == "5":
            gestor_habitaciones.mostrar_habitaciones()

        elif opcion == "6":
            print("Saliendo del menú de reservas...")
            break

        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu_reservas()