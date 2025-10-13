class Habitacion:
    def __init__(self, numero, tipo, tarifa):
        self.numero = numero
        self.tipo = tipo
        self.tarifa = float(tarifa)
        self.estado = "disponible"

    def mostrar_info(self):
        print(f"Habitación {self.numero} | Tipo: {self.tipo} | Tarifa: ${self.tarifa:.2f} | Estado: {self.estado}")

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in ["disponible", "ocupada", "mantenimiento"]:
            self.estado = nuevo_estado
            print(f"Habitación {self.numero} ahora está '{nuevo_estado}'.")
        else:
            print("Estado no válido. Usa: disponible, ocupada o mantenimiento.")


class GestorHabitaciones:
    def __init__(self):
        self.habitaciones = []
        # Agregar habitaciones por defecto
        self.habitaciones.append(Habitacion("001", "Sencilla", 50.0))
        self.habitaciones.append(Habitacion("002", "Doble", 80.0))
        self.habitaciones.append(Habitacion("003", "Suite", 150.0))
        self.habitaciones.append(Habitacion("004", "Sencilla", 50.0))
        self.habitaciones.append(Habitacion("005", "Doble", 80.0))

    def agregar_habitacion(self):
        print("\n--- Registrar nueva habitación ---")
        numero = input("Ingrese el número de habitación: ")
        tipo = input("Ingrese el tipo (Sencilla, Doble, Suite, etc.): ")
        tarifa = input("Ingrese la tarifa por noche: ")

        nueva = Habitacion(numero, tipo, tarifa)
        self.habitaciones.append(nueva)
        print(f"Habitación {numero} registrada correctamente.\n")

    def mostrar_todas(self):
        print("\n--- Listado de habitaciones ---")
        if not self.habitaciones:
            print("No hay habitaciones registradas.")
        else:
            for hab in self.habitaciones:
                hab.mostrar_info()
        print()

    def cambiar_estado(self):
        print("\n--- Cambiar estado de habitación ---")
        numero = input("Ingrese el número de habitación: ")
        for hab in self.habitaciones:
            if hab.numero == numero:
                print(f"Estado actual: {hab.estado}")
                nuevo = input("Nuevo estado (disponible / ocupada / mantenimiento): ").lower()
                hab.cambiar_estado(nuevo)
                return
        print("No se encontró esa habitación.\n")

    def buscar_por_estado(self):
        print("\n--- Buscar habitaciones por estado ---")
        estado = input("Ingrese el estado (disponible / ocupada / mantenimiento): ").lower()
        filtradas = [h for h in self.habitaciones if h.estado == estado]

        if filtradas:
            print(f"\nHabitaciones con estado '{estado}':")
            for h in filtradas:
                h.mostrar_info()
        else:
            print("No hay habitaciones con ese estado.")
        print()

    def buscar_por_tipo(self):
        print("\n--- Buscar habitaciones por tipo ---")
        tipo = input("Ingrese el tipo (Sencilla / Doble / Suite, etc.): ")
        filtradas = [h for h in self.habitaciones if h.tipo.lower() == tipo.lower()]

        if filtradas:
            print(f"\nHabitaciones tipo '{tipo}':")
            for h in filtradas:
                h.mostrar_info()
        else:
            print("No hay habitaciones de ese tipo.")
        print()

    def ordenar_por_tarifa(self):
        print("\n--- Clasificación por tarifa ---")
        if not self.habitaciones:
            print("No hay habitaciones registradas.")
        else:
            ordenadas = sorted(self.habitaciones, key=lambda x: x.tarifa)
            for h in ordenadas:
                h.mostrar_info()
        print()

    def get_habitaciones_disponibles(self):
        return [h.numero for h in self.habitaciones if h.estado == "disponible"]

    def ocupar_habitacion(self, numero):
        for h in self.habitaciones:
            if h.numero == numero and h.estado == "disponible":
                h.cambiar_estado("ocupada")
                return True
        return False

    def liberar_habitacion(self, numero):
        for h in self.habitaciones:
            if h.numero == numero and h.estado == "ocupada":
                h.cambiar_estado("disponible")
                return True
        return False


def menu():
    gestor = GestorHabitaciones()
    opcion = ""

    while opcion != "7":
        print("====== SISTEMA DE GESTIÓN DE HABITACIONES ======")
        print("1. Registrar habitación")
        print("2. Mostrar todas las habitaciones")
        print("3. Cambiar estado de habitación (disponibilidad en tiempo real)")
        print("4. Buscar habitaciones por estado")
        print("5. Buscar habitaciones por tipo")
        print("6. Clasificar habitaciones por tarifa")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestor.agregar_habitacion()
        elif opcion == "2":
            gestor.mostrar_todas()
        elif opcion == "3":
            gestor.cambiar_estado()
        elif opcion == "4":
            gestor.buscar_por_estado()
        elif opcion == "5":
            gestor.buscar_por_tipo()
        elif opcion == "6":
            gestor.ordenar_por_tarifa()
        elif opcion == "7":
            print("Saliendo...")
        else:
            print("Opción no válida. Intente nuevamente.\n")


if __name__ == "__main__":
    menu()