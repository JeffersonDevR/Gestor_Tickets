#Procesamiento de pagos de manera asincrona, validando medios de pago, estado de las transacciones y confirmaciones automaticas
from abc import ABC, abstractmethod
from enum import Enum

# class MetodoDePago(Enum):
#     TARJETA_CREDITO = "tarjeta_credito"
#     TRANSFERENCIA = "transferencia"
#     EFECTIVO = "efectivo"

class Pago(ABC):

    def __init__(self,ammount:float,date):
        self.ammount = ammount
        self.date = date
        self.status = "pending"

    @abstractmethod
    def process(self) -> bool:
        pass

    @abstractmethod
    def validate(self) -> bool:
        pass



class PagoEnEfectivo(Pago):

    def __init__(self, ammount, date):
        super().__init__(ammount, date)
        

    def validate(self) -> bool:
        return self.ammount > 0
    
    def process(self) -> bool;
        if not self.validate():
            return False
        print(f"Pago en efectivo realizado: ${self.ammount}")
        self.status = "completed" 
        return True  

class PagoConTarjeta(Pago):

    def __init__(self, ammount, date,card_number:str,cvv:str):
        super().__init__(ammount, date)
        self.card_number - card_number
        self.cvv = cvv

    def validate(self) -> bool:

        if len(self.card_number) != 26:
            return False
        if len(self.cvv) != 3:
            return False
        return True
        
    def process(self) -> bool:
        if not self.validate():
            return False
        print(f"Pago con tarjeta completado: ${self.amount}")
        self.status = "completed"
        return True