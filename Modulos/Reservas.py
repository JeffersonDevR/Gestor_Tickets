# Importar el gestor de habitaciones para integración
from Modulos.Habitaciones import GestorHabitaciones

# Instancia global del gestor de habitaciones
gestor_habitaciones = GestorHabitaciones()

class Reservas:
    def __init__(self):
        # Aquí se guardan todas las reservas en formato de diccionario
        self.lista_reservas = []

    # 1. Crear reservas
    def crear_reserva(self, cliente, habitacion, fecha, hora):
        habitaciones_disponibles = gestor_habitaciones.get_habitaciones_disponibles()
        if habitacion in habitaciones_disponibles:
            reserva = {
                "cliente": cliente,
                "habitacion": habitacion,
                "fecha": fecha,
                "hora": hora
            }
            self.lista_reservas.append(reserva)
            gestor_habitaciones.ocupar_habitacion(habitacion)  # ocupar la habitación
            print(f"Reserva creada: {cliente} en habitación {habitacion} el {fecha} a las {hora}.")
        else:
            print("Habitación no disponible.")

    # 2. MODIFICAR RESERVA
    def modificar_reserva(self, cliente, nueva_habitacion, nueva_fecha, nueva_hora):
        for reserva in self.lista_reservas:
            if reserva["cliente"] == cliente:
                # liberar la habitación anterior
                gestor_habitaciones.liberar_habitacion(reserva["habitacion"])

                # asignar la nueva
                habitaciones_disponibles = gestor_habitaciones.get_habitaciones_disponibles()
                if nueva_habitacion in habitaciones_disponibles:
                    reserva["habitacion"] = nueva_habitacion
                    reserva["fecha"] = nueva_fecha
                    reserva["hora"] = nueva_hora
                    gestor_habitaciones.ocupar_habitacion(nueva_habitacion)
                    print(f"Reserva modificada para {cliente}.")
                else:
                    print("Nueva habitación no disponible.")
                return
        print("No se encontró la reserva del cliente.")

    # 3. CANCELAR RESERVA
    def cancelar_reserva(self, cliente):
        for reserva in self.lista_reservas:
            if reserva["cliente"] == cliente:
                gestor_habitaciones.liberar_habitacion(reserva["habitacion"])  # liberar la habitación
                self.lista_reservas.remove(reserva)
                print(f"Reserva cancelada para {cliente}.")
                return
        print("No se encontró la reserva para cancelar.")

    # 4. MOSTRAR TODAS LAS RESERVAS
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
            habitaciones_disponibles = gestor_habitaciones.get_habitaciones_disponibles()
            print("Las habitaciones disponibles son : ", habitaciones_disponibles)
            habitacion = input("Número de habitación: ")
            fecha = input("Fecha (dd/mm/aaaa): ")
            hora = input("Hora: ")
            sistema.crear_reserva(cliente, habitacion, fecha, hora)

        elif opcion == "2":
            cliente = input("Nombre del cliente: ")
            habitaciones_disponibles = gestor_habitaciones.get_habitaciones_disponibles()
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
            habitaciones_disponibles = gestor_habitaciones.get_habitaciones_disponibles()
            print("Habitaciones disponibles:", habitaciones_disponibles)

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

        print()


def menu_reservas():
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
            habitaciones_disponibles = gestor_habitaciones.get_habitaciones_disponibles()
            print("Las habitaciones disponibles son : ", habitaciones_disponibles)
            habitacion = input("Número de habitación: ")
            fecha = input("Fecha (dd/mm/aaaa): ")
            hora = input("Hora: ")
            sistema.crear_reserva(cliente, habitacion, fecha, hora)

        elif opcion == "2":
            cliente = input("Nombre del cliente: ")
            habitaciones_disponibles = gestor_habitaciones.get_habitaciones_disponibles()
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
            habitaciones_disponibles = gestor_habitaciones.get_habitaciones_disponibles()
            print("Habitaciones disponibles:", habitaciones_disponibles)

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

        print()


if __name__ == "__main__":
    # Ejecutar el menú
    menu_reservas()