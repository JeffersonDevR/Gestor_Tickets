from Modulos.Habitaciones import GestorHabitaciones, Habitacion
class Reserva:
    def __init__(self, cliente, habitacion, fecha, hora):
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha = fecha
        self.hora = hora

    def __str__(self):
        return (f"Cliente: {self.cliente.nombre} | Identificación: {self.cliente.n_identificacion}  "
                f"Habitación: {self.habitacion.numero} | "
                f"Fecha: {self.fecha} | Hora: {self.hora}")


class GestorReservas:
    def __init__(self, gestor_habitaciones):
        self.lista_reservas = []
        self.gestor_habitaciones = GestorHabitaciones()

    def crear_reserva(self, cliente, numero_habitacion, fecha, hora):
        habitacion = next(
            (h for h in self.gestor_habitaciones.habitaciones if h.numero == numero_habitacion),
            None
        )

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
            print("\nLista de reservas:")
            for r in self.lista_reservas:
                print(f"- Cliente: {r['cliente']}, Habitación: {r['habitacion']}, Fecha: {r['fecha']}, Hora: {r['hora']}")

def menu():
    sistema = Reservas()  # Crear el objeto del sistema de reservas

    while True:
        print("=== Sistema de Gestión de Reservas ===")
        print("1. Crear reserva")
        print("2. Modificar reserva")
        print("3. Cancelar reserva")
        print("4. Mostrar todas las reservas")
        print("5. Mostrar habitaciones disponibles")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cliente = input("Nombre del cliente: ")
            print("Las habitaciones disponibles son : ", habitaciones_disponibles)
            habitacion = input("Número de habitación: ")
            fecha = input("Fecha (dd/mm/aaaa): ")
            hora = input("Hora: ")
            sistema.crear_reserva(cliente, habitacion, fecha, hora)

        elif opcion == "2":
            cliente = input("Nombre del cliente: ")
            print("Las habitaciones disponibles son : ", habitaciones_disponibles)
            nueva_habitacion = input("Nueva habitación: ")
            nueva_fecha = input("Nueva fecha (dd/mm/aaaa): ")
            nueva_hora = input("Nueva hora: ")
            sistema.modificar_reserva(cliente, nueva_habitacion, nueva_fecha, nueva_hora)

        elif opcion == "3":
            cliente = input("Nombre del cliente: ")
            sistema.cancelar_reserva(cliente)

        elif opcion == "4":
            sistema.mostrar_reservas()

        elif opcion == "5":
            print("Habitaciones disponibles:", habitaciones_disponibles)

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

        print()

# Ejecutar el menú
if __name__=="__main__":
    menu()