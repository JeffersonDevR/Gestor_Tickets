# -*- coding: utf-8 -*-
# Importamos los módulos necesarios para la aplicación.
import datetime
from Modulos.Clientes import Cliente
from Modulos.Habitaciones import GestorHabitaciones
from Modulos.Reservas import GestorReservas
from Modulos.Pagos import GestorDePagos, PagoEnEfectivo, PagoConTarjeta

class HotelApp:
    """
    Clase principal que orquesta la aplicación de gestión del hotel.
    """
    def __init__(self):
        """
        Inicializa la aplicación, creando instancias de los gestores.
        """
        self.gestor_habitaciones = GestorHabitaciones()
        self.gestor_reservas = GestorReservas(self.gestor_habitaciones)
        self.gestor_pagos = GestorDePagos()
        self._pre_cargar_datos()

    def _pre_cargar_datos(self):
        """
        Precarga datos iniciales para demostración, como habitaciones y un usuario administrador.
        """
        # Precargar algunas habitaciones para demostración.
        self.gestor_habitaciones.agregar_habitacion("101", "Sencilla", 150.0)
        self.gestor_habitaciones.agregar_habitacion("102", "Doble", 250.0)
        self.gestor_habitaciones.agregar_habitacion("201", "Suite", 500.0)
        # Precargar un cliente administrador.
        Cliente.registrar_cliente("Admin", "0", "admin@hotel.com", "0")

    def menu_admin(self):
        """
        Muestra y gestiona el menú para el administrador.
        """
        while True:
            print("\n--- Panel de Administración ---")
            print("1. Gestionar Clientes")
            print("2. Gestionar Habitaciones")
            print("3. Ver Reservas Activas")
            print("4. Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.gestionar_clientes_admin()
            elif opcion == "2":
                self.gestionar_habitaciones_admin()
            elif opcion == "3":
                self.gestor_reservas.mostrar_reservas_activas()
            elif opcion == "4":
                break
            else:
                print("Opción no válida.")

    def gestionar_clientes_admin(self):
        """
        Submenú para la gestión de clientes por parte del administrador.
        """
        while True:
            print("\n--- Gestión de Clientes ---")
            print("1. Ver todos los clientes")
            print("2. Actualizar cliente")
            print("3. Volver al panel de administración")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                for cliente in Cliente.clientes_registrados:
                    print(cliente)
            elif opcion == "2":
                doc = input("Ingrese el N° de identificación del cliente a actualizar: ")
                nombre = input("Nuevo nombre (o presione Enter para omitir): ")
                correo = input("Nuevo correo (o presione Enter para omitir): ")
                telefono = input("Nuevo teléfono (o presione Enter para omitir): ")
                Cliente.actualizar_info_cliente(doc, nombre or None, correo or None, telefono or None)
            elif opcion == "3":
                break
            else:
                print("Opción no válida.")

    def gestionar_habitaciones_admin(self):
        """
        Submenú para la gestión de habitaciones por parte del administrador.
        """
        while True:
            print("\n--- Gestión de Habitaciones ---")
            print("1. Ver todas las habitaciones")
            print("2. Agregar habitación")
            print("3. Cambiar estado de una habitación")
            print("4. Volver al panel de administración")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.gestor_habitaciones.mostrar_todas()
            elif opcion == "2":
                num = input("Número de habitación: ")
                tipo = input("Tipo: ")
                tarifa = float(input("Tarifa: "))
                self.gestor_habitaciones.agregar_habitacion(num, tipo, tarifa)
            elif opcion == "3":
                num = input("Número de habitación a modificar: ")
                nuevo_estado = input("Nuevo estado (disponible, ocupada, mantenimiento): ")
                hab = next((h for h in self.gestor_habitaciones.habitaciones if h.numero == num), None)
                if hab:
                    hab.cambiar_estado(nuevo_estado)
                else:
                    print("Habitación no encontrada.")
            elif opcion == "4":
                break
            else:
                print("Opción no válida.")

    def menu_cliente(self):
        """
        Muestra y gestiona el menú para los clientes.
        """
        print("\n--- Portal de Clientes ---")
        identificacion = input("Ingrese su número de identificación para iniciar sesión: ")
        cliente_actual = next((c for c in Cliente.clientes_registrados if c.n_identificacion == identificacion), None)

        if not cliente_actual:
            print("No se encontró el cliente. ¿Desea registrarse? (s/n)")
            if input().lower() == 's':
                cliente_actual = self.registrar_nuevo_cliente()
                if not cliente_actual:
                    return  # No se pudo registrar, volver al menú principal
            else:
                return

        while True:
            print(f"\nBienvenido, {cliente_actual.nombre}")
            print("1. Ver mis datos")
            print("2. Ver mis reservas")
            print("3. Crear una nueva reserva")
            print("4. Realizar un pago")
            print("5. Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(cliente_actual)
            elif opcion == "2":
                cliente_actual.mostrar_reservas()
            elif opcion == "3":
                self.crear_reserva_cliente(cliente_actual)
            elif opcion == "4":
                self.realizar_pago_cliente()
            elif opcion == "5":
                break
            else:
                print("Opción no válida.")

    def registrar_nuevo_cliente(self):
        """
        Permite a un nuevo usuario registrarse como cliente.
        """
        print("\n--- Registro de Nuevo Cliente ---")
        nombre = input("Nombre completo: ")
        doc = input("Número de identificación: ")
        correo = input("Correo electrónico: ")
        tel = input("Teléfono: ")
        return Cliente.registrar_cliente(nombre, doc, correo, tel)

    def crear_reserva_cliente(self, cliente):
        """
        Permite a un cliente crear una nueva reserva.
        """
        print("\n--- Crear Nueva Reserva ---")
        self.gestor_habitaciones.mostrar_todas()
        num_hab = input("Seleccione el número de la habitación que desea reservar: ")

        try:
            f_inicio_str = input("Fecha de inicio (YYYY-MM-DD): ")
            f_fin_str = input("Fecha de fin (YYYY-MM-DD): ")
            f_inicio = datetime.datetime.strptime(f_inicio_str, "%Y-%m-%d")
            f_fin = datetime.datetime.strptime(f_fin_str, "%Y-%m-%d")
        except ValueError:
            print("Formato de fecha inválido.")
            return

        self.gestor_reservas.crear_reserva(cliente, num_hab, f_inicio, f_fin)

    def realizar_pago_cliente(self):
        """
        Permite a un cliente realizar un pago.
        """
        print("\n--- Realizar un Pago ---")
        monto = float(input("Monto a pagar: "))
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

    def run(self):
        """
        Inicia la ejecución del bucle principal de la aplicación.
        """
        while True:
            print("\n====== Bienvenido al Sistema de Gestión Hotelera ======")
            print("1. Soy Administrador")
            print("2. Soy Cliente")
            print("3. Salir")
            opcion_main = input("Seleccione su rol: ")

            if opcion_main == "1":
                self.menu_admin()
            elif opcion_main == "2":
                self.menu_cliente()
            elif opcion_main == "3":
                print("Gracias por usar nuestro sistema. ¡Hasta pronto!")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    # Punto de entrada de la aplicación.
    app = HotelApp()
    app.run()