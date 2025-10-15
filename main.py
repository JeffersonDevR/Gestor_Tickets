<<<<<<< HEAD
from Modulos.Clientes import Cliente
from Modulos.Habitaciones import GestorHabitaciones
from Modulos.Reservas import GestorReservas
=======
# -*- coding: utf-8 -*-
from Modulos.Clientes import Cliente
from Modulos.Habitaciones import GestorHabitaciones, Habitacion
from Modulos.Reservas import Reservas, habitaciones_disponibles
>>>>>>> 25806a2 (feat: Implement main menu and refactor Pagos module)
from Modulos.Pagos import GestorDePagos, PagoEnEfectivo, PagoConTarjeta

class HotelApp:
    def __init__(self):
        self.gestor_habitaciones = GestorHabitaciones()
<<<<<<< HEAD
        self.reservas = GestorReservas(self.gestor_habitaciones)
=======
        self.reservas = Reservas()
>>>>>>> 25806a2 (feat: Implement main menu and refactor Pagos module)
        self.gestor_pagos = GestorDePagos()
        self._pre_cargar_datos()

    def _pre_cargar_datos(self):
<<<<<<< HEAD
        if not any(c.n_identificacion == 0 for c in Cliente.clientes_registrados):
             Cliente.registrar_cliente("Admin", 0, "admin@hotel.com", "0")

=======
        if not self.gestor_habitaciones.habitaciones:
            self.gestor_habitaciones.habitaciones.append(Habitacion("101", "Sencilla", 150.0))
            self.gestor_habitaciones.habitaciones.append(Habitacion("102", "Doble", 250.0))
            self.gestor_habitaciones.habitaciones.append(Habitacion("201", "Suite", 500.0))
            habitaciones_disponibles.extend(["101", "102", "201"])

        if not any(c.n_identificacion == 0 for c in Cliente.clientes_registrados):
             Cliente.registrar_cliente("Admin", 0, "admin@hotel.com", "0")

>>>>>>> 25806a2 (feat: Implement main menu and refactor Pagos module)
    def menu_principal(self):
        while True:
            print("\n====== Menú Principal del Hotel ======")
            print("1. Entrar como Administrador")
            print("2. Entrar como Cliente")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.menu_admin()
            elif opcion == "2":
                self.menu_cliente_inicial()
            elif opcion == "3":
                print("Gracias por usar el sistema. ¡Adiós!")
                break
            else:
                print("Opción no válida.")

    def menu_admin(self):
        while True:
            print("\n--- Panel de Administración ---")
            print("1. Gestionar Clientes")
            print("2. Gestionar Habitaciones")
            print("3. Gestionar Reservas")
<<<<<<< HEAD
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
                self.admin_gestionar_pagos()
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
                self.gestor_habitaciones.agregar_habitacion() # type: ignore
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

            print("Habitaciones disponibles:", )
            num_hab = input("Seleccione el número de la habitación: ")
            fecha = input("Fecha (dd/mm/aaaa): ")
            hora = input("Hora: ")
            self.reservas.crear_reserva(cliente.nombre, num_hab, fecha, hora)
        except ValueError:
            print("El N° de identificación debe ser un número.")

    def admin_gestionar_pagos(self):
        while True:
            print("\n--- Gestión de Pagos (Admin) ---")
            print("1. Procesar un nuevo pago")
            print("2. Volver al panel de administración")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                try:
                    monto = float(input("Ingrese el monto a pagar: "))
                    self.realizar_pago(monto)
                except ValueError:
                    print("Monto inválido.")
            elif opcion == "2":
=======
            print("4. Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.admin_gestionar_clientes()
            elif opcion == "2":
                self.admin_gestionar_habitaciones()
            elif opcion == "3":
                self.admin_gestionar_reservas()
            elif opcion == "4":
>>>>>>> 25806a2 (feat: Implement main menu and refactor Pagos module)
                break
            else:
                print("Opción no válida.")

<<<<<<< HEAD
=======
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
        self.gestor_habitaciones.mostrar_todas()
        print("Para más opciones de gestión de habitaciones, el módulo original es interactivo.")

    def admin_gestionar_reservas(self):
        self.reservas.mostrar_reservas()
        print("Para más opciones de gestión de reservas, el módulo original es interactivo.")

>>>>>>> 25806a2 (feat: Implement main menu and refactor Pagos module)
    def menu_cliente_inicial(self):
        print("\n--- Portal de Clientes ---")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            self.login_cliente()
        elif opcion == "2":
            self.registrar_nuevo_cliente()
        else:
            print("Opción no válida.")

    def login_cliente(self):
<<<<<<< HEAD
        try:
            identificacion = int(input("Ingrese su número de identificación: "))
            cliente_actual = next((c for c in Cliente.clientes_registrados if c.n_identificacion == identificacion), None)
            if cliente_actual:
                self.menu_cliente_logueado(cliente_actual)
            else:
                print("Cliente no encontrado.")
        except ValueError:
            print("Identificación inválida. Debe ser un número.")

    def registrar_nuevo_cliente(self):
        try:
            print("\n--- Registro de Nuevo Cliente ---")
            nombre = input("Nombre completo: ")
            doc = int(input("Número de identificación: "))
            correo = input("Correo electrónico: ")
            tel = int(input("Teléfono: "))
            nuevo_cliente = Cliente.registrar_cliente(nombre, doc, correo, tel)
            if nuevo_cliente:
                print("Registro exitoso. Ahora puede iniciar sesión.")
        except ValueError:
            print("El número de identificación y el teléfono deben ser valores numéricos.")
=======
        identificacion = int(input("Ingrese su número de identificación: "))
        cliente_actual = next((c for c in Cliente.clientes_registrados if c.n_identificacion == identificacion), None)

        if cliente_actual:
            self.menu_cliente_logueado(cliente_actual)
        else:
            print("Cliente no encontrado.")

    def registrar_nuevo_cliente(self):
        print("\n--- Registro de Nuevo Cliente ---")
        nombre = input("Nombre completo: ")
        doc = int(input("Número de identificación: "))
        correo = input("Correo electrónico: ")
        tel = int(input("Teléfono: "))
        nuevo_cliente = Cliente.registrar_cliente(nombre, doc, correo, tel)
        if nuevo_cliente:
            print("Registro exitoso. Ahora puede iniciar sesión.")
>>>>>>> 25806a2 (feat: Implement main menu and refactor Pagos module)

    def menu_cliente_logueado(self, cliente):
        while True:
            print(f"\n--- Bienvenido, {cliente.nombre} ---")
            print("1. Ver mis datos")
            print("2. Crear una reserva")
            print("3. Ver mis reservas")
<<<<<<< HEAD
            print("4. Pagar reservación")
            print("5. Cerrar sesión")
=======
            print("4. Cerrar sesión")
>>>>>>> 25806a2 (feat: Implement main menu and refactor Pagos module)
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(cliente)
            elif opcion == "2":
                self.crear_reserva_cliente(cliente)
            elif opcion == "3":
<<<<<<< HEAD
                self.ver_reservas_cliente(cliente)
            elif opcion == "4":
                self.pagar_reservacion_cliente(cliente)
            elif opcion == "5":
=======
                cliente.mostrar_reservas_de_un_cliente()
            elif opcion == "4":
>>>>>>> 25806a2 (feat: Implement main menu and refactor Pagos module)
                break
            else:
                print("Opción no válida.")

    def crear_reserva_cliente(self, cliente):
        print("\n--- Crear Nueva Reserva ---")
<<<<<<< HEAD
        print("Habitaciones disponibles:", )
=======
        print("Habitaciones disponibles:", habitaciones_disponibles)
>>>>>>> 25806a2 (feat: Implement main menu and refactor Pagos module)
        num_hab = input("Seleccione el número de la habitación: ")
        fecha = input("Fecha (dd/mm/aaaa): ")
        hora = input("Hora: ")
        self.reservas.crear_reserva(cliente.nombre, num_hab, fecha, hora)
<<<<<<< HEAD

    def ver_reservas_cliente(self, cliente):
        reservas_cliente = [r for r in self.reservas.lista_reservas if r['cliente'] == cliente.nombre]
        if not reservas_cliente:
            print("No tiene reservas activas.")
            return
        print("\n--- Sus Reservas ---")
        for i, reserva in enumerate(reservas_cliente):
            print(f"{i+1}. Habitación: {reserva['habitacion']}, Fecha: {reserva['fecha']}, Hora: {reserva['hora']}")

    def pagar_reservacion_cliente(self, cliente):
        reservas_cliente = [r for r in self.reservas.lista_reservas if r['cliente'] == cliente.nombre]
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

            self.realizar_pago(habitacion_a_pagar.tarifa)

        except (ValueError, IndexError):
            print("Entrada inválida.")

    def realizar_pago(self, monto):
        print(f"El monto a pagar es de: ${monto}")
        tipo_pago = input("Método de pago (efectivo/tarjeta): ").lower()

        if tipo_pago == "efectivo":
            pago = PagoEnEfectivo(monto=monto)
            self.gestor_pagos.realizar_pago(pago)
        elif tipo_pago == "tarjeta":
            num_tarjeta = input("Número de tarjeta (16 dígitos): ")
            cvv = input("CVV (3 dígitos): ")
            try:
                pago = PagoConTarjeta(monto=monto, numero_tarjeta=num_tarjeta, cvv=cvv)
                self.gestor_pagos.realizar_pago(pago)
            except ValueError as e:
                print(f"Error en los datos de la tarjeta: {e}")
        else:
            print("Método de pago no válido.")

if __name__ == "__main__":
    app = HotelApp()
    app.menu_principal()
=======

if __name__ == "__main__":
    app = HotelApp()
    app.menu_principal()
>>>>>>> 25806a2 (feat: Implement main menu and refactor Pagos module)
