class Cliente:
    
    clientes_registrados = []
    def __init__(self,nombre,n_identificacion,correo,n_telefono):
        self.nombre = nombre
        self.n_identificacion = n_identificacion
        self.correo = correo
        self.n_telefono = n_telefono
        self.historial_de_reservas = []
        
    @classmethod
    def registrar_cliente(cls,nombre,numero_documento,correo_electr,telefono):
        for cliente_existente in cls.clientes_registrados:
            if cliente_existente.n_identificacion == numero_documento:
                print("Este cliente ya se encuentra registrado en el sistema")
                return 
        else:#este else va con el for, no con el if. Para evitar duplicados(osea que si no es if,vaya al else
            #y me cree un usuario con el el mismo documento, ya que el else, no tiene ninguna validacion)
            cliente_nuevo=Cliente(nombre,numero_documento,correo_electr,telefono)
            Cliente.clientes_registrados.append(cliente_nuevo)
            print("Cliente registrado con éxito")
            return cliente_nuevo
    @classmethod
    def actualizar_info_clientes(cls,buscar_cliente):
        encontrado=False
        for  cliente_existente in cls.clientes_registrados:
            if buscar_cliente.lower() in cliente_existente.nombre.lower():
                if not encontrado:
                   print(f"Los usuarios que tenemos registrados con el nombre : {buscar_cliente} son: ") 
                   encontrado=True#para que se muestre una sola vez el mensaje
                print(cliente_existente.nombre)
            else:
              print(f"No hay un usuario que coincida con el nombre {buscar_cliente} en nuestros registros")
              return  
        numero_de_documento = int(input("Ingrese su número de identificacion, para poder continuar con la actualizacion" \
                "de algunos de sus datos; "))
        for cliente_coincididos in Cliente.clientes_registrados:
            if cliente_coincididos.n_identificacion == numero_de_documento:
                    print(f"Estos son sus datos actuales: {cliente_coincididos}")

                    validar_desicion=input("Desea actualizar algunos de estos datos: si/no ")
                    if validar_desicion.lower() == "si":   
                        
                        while True:
                             print("Eliga alguna de estas opciones: " \
                                   "\n1. Actualizar nombre\n2. Actualizar correo\n3. Actualizar télefono")
                             
                             opcion=input("Ingrese una opción: ")
                             if opcion=="1":
                                nombre_nuevo=input("Ingrese el nuevo nombre: ")
                                if "1234567890¿@+*" in nombre_nuevo:
                                    print("Socio solo se aceptan letras,no es un gamername")
                                else:
                                    cliente_existente.nombre=nombre_nuevo
                                    print("El nombre ha sido actualizado con éxito")
                                    break

                             elif opcion=="2":
                                  correo_nuevo=input("Ingrese el nuevo correo: ")
                                  if "@" and ".com" in correo_nuevo:
                                    cliente_existente.correo=correo_nuevo
                                    print("El correo ha sido actualizado con éxito")
                                    break
                                  else:
                                    print("¡Paila menor!.Ingrese un formato de correo electrónico válido")

                             elif opcion=="3":
                                  try:
                                      telefono_nuevo=int(input("Ingrese el nuevo telefono: "))
                                  
                                      cliente_existente.n_telefono=telefono_nuevo
                                      print("El télefono ha sido actualizado con éxito")
                                      break
                                  except ValueError:
                                      print("¡No sea bruto!,solo se puede ingresar valores numericos para teléfonos")
                             else:
                
                                 print("Papito no sea bruto,ingrese una opción de las que se muestran")
                    elif validar_desicion.lower()== "no":
                        return f"Okey, no quieres cambios, saliendo de la opción actualizar...."
                    else:
                        print("Ingrese si o no,animal.")
            else:
                print( f"No hay ningún cliente en nuestros registros con el número de documento: {numero_de_documento}")
    def mostrar_reservas_de_un_cliente(self):
        nombre_cliente_busq=input("Ingrese el nombre del cliente que desea consultar: ")
        documento_cliente_busq=int(input("Ingrese  su número de identificación"))
        for cliente in self.historial_de_reservas:
           if nombre_cliente_busq==cliente.n_identificacion and documento_cliente_busq==cliente.n_identificacion and documento_cliente_busq== cliente.correo :
               print(cliente.historial_de_reservas)
               


    def __str__(self):
        return f"Cliente: {self.nombre}||\nIdentificación: {self.n_identificacion}|| Correo electrónico: {self.correo}|| Número de contacto: {self.n_telefono}"
            

while True:
    option=input("Ingrese una opción: ")
    if option=="1":
        print("Ingrese sus datos, para hacer el registro: ")
        name= input("Ingrese su nombre completo(con apellidos): ")
        number_docu=int(input("Ingrese su número de identificación: "))
        email_electro=input("Ingrese su correo electrónico: ")
        iphone=int(input("Ingrese su número de teléfono: "))
        Cliente.registrar_cliente(name,number_docu,email_electro,iphone)
        for clientes in Cliente.clientes_registrados:
            print(clientes)
       
    elif option=="2":
        
        if not Cliente.clientes_registrados:
            print("No hay clientes registrados hasta el momento en el sistema")
        else:
            print("Ingrese el nombre del cliente que desea buscar: ")
            nombre_cliente=input("")
            Cliente.actualizar_info_clientes(nombre_cliente)
        
            
    elif option=="3":
        print("Adios bby")
        break    
    else:
        print("Escoja del 1 al 3 bobo")


        