class Cliente:
    def __init__(self,nombre,n_identificacion,correo,n_telefono):
        self.nombre = nombre
        self.n_identificacion = n_identificacion
        self.correo = correo
        self.n_telefono = n_telefono
        self.historial_de_reservas = []
        self.clientes_registrados = []

    def registrar_cliente(self,cliente_nuevo):
        for cliente_existente in self.clientes_registrados:
            if cliente_existente.n_identificacion == cliente_nuevo.identificacion:
                print("Este cliente ya se encuentra registrado en el sistema")
                return
        self.clientes_registrados.append(cliente_nuevo)

    def actualizar_info_clientes():

    
            

        pass