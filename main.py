# -*- coding: utf-8 -*-
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
            print("4. Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.admin_gestionar_clientes()
            elif opcion == "2":
                self.admin_gestionar_habitaciones()
            elif opcion == "3":
                self.admin_gestionar_reservas()
            elif opcion == "4":
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
        self.gestor_habitaciones.mostrar_todas()
        print("Para más opciones de gestión de habitaciones, el módulo original es interactivo.")

    def admin_gestionar_reservas(self):
        self.reservas.mostrar_reservas()
        print("Para más opciones de gestión de reservas, el módulo original es interactivo.")

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

    def menu_cliente_logueado(self, cliente):
        while True:
            print(f"\n--- Bienvenido, {cliente.nombre} ---")
            print("1. Ver mis datos")
            print("2. Crear una reserva")
            print("3. Ver mis reservas")
            print("4. Cerrar sesión")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(cliente)
            elif opcion == "2":
                self.crear_reserva_cliente(cliente)
            elif opcion == "3":
                cliente.mostrar_reservas_de_un_cliente()
            elif opcion == "4":
                break
            else:
                print("Opción no válida.")

    def crear_reserva_cliente(self, cliente):
        print("\n--- Crear Nueva Reserva ---")
        print("Habitaciones disponibles:", habitaciones_disponibles)
        num_hab = input("Seleccione el número de la habitación: ")
        fecha = input("Fecha (dd/mm/aaaa): ")
        hora = input("Hora: ")
        self.reservas.crear_reserva(cliente.nombre, num_hab, fecha, hora)

if __name__ == "__main__":
    app = HotelApp()
    app.menu_principal()