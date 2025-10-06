class Cliente:
    
    clientes_registrados = []
    def __init__(self,nombre,n_identificacion,correo,n_telefono):
        self.nombre = nombre
        self.n_identificacion = n_identificacion
        self.correo = correo
        self.n_telefono = n_telefono
        self.historial_de_reservas = []
        

    def registrar_cliente(self,cliente_nuevo):
        for cliente_existente in Cliente.clientes_registrados:
            if cliente_existente.n_identificacion == cliente_nuevo.identificacion:
                print("Este cliente ya se encuentra registrado en el sistema")
                return
            Cliente.clientes_registrados.append(cliente_nuevo)

    def actualizar_info_clientes(self,buscar_cliente,numero_de_documento ):
        for  cliente_existente in Cliente.clientes_registrados:
            if cliente_existente.nombre == buscar_cliente.lower():
                print(f"Los usuarios que tenemos registrados con el nombre : {buscar_cliente} son: ") 
                print(cliente_existente)
                
                numero_de_documento = int(input("Ingrese su número de identificacion, para poder continuar con la actualizacion" \
                "de algunos de sus datos"))
                if cliente_existente.n_identificacion == numero_de_documento:
                    print(f"Estos son sus datos actuales: {cliente_existente}")
                else:
                    return f"No hay ningún cliente en nuestros registros con el número de documento: {numero_de_documento}"    
                validar_desicion=input("Desea actualizar algunos de estos datos: si/no ")
                if validar_desicion.lower() == "si":
                    print("Eliga alguna de estas opciones: " \
                    "1. Actualizar nombre\n2. Actualizar correo\n3. Actualizar télefono" 
                        )
                    while True:
                             opcion=input()
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
                                  telefono_nuevo=int(input("Ingrese el nuevo telefono: "))
                                  try:
                                      cliente_existente.correo=telefono_nuevo
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
                return f"No hay un usuario que coincida con el nombre {buscar_cliente} en nuestros registros"

    
            

        pass