#Procesamiento de pagos de manera asincrona, validando medios de pago, estado de las transacciones y confirmaciones automaticas
from abc import ABC, abstractmethod
from enum import Enum

# class MetodoDePago(Enum):
#     TARJETA_CREDITO = "tarjeta_credito"
#     TRANSFERENCIA = "transferencia"
#     EFECTIVO = "efectivo"

class Pago(ABC):

    def __init__(self,amount:float,date):
        self.amount = amount
        self.date = date
        self.status = "pending"

    @abstractmethod
    def process(self) -> bool:
        pass

    @abstractmethod
    def validate(self) -> bool:
        pass



class PagoEnEfectivo(Pago):

    def __init__(self, amount, date):
        super().__init__(amount, date)


    def validate(self) -> bool:
        return self.amount > 0

    def process(self) -> bool:
        if not self.validate():
            return False
        print(f"Pago en efectivo realizado: ${self.amount:,.0f} COP")
        self.status = "completed"
        return True

class PagoConTarjeta(Pago):

    def __init__(self, amount, date,card_number:str,cvv:str):
        super().__init__(amount, date)
        self.card_number = card_number
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
        print(f"Pago con tarjeta completado: ${self.amount:,.0f} COP")
        self.status = "completed"
        return True


def menu():
    while True:
        print("====== GESTIÓN DE PAGOS ======")
        print("1. Pago en efectivo")
        print("2. Pago con tarjeta")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            amount = float(input("Ingrese el monto: "))
            date = input("Ingrese la fecha (dd/mm/aaaa): ")
            pago = PagoEnEfectivo(amount, date)
            if pago.process():
                print("Pago en efectivo procesado exitosamente.")
            else:
                print("Error en el pago en efectivo.")

        elif opcion == "2":
            amount = float(input("Ingrese el monto: "))
            date = input("Ingrese la fecha (dd/mm/aaaa): ")
            card_number = input("Ingrese el número de tarjeta (26 dígitos): ")
            cvv = input("Ingrese el CVV (3 dígitos): ")
            pago = PagoConTarjeta(amount, date, card_number, cvv)
            if pago.process():
                print("Pago con tarjeta procesado exitosamente.")
            else:
                print("Error en el pago con tarjeta.")

        elif opcion == "3":
            print("Saliendo del módulo de pagos...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
    
