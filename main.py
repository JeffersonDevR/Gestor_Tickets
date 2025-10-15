# -*- coding: utf-8 -*-
import subprocess
from Modulos.Pagos import GestorDePagos, PagoEnEfectivo, PagoConTarjeta

class AdminApp:
    def __init__(self):
        """
        Inicializa la aplicación de administración.
        Solo el gestor de pagos se maneja directamente aquí, ya que fue refactorizado.
        Los otros módulos se ejecutarán como procesos separados.
        """
        self.gestor_pagos = GestorDePagos()
        self._pre_cargar_datos()

    def _pre_cargar_datos(self):
        """
        Precarga datos iniciales para demostración.
        Esto es un truco para añadir datos sin modificar los módulos originales.
        """
        from Modulos.Habitaciones import GestorHabitaciones, Habitacion
        gestor_habitaciones = GestorHabitaciones()
        if not gestor_habitaciones.habitaciones: # Solo si no hay habitaciones
            gestor_habitaciones.habitaciones.append(Habitacion("101", "Sencilla", 150.0))
            gestor_habitaciones.habitaciones.append(Habitacion("102", "Doble", 250.0))
            gestor_habitaciones.habitaciones.append(Habitacion("201", "Suite", 500.0))
            print("Datos de habitaciones pre-cargados para demostración.")

    def run(self):
        """
        Ejecuta el bucle principal del panel de administración.
        """
        while True:
            print("\n--- Panel de Administración ---")
            print("1. Gestionar Clientes (Lanza módulo interactivo)")
            print("2. Gestionar Habitaciones (Lanza módulo interactivo)")
            print("3. Gestionar Reservas (Lanza módulo interactivo)")
            print("4. Realizar un Pago")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.gestionar_clientes()
            elif opcion == "2":
                self.gestionar_habitaciones()
            elif opcion == "3":
                self.gestionar_reservas()
            elif opcion == "4":
                self.realizar_pago()
            elif opcion == "5":
                print("Saliendo del panel de administración.")
                break
            else:
                print("Opción no válida.")

    def _ejecutar_modulo(self, nombre_modulo):
        """
        Ejecuta un módulo interactivo como un subproceso.
        """
        ruta_modulo = f"Modulos/{nombre_modulo}.py"
        print(f"\n--- Lanzando el Módulo de {nombre_modulo} ---")
        print(f"Interactúe con el módulo. Cuando elija la opción de salir en ese módulo, el control volverá aquí.")
        try:
            # Usamos subprocess.run para ejecutar el script del módulo.
            # El control se detiene aquí hasta que el subproceso termine.
            subprocess.run(["python", ruta_modulo], check=True)
        except FileNotFoundError:
            print(f"Error: No se encontró el script '{ruta_modulo}'.")
        except subprocess.CalledProcessError as e:
            print(f"El script de {nombre_modulo} terminó con un error: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado al lanzar el módulo: {e}")
        print(f"\n--- Ha vuelto al Panel de Administración ---")

    def gestionar_clientes(self):
        self._ejecutar_modulo("Clientes")

    def gestionar_habitaciones(self):
        self._ejecutar_modulo("Habitaciones")

    def gestionar_reservas(self):
        self._ejecutar_modulo("Reservas")

    def realizar_pago(self):
        """
        Gestiona la creación de un nuevo pago.
        """
        print("\n--- Realizar un Pago ---")
        try:
            monto = float(input("Monto a pagar: "))
            tipo_pago = input("Método de pago (efectivo/tarjeta): ").lower()

            if tipo_pago == "efectivo":
                pago = PagoEnEfectivo(monto=monto)
                self.gestor_pagos.realizar_pago(pago)
            elif tipo_pago == "tarjeta":
                num_tarjeta = input("Número de tarjeta (16 dígitos): ")
                cvv = input("CVV (3 dígitos): ")
                pago = PagoConTarjeta(monto=monto, numero_tarjeta=num_tarjeta, cvv=cvv)
                self.gestor_pagos.realizar_pago(pago)
            else:
                print("Método de pago no válido.")
        except ValueError as e:
            print(f"Error en los datos del pago: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    app = AdminApp()
    app.run()