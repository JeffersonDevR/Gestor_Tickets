# Lista inicial de habitaciones disponibles(temporal)
habitaciones_disponibles = ["001", "002", "003", "004", "005"]

class Reservas:
    def __init__(self):
        # Aquí se guardan todas las reservas en formato de diccionario
        self.lista_reservas = []

    # 1. Crear reservas 
    def crear_reserva(self, cliente, habitacion, fecha, hora):
        if habitacion in habitaciones_disponibles:
            reserva = {
                "cliente": cliente,
                "habitacion": habitacion,
                "fecha": fecha,
                "hora": hora
            }
            self.lista_reservas.append(reserva)
            habitaciones_disponibles.remove(habitacion)  # quitar la habitación de disponibles
            print(f"Reserva creada: {cliente} en habitación {habitacion} el {fecha} a las {hora}.")
        else:
            print("Habitación no disponible.")

    # 2. MODIFICAR RESERVA
    def modificar_reserva(self, cliente, nueva_habitacion, nueva_fecha, nueva_hora):
        for reserva in self.lista_reservas:
            if reserva["cliente"] == cliente:
                # liberar la habitación anterior
                habitaciones_disponibles.append(reserva["habitacion"])

                # asignar la nueva
                if nueva_habitacion in habitaciones_disponibles:
                    reserva["habitacion"] = nueva_habitacion
                    reserva["fecha"] = nueva_fecha
                    reserva["hora"] = nueva_hora
                    habitaciones_disponibles.remove(nueva_habitacion)
                    print(f"Reserva modificada para {cliente}.")
                else:
                    print("Nueva habitación no disponible.")
                return
        print("No se encontró la reserva del cliente.")

    # 3. CANCELAR RESERVA
    def cancelar_reserva(self, cliente):
        for reserva in self.lista_reservas:
            if reserva["cliente"] == cliente:
                habitaciones_disponibles.append(reserva["habitacion"])  # liberar la habitación
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
                   
                       