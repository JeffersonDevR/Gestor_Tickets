class Cliente:
    """
    Clase que representa a un cliente del hotel.
    """
    # Lista de clase para almacenar todos los clientes registrados.
    clientes_registrados = []

    def __init__(self, nombre, n_identificacion, correo, n_telefono):
        """
        Inicializa un nuevo objeto Cliente.

        Args:
            nombre (str): El nombre completo del cliente.
            n_identificacion (int): El número de identificación del cliente.
            correo (str): El correo electrónico del cliente.
            n_telefono (int): El número de teléfono del cliente.
        """
        self.nombre = nombre
        self.n_identificacion = n_identificacion
        self.correo = correo
        self.n_telefono = n_telefono
        self.historial_de_reservas = []

    @classmethod
    def registrar_cliente(cls, nombre, numero_documento, correo_electr, telefono):
        """
        Registra un nuevo cliente en el sistema.

        Args:
            nombre (str): Nombre del cliente.
            numero_documento (int): Número de identificación.
            correo_electr (str): Correo electrónico.
            telefono (int): Número de teléfono.

        Returns:
            Cliente: El objeto del cliente recién creado o None si ya existe.
        """
        # Verifica si el cliente ya está registrado.
        if any(cliente.n_identificacion == numero_documento for cliente in cls.clientes_registrados):
            print("Este cliente ya se encuentra registrado en el sistema.")
            return None

        # Crea y registra al nuevo cliente.
        cliente_nuevo = cls(nombre, numero_documento, correo_electr, telefono)
        cls.clientes_registrados.append(cliente_nuevo)
        print("Cliente registrado con éxito.")
        return cliente_nuevo

    @classmethod
    def actualizar_info_cliente(cls, n_identificacion, nuevo_nombre=None, nuevo_correo=None, nuevo_telefono=None):
        """
        Actualiza la información de un cliente existente.

        Args:
            n_identificacion (int): Número de identificación del cliente a actualizar.
            nuevo_nombre (str, optional): El nuevo nombre del cliente.
            nuevo_correo (str, optional): El nuevo correo del cliente.
            nuevo_telefono (int, optional): El nuevo número de teléfono.

        Returns:
            bool: True si el cliente fue actualizado, False en caso contrario.
        """
        cliente_a_actualizar = next((c for c in cls.clientes_registrados if c.n_identificacion == n_identificacion), None)
        
        if cliente_a_actualizar:
            if nuevo_nombre:
                cliente_a_actualizar.nombre = nuevo_nombre
            if nuevo_correo:
                cliente_a_actualizar.correo = nuevo_correo
            if nuevo_telefono:
                cliente_a_actualizar.n_telefono = nuevo_telefono
            print("Información del cliente actualizada con éxito.")
            return True
        
        print(f"No se encontró ningún cliente con el número de documento: {n_identificacion}.")
        return False

    def mostrar_reservas(self):
        """
        Muestra el historial de reservas de este cliente.
        """
        if self.historial_de_reservas:
            print(f"Historial de reservas de {self.nombre}:")
            for reserva in self.historial_de_reservas:
                print(reserva)
        else:
            print(f"El cliente {self.nombre} no tiene reservas asignadas.")

    def __str__(self):
        """
        Devuelve una representación en cadena del objeto Cliente.
        """
        return (f"Cliente: {self.nombre} | Identificación: {self.n_identificacion} | "
                f"Correo: {self.correo} | Teléfono: {self.n_telefono}")