from Modulos.Pagos import menu as menu_pagos
from Modulos.Clientes import menu as menu_clientes, Cliente
from Modulos.Habitaciones import menu as menu_habitaciones
from Modulos.Reservas import menu_reservas

# Admin credentials (hardcoded)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"


def login():
    """Function to handle login for admin or client selection"""
    while True:
        print("====== SISTEMA DE GESTIÓN DE TICKETS PARA HOTEL ======")
        print("1. Iniciar sesión como Administrador")
        print("2. Continuar como Cliente")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            username = input("Usuario: ")
            password = input("Contraseña: ")
            if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                print("Inicio de sesión exitoso como Administrador.")
                return "admin"
            else:
                print("Credenciales incorrectas.")
                continue

        elif opcion == "2":
            return "cliente"

        elif opcion == "3":
            print("Saliendo del sistema...")
            return None

        else:
            print("Opción no válida.")


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


def admin_menu():
    """Menu for admin users with full access to all modules"""
    while True:
        print("\n====== MENÚ ADMINISTRADOR ======")
        print("1. Gestión de Clientes")
        print("2. Gestión de Habitaciones")
        print("3. Gestión de Reservas")
        print("4. Gestión de Pagos")
        print("5. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_habitaciones()
        elif opcion == "3":
            menu_reservas()
        elif opcion == "4":
            menu_pagos()
        elif opcion == "5":
            print("Cerrando sesión de administrador...")
            return  # Return to main login instead of breaking
        else:
            print("Opción no válida. Intente nuevamente.")


def cliente_menu(cliente_actual):
    """Simplified menu for clients with essential operations"""
    while True:
        print(f"\n====== MENÚ CLIENTE - {cliente_actual.nombre} ======")
        print("1. Actualizar mis datos")
        print("2. Hacer una reserva")
        print("3. Modificar mi reserva")
        print("4. Cancelar mi reserva")
        print("5. Ver mis reservas")
        print("6. Cambiar de cliente")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Update client data
            print("Ingrese sus datos actualizados:")
            nombre = input("Nombre completo: ")
            n_identificacion = int(input("Número de identificación: "))
            correo = input("Correo electrónico: ")
            n_telefono = int(input("Número de teléfono: "))
            cliente_nuevo = Cliente.registrar_cliente(nombre, n_identificacion, correo, n_telefono)
            if cliente_nuevo:
                cliente_actual = cliente_nuevo
                print(f"Datos actualizados. Cliente actual: {cliente_actual.nombre}")

        elif opcion == "2":
            # Make reservation - use shared reservation system
            from Modulos.Reservas import get_sistema_reservas, gestor_habitaciones
            sistema_reservas = get_sistema_reservas()  # Get shared instance
            habitaciones_disponibles = gestor_habitaciones.get_habitaciones_disponibles()

            if not habitaciones_disponibles:
                print("No hay habitaciones disponibles en este momento.")
            else:
                print("Habitaciones disponibles:", habitaciones_disponibles)
                habitacion = input("Número de habitación: ")
                fecha = input("Fecha (dd/mm/aaaa): ")
                hora = input("Hora: ")
                sistema_reservas.crear_reserva(cliente_actual.nombre, habitacion, fecha, hora)

        elif opcion == "3":
            # Modify reservation - use shared system
            from Modulos.Reservas import get_sistema_reservas, gestor_habitaciones
            sistema_reservas = get_sistema_reservas()  # Shared instance
            habitaciones_disponibles = gestor_habitaciones.get_habitaciones_disponibles()

            print("Habitaciones disponibles:", habitaciones_disponibles)
            nueva_habitacion = input("Nueva habitación: ")
            nueva_fecha = input("Nueva fecha (dd/mm/aaaa): ")
            nueva_hora = input("Nueva hora: ")
            sistema_reservas.modificar_reserva(cliente_actual.nombre, nueva_habitacion, nueva_fecha, nueva_hora)

        elif opcion == "4":
            # Cancel reservation - use shared system
            from Modulos.Reservas import get_sistema_reservas
            sistema_reservas = get_sistema_reservas()  # Shared instance
            sistema_reservas.cancelar_reserva(cliente_actual.nombre)

        elif opcion == "5":
            # Show client's reservations - use current client data
            cliente_actual.mostrar_reservas_de_un_cliente()

        elif opcion == "6":
            cliente_actual = seleccionar_cliente()
            if cliente_actual is None:
                break

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


def main_menu(cliente_actual):
    """Legacy admin menu - kept for compatibility"""
    admin_menu()


if __name__ == "__main__":
    print("Bienvenido al Sistema de Gestión de Tickets para Hotel")

    while True:  # Main loop to return to login after logout
        # Login selection
        user_type = login()

        if user_type == "admin":
            # Admin has full access
            admin_menu()

        elif user_type == "cliente":
            # Client needs to select/register first
            cliente = seleccionar_cliente()
            if cliente:
                cliente_menu(cliente)
            else:
                print("Sistema cerrado.")
                break

        else:
            print("Sistema cerrado.")
            break