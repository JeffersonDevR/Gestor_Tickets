#Procesamiento de pagos de manera asincrona, validando medios de pago, estado de las transacciones y confirmaciones automaticas


class Pagos():
    
    def __init__(self):
        self.medios_de_pago = ["Efectivo", "Tarjeta","Nequi"]
        
    def validar_pago(self,metodo_pago_cliente):
        if metodo_pago_cliente in self.medios_de_pago:
            print("Pago procesado.")
            
        else:
            print("Pago no procesado.")
        
    def procesar_pago(self,medio_de_pago):
        pass
    
    def mostrar_estados_transacciones(self):
        pass        
    
    def procesar_reembolso(self,aprobado):
        pass
