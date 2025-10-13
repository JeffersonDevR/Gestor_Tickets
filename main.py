from Modulos.Pagos import menu as menu_pagos
from Modulos.Clientes import menu as menu_clientes, Cliente
from Modulos.Habitaciones import menu as menu_habitaciones
from Modulos.Reservas import menu_reservas

# Admin credentials (hardcoded)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def seleccionar_cliente():
    """Función para seleccionar o registrar un cliente antes de proceder"""
    while True:
        print("====== SELECCIÓN DE CLIENTE ======")
        print("Para continuar, debe seleccionar un cliente existente o registrar uno nuevo.")
        print("1. Seleccionar cliente existente")
        print("2. Registrar nuevo cliente")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if not Cliente.clientes_registrados:
                print("No hay clientes registrados. Registre uno nuevo primero.")
                continue
            print("Clientes registrados:")
            for i, cliente in enumerate(Cliente.clientes_registrados, 1):
                print(f"{i}. {cliente.nombre}")
            try:
                indice = int(input("Seleccione el número del cliente: ")) - 1
                if 0 <= indice < len(Cliente.clientes_registrados):
                    cliente_seleccionado = Cliente.clientes_registrados[indice]
                    print(f"Cliente seleccionado: {cliente_seleccionado.nombre}")
                    return cliente_seleccionado
                else:
                    print("Selección inválida.")
            except ValueError:
                print("Entrada inválida.")

        elif opcion == "2":
            print("Ingrese los datos del nuevo cliente:")
            nombre = input("Nombre completo: ")
            n_identificacion = int(input("Número de identificación: "))
            correo = input("Correo electrónico: ")
            n_telefono = int(input("Número de teléfono: "))
            cliente_nuevo = Cliente.registrar_cliente(nombre, n_identificacion, correo, n_telefono)
            if cliente_nuevo:
                print(f"Cliente registrado y seleccionado: {cliente_nuevo.nombre}")
                return cliente_nuevo

        elif opcion == "3":
            print("Saliendo del sistema...")
            return None

        else:
            print("Opción no válida.")


def main_menu(cliente_actual):
    while True:
        print(f"\n====== GESTOR DE TICKETS PARA HOTEL ======")
        print(f"Cliente actual: {cliente_actual.nombre}")
        print("1. Gestión de Clientes")
        print("2. Gestión de Habitaciones")
        print("3. Gestión de Reservas")
        print("4. Gestión de Pagos")
        print("5. Cambiar cliente")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_habitaciones()
        elif opcion == "3":
            if not Cliente.clientes_registrados:
                print("Debe registrar un cliente antes de hacer reservas.")
            else:
                menu_reservas()
        elif opcion == "4":
            if not Cliente.clientes_registrados:
                print("Debe registrar un cliente antes de procesar pagos.")
            else:
                menu_pagos()
        elif opcion == "5":
            cliente_actual = seleccionar_cliente()
            if cliente_actual is None:
                break
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    print("Bienvenido al Sistema de Gestión de Tickets para Hotel")
    cliente = seleccionar_cliente()
    if cliente:
        main_menu(cliente)
    else:
        print("Sistema cerrado.")
