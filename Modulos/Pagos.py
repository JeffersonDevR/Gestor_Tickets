# Importamos Pydantic para la validación de datos y otros módulos necesarios.
from pydantic import BaseModel, validator, Field
from typing import ClassVar
from abc import ABC, abstractmethod
from datetime import datetime

# Definimos una clase base para los pagos que hereda de BaseModel de Pydantic.
class Pago(BaseModel, ABC):
    """
    Clase base para representar un pago.

    Atributos:
        monto (float): La cantidad del pago.
        fecha (datetime): La fecha y hora en que se procesó el pago.
        estado (str): El estado actual del pago ('pendiente', 'completado', 'fallido').
    """
    monto: float = Field(..., gt=0, description="El monto debe ser un número positivo.")
    fecha: datetime = Field(default_factory=datetime.now)
    estado: str = "pendiente"

    # Método abstracto que debe ser implementado por las subclases para procesar el pago.
    @abstractmethod
    def procesar(self) -> bool:
        """Procesa el pago y retorna True si fue exitoso, de lo contrario False."""
        pass

# Definimos una clase para pagos en efectivo que hereda de la clase base Pago.
class PagoEnEfectivo(Pago):
    """
    Representa un pago realizado en efectivo.
    """
    def procesar(self) -> bool:
        """
        Procesa un pago en efectivo.
        Para los pagos en efectivo, el procesamiento es directo y se considera exitoso.
        """
        self.estado = "completado"
        print(f"Pago en efectivo de ${self.monto:,.2f} procesado exitosamente.")
        return True

# Definimos una clase para pagos con tarjeta que también hereda de Pago.
class PagoConTarjeta(Pago):
    """
    Representa un pago realizado con tarjeta de crédito/débito.

    Atributos:
        numero_tarjeta (str): El número de la tarjeta, que debe tener 16 dígitos.
        cvv (str): El código de seguridad de la tarjeta, que debe tener 3 dígitos.
    """
    numero_tarjeta: str
    cvv: str

    # Usamos un validador de Pydantic para asegurar que el número de tarjeta tenga 16 dígitos.
    @validator('numero_tarjeta')
    def validar_numero_tarjeta(cls, v):
        if len(v) != 16 or not v.isdigit():
            raise ValueError('El número de tarjeta debe tener 16 dígitos numéricos.')
        return v

    # Usamos otro validador para el CVV, que debe tener 3 dígitos.
    @validator('cvv')
    def validar_cvv(cls, v):
        if len(v) != 3 or not v.isdigit():
            raise ValueError('El CVV debe tener 3 dígitos numéricos.')
        return v

    def procesar(self) -> bool:
        """
        Procesa un pago con tarjeta.
        Simula una validación con una pasarela de pagos.
        """
        print(f"Procesando pago de ${self.monto:,.2f} con tarjeta {self.numero_tarjeta[-4:]}...")
        # Simulación de un procesamiento exitoso
        self.estado = "completado"
        print("Pago con tarjeta procesado exitosamente.")
        return True

# Definimos una clase para gestionar los pagos.
class GestorDePagos:
    """
    Gestiona y procesa los diferentes tipos de pagos.
    """
    def __init__(self):
        self.pagos_procesados: ClassVar[list] = []

    def realizar_pago(self, pago: Pago) -> bool:
        """
        Realiza un pago utilizando el método de pago proporcionado.

        Args:
            pago (Pago): Una instancia de una subclase de Pago.

        Returns:
            bool: True si el pago fue exitoso, False en caso contrario.
        """
        try:
            if pago.procesar():
                self.pagos_procesados.append(pago)
                return True
            else:
                pago.estado = "fallido"
                print("El pago no pudo ser procesado.")
                return False
        except ValueError as e:
            print(f"Error de validación: {e}")
            return False