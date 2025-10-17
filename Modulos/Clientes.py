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
            cls.clientes_registrados.append(cliente_nuevo)
            print("Cliente registrado con éxito")
            return cliente_nuevo
    @classmethod
    def actualizar_info_clientes(cls,buscar_cliente):
        encontrado=False
        for  cliente_existente in cls.clientes_registrados:
            if buscar_cliente.lower() in cliente_existente.nombre.lower().split():
                if not encontrado:
                   print(f"Los usuarios que tenemos registrados con el nombre : {buscar_cliente} son: ") 
                   encontrado=True#para que se muestre una sola vez el mensaje
                print(cliente_existente.nombre)
        if not encontrado:
              print(f"No hay un usuario que coincida con el nombre {buscar_cliente} en nuestros registros")
              return  
        numero_de_documento = int(input("Ingrese su número de identificacion, para poder continuar con la actualizacion" \
                "de algunos de sus datos; "))
        for cliente_coincididos in cls.clientes_registrados:
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
            
                                if nombre_nuevo.replace(" ", "").isalpha():#replace ayuda a que alpha no me termine por tener espacios, los quita temporal, para validar solo letras.
                                    cliente_coincididos.nombre=nombre_nuevo
                                    print("Nombre actualizado con éxito")
                                    break
                                    
                                else:
                                    print("Solo se aceptan letras")
                                    

                             elif opcion=="2":
                                  correo_nuevo=input("Ingrese el nuevo correo: ")
                                  if "@"  in correo_nuevo and ".com"  in correo_nuevo:
                                    for cliente in cls.clientes_registrados:
                                       if cliente.correo==correo_nuevo:
                                           print("¡Error!, este correo ya esta asociado a un cliente.")
                                           break

                                    else:
                                        cliente_coincididos.correo=correo_nuevo
                                        print("El correo ha sido actualizado con éxito")
                                        break
                                    
                                  else:
                                      print("¡Error!.Ingrese un formato de correo electrónico válido")
                                     

                             elif opcion=="3":
                                  
                                      telefono_nuevo_str=input("Ingrese el nuevo telefono: ")
                                      if len(telefono_nuevo_str)==10:
                                         try:
                                             telefono_nuevo=int(telefono_nuevo_str)
                                             cliente_coincididos.n_telefono=telefono_nuevo
                                             print("El télefono ha sido actualizado con éxito")
                                             break
                                         except ValueError:
                                            print("¡Solo se puede ingresar valores numericos para teléfonos")
                                      else: 
                                          print("El telefono debe contener 10 digitos exactos.")                             
                                    
                             else:
                
                                 print("Ingrese una opción de las que se muestran")#Se refiere al mini menu de mi while
                    elif validar_desicion.lower()== "no":
                        print(f"Okey, no quieres cambios, saliendo de la opción actualizar....")
                        return      
                    else:
                        print("Ingrese si o no")#es para si la opcion e diferente a no o si
                    break
        else:#colocar este else, con el for o un return al if y luego un print al terminar el bucle, sino encuentra.(el print sin el else
                #solo si el if tiene un return para terminar cuando se cumpla, sino asi se cumpla va seguir y me va imprimir el print, cosa que no seria)
                print( f"No hay ningún cliente en nuestros registros con el número de documento: {numero_de_documento}")
    def mostrar_reservas_de_un_cliente(self,historial_reservas_g, cliente):
        self.historial_de_reservas=[reserva for reserva in historial_reservas_g
            if cliente.n_identificacion == reserva.cliente.n_identificacion]
        if self.historial_de_reservas:      
            for r in self.historial_de_reservas:
                print(r)
        else:
            print(f"El cliente {cliente.nombre}  no tiene reservas  en su historial")  
              
            


    def __str__(self):
        return (
        f"\n=== Datos del Cliente ===\n"
        f"Nombre: {self.nombre}\n"
        f"Identificación: {self.n_identificacion}\n"
        f"Correo: {self.correo}\n"
        f"Teléfono: {self.n_telefono}\n"
        f"========================="
    )
if __name__=="__main__":
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
            cliente_instancia=None
            for client in Cliente.clientes_registrados:
                cliente_instancia=client
            if cliente_instancia is not None:   
                cliente_instancia.mostrar_reservas_de_un_cliente()
            else:
                print("No hay clientes registrados en el sistema para ver sus reservas.")
                    
        elif option=="4":
            print("Saliendo...")
            break       
        else:
            print("Escoja del 1 al 3 ")


            