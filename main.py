import asyncio
from Modulos.Clientes import Cliente
from Modulos.Habitaciones import GestorHabitaciones, Habitacion
from Modulos.Reservas import Reservas, habitaciones_disponibles
from Modulos.Pagos import GestorDePagos, PagoEnEfectivo, PagoConTarjeta

class HotelApp:
    def __init__(self):
        self.gestor_habitaciones = GestorHabitaciones()
        self.reservas = Reservas()
        self.gestor_pagos = GestorDePagos()
        self._pre_cargar_datos()

    def _pre_cargar_datos(self):
        if not self.gestor_habitaciones.habitaciones:
            self.gestor_habitaciones.habitaciones.append(Habitacion("101", "Sencilla", 150.0))
            self.gestor_habitaciones.habitaciones.append(Habitacion("102", "Doble", 250.0))
            self.gestor_habitaciones.habitaciones.append(Habitacion("201", "Suite", 500.0))
            habitaciones_disponibles.extend(["101", "102", "201"])

        if not any(c.n_identificacion == 0 for c in Cliente.clientes_registrados):
             Cliente.registrar_cliente("Admin", 0, "admin@hotel.com", "0")

    async def menu_principal(self):
        while True:
            print("\n====== Menú Principal del Hotel ======")
            print("1. Entrar como Administrador")
            print("2. Entrar como Cliente")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                await self.menu_admin()
            elif opcion == "2":
                await self.menu_cliente_inicial()
            elif opcion == "3":
                print("Gracias por usar el sistema. ¡Adiós!")
                break
            else:
                print("Opción no válida.")

    async def menu_admin(self):
        while True:
            print("\n--- Panel de Administración ---")
            print("1. Gestionar Clientes")
            print("2. Gestionar Habitaciones")
            print("3. Gestionar Reservas")
            print("4. Gestionar Pagos")
            print("5. Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.admin_gestionar_clientes()
            elif opcion == "2":
                self.admin_gestionar_habitaciones()
            elif opcion == "3":
                self.admin_gestionar_reservas()
            elif opcion == "4":
                await self.admin_gestionar_pagos()
            elif opcion == "5":
                break
            else:
                print("Opción no válida.")

    def admin_gestionar_clientes(self):
        print("\n--- Gestión de Clientes (Admin) ---")
        print("1. Ver todos los clientes")
        print("2. Actualizar cliente")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            for cliente in Cliente.clientes_registrados:
                print(cliente)
        elif opcion == '2':
            nombre_cliente = input("Ingrese el nombre del cliente que desea buscar para actualizar: ")
            Cliente.actualizar_info_clientes(nombre_cliente)

    def admin_gestionar_habitaciones(self):
        while True:
            print("\n--- Gestión de Habitaciones (Admin) ---")
            print("1. Ver todas las habitaciones")
            print("2. Agregar nueva habitación")
            print("3. Cambiar estado de una habitación")
            print("4. Volver al panel de administración")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.gestor_habitaciones.mostrar_todas()
            elif opcion == "2":
                self.gestor_habitaciones.agregar_habitacion()
            elif opcion == "3":
                self.gestor_habitaciones.cambiar_estado()
            elif opcion == "4":
                break
            else:
                print("Opción no válida.")

    def admin_gestionar_reservas(self):
        while True:
            print("\n--- Gestión de Reservas (Admin) ---")
            print("1. Ver todas las reservas")
            print("2. Crear nueva reserva para un cliente")
            print("3. Volver al panel de administración")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.reservas.mostrar_reservas()
            elif opcion == "2":
                self.admin_crear_reserva()
            elif opcion == "3":
                break
            else:
                print("Opción no válida.")

    def admin_crear_reserva(self):
        print("\n--- Creando Nueva Reserva (Admin) ---")
        try:
            id_cliente = int(input("Ingrese el N° de identificación del cliente: "))
            cliente = next((c for c in Cliente.clientes_registrados if c.n_identificacion == id_cliente), None)
            if not cliente:
                print("Cliente no encontrado.")
                return
            #apuntar a gestor de habitaciones
            print("Habitaciones disponibles:", habitaciones_disponibles)
            num_hab = input("Seleccione el número de la habitación: ")
            fecha = input("Fecha (dd/mm/aaaa): ")
            hora = input("Hora: ")
            self.reservas.crear_reserva((f"Cliente:{cliente.n_identificacion}",f"Documento:{cliente.n_identificacion}"), num_hab, fecha, hora)
        except ValueError:
            print("El N° de identificación debe ser un número.")

    async def admin_gestionar_pagos(self):
        while True:
            print("\n--- Gestión de Pagos (Admin) ---")
            print("1. Procesar un nuevo pago")
            print("2. Volver al panel de administración")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                try:
                    monto = float(input("Ingrese el monto a pagar: "))
                    await self.realizar_pago(monto)
                except ValueError:
                    print("Monto inválido.")
            elif opcion == "2":
                break
            else:
                print("Opción no válida.")

    async def menu_cliente_inicial(self):
        print("\n--- Portal de Clientes ---")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            await self.login_cliente()
        elif opcion == "2":
            self.registrar_nuevo_cliente()
        else:
            print("Opción no válida.")

    async def login_cliente(self):
        try:
            identificacion = int(input("Ingrese su número de identificación: "))
            cliente_actual = next((c for c in Cliente.clientes_registrados if c.n_identificacion == identificacion), None)
            if cliente_actual:
                await self.menu_cliente_logueado(cliente_actual)
            else:
                print("Cliente no encontrado.")
        except ValueError:
            print("Identificación inválida. Debe ser un número.")

    

    def registrar_nuevo_cliente(self):
        print("\n--- Registro de Nuevo Cliente ---")

        while True:
            nombre = input("Nombre completo: ")
            # Usamos all() para permitir espacios entre nombres
            if all(ch.isalpha() or ch.isspace() for ch in nombre) and nombre.strip():
                break
            else:
                print("El nombre solo debe contener letras y espacios.")

        
        while True:
            doc = input("Número de identificación: ")
            if doc.isdigit():
                doc = int(doc)
                break
            else:
                print("El número de identificación debe ser numérico.")

        
        while True:
            correo = input("Correo electrónico: ")
            if "@" in correo and (correo.endswith(".com") or correo.endswith(".co") or correo.endswith(".org")):
                break
            else:
                print("El correo debe contener '@' y terminar en '.com', '.co' o '.org'.")

    
        while True:
            tel = input("Teléfono: ")
            if tel.isdigit():
                tel = int(tel)
                break
            else:
                print("El teléfono debe contener solo números.")
        for c in Cliente.clientes_registrados:
            print(c)
        nuevo_cliente = Cliente.registrar_cliente(nombre, doc, correo, tel)
        if nuevo_cliente:
            print("Registro exitoso. Ahora puede iniciar sesión.")

    async def menu_cliente_logueado(self, cliente):
        while True:
            print(f"\n--- Bienvenido, {cliente.n_identificacion} ---")
            print("1. Ver mis datos")
            print("2. Actualizar datos")
            print("3. Crear una reserva")
            print("4. Ver mis reservas")
            print("5. Pagar reservación")
            print("6. Cerrar sesión")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(cliente)
            elif opcion == "2":
                Cliente.actualizar_info_clientes(cliente.n_identificacion)
            elif opcion == "3":
                await self.crear_reserva_cliente(cliente)
            elif opcion == "4":
                self.ver_reservas_cliente(cliente)
            elif opcion == "5":
                await self.pagar_reservacion_cliente(cliente)
            elif opcion == "6":
                break
            else:
                print("Opción no válida.")

    async def crear_reserva_cliente(self, cliente):
        print("\n--- Crear Nueva Reserva ---")
        print("Habitaciones disponibles:", [h.numero for h in self.gestor_habitaciones.habitaciones])
        num_hab = input("Seleccione el número de la habitación: ")
        # Lógica para encontrar la habitación y su tarifa
        habitacion_seleccionada = next((h for h in self.gestor_habitaciones.habitaciones if h.numero == num_hab), None)
        if not habitacion_seleccionada:
            print("Número de habitación no válido.")
            return

        fecha = input("Fecha (dd/mm/aaaa): ")
        hora = input("Hora: ")
        self.reservas.crear_reserva(cliente.n_identificacion, num_hab, fecha, hora)

        # Preguntar si desea pagar ahora
        desea_pagar = input("¿Desea pagar la reserva ahora? (s/n): ").lower()
        if desea_pagar == 's':
            await self.realizar_pago(habitacion_seleccionada.tarifa)


    def ver_reservas_cliente(self, cliente):
        reservas_cliente = [r for r in self.reservas.lista_reservas if r['cliente'] == cliente.n_identificacion]
        if not reservas_cliente:
            print("No tiene reservas activas.")
            return
        print("\n--- Sus Reservas ---")
        for i, reserva in enumerate(reservas_cliente):
            print(f"{i+1}. Habitación: {reserva['habitacion']}, Fecha: {reserva['fecha']}, Hora: {reserva['hora']}")

    async def pagar_reservacion_cliente(self, cliente):
        #Se tiene que agregar o implementar pago por el historial_de_reservas
        # self.historial_de_reservas = []
        reservas_cliente = [r for r in cliente.historial_de_reservas if r['cliente'] == cliente.n_identificacion]
        if not reservas_cliente:
            print("No tiene reservas para pagar.")
            return

        print("\n--- Seleccione la Reservación a Pagar ---")
        for i, reserva in enumerate(reservas_cliente):
            hab = next((h for h in self.gestor_habitaciones.habitaciones if h.numero == reserva['habitacion']), None)
            tarifa = hab.tarifa if hab else "N/A"
            print(f"{i+1}. Habitación: {reserva['habitacion']}, Tarifa: ${tarifa}")

        try:
            opcion = int(input("Seleccione una reservación: ")) - 1
            if not 0 <= opcion < len(reservas_cliente):
                print("Selección inválida.")
                return

            reserva_a_pagar = reservas_cliente[opcion]
            habitacion_a_pagar = next((h for h in self.gestor_habitaciones.habitaciones if h.numero == reserva_a_pagar['habitacion']), None)

            if not habitacion_a_pagar:
                print("Error: La habitación de la reserva no fue encontrada.")
                return

            await self.realizar_pago(habitacion_a_pagar.tarifa)

        except (ValueError, IndexError):
            print("Entrada inválida.")

    async def realizar_pago(self, monto):
        print(f"El monto a pagar es de: ${monto}")
        tipo_pago = input("Método de pago (efectivo/tarjeta): ").lower()

        if tipo_pago == "efectivo":
            pago = PagoEnEfectivo(monto=monto)
            await self.gestor_pagos.realizar_pago(pago)
        elif tipo_pago == "tarjeta":
            num_tarjeta = input("Número de tarjeta (16 dígitos): ")
            cvv = input("CVV (3 dígitos): ")
            try:
                pago = PagoConTarjeta(monto=monto, numero_tarjeta=num_tarjeta, cvv=cvv)
                await self.gestor_pagos.realizar_pago(pago)
            except ValueError as e:
                print(f"Error en los datos de la tarjeta: {e}")
        else:
            print("Método de pago no válido.")

async def main():
    app = HotelApp()
    await app.menu_principal()

if __name__ == "__main__":
    asyncio.run(main())