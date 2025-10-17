# Sistema de Gestión Hotelera
---
## VISIÓN GENERAL DEL PROYECTO

### Descripción del Sistema
Sistema integral de gestión hotelera desarrollado en Python que permite la administración completa de operaciones hoteleras a través de una interfaz de línea de comandos (CLI). El sistema está diseñado para manejar dos tipos de usuarios principales: **Administradores** y **Clientes**, con funcionalidades diferenciadas según el rol.

### Alcance del Sistema
- Gestión completa del ciclo de vida del cliente
- Administración de inventario de habitaciones
- Procesamiento de reservas y modificaciones
- Gestión de pagos con múltiples métodos
- Reportes básicos de ocupación y operaciones

---

## ARQUITECTURA TÉCNICA
### Tecnologías Utilizadas
- **Lenguaje**: Python 3.8+
- **Paradigma**: Programación Orientada a Objetos
- **Asincronía**: asyncio para operaciones concurrentes
- **Validación**: Pydantic para modelos de datos

### Patrón Arquitectónico
El sistema sigue un patrón de arquitectura modular donde cada módulo representa una entidad de negocio específica:


## REQUISITOS FUNCIONALES Y HISTORIAS DE USUARIO

### MÓDULO 1: GESTIÓN DE CLIENTES

#### RF-001: Registro de nuevos clientes

**Descripción**: El sistema debe permitir el registro de nuevos clientes con información personal básica.

**Historia de Usuario US-001**

**Título**: Registro de nuevo cliente en el sistema

*Como*: Recepcionista del hotel o Cliente

*Quiero*: Registrar un nuevo cliente con su información personal completa

*Para que*: Pueda crear su perfil en el sistema y posteriormente realizar reservas a su nombre

**Criterios de Aceptación**:
- ✓ El sistema solicita: nombre completo, identificación, email, teléfono
- ✓ El nombre debe contener solo letras y espacios
- ✓ La identificación debe ser un número único en el sistema
- ✓ El email debe tener formato válido (@ y dominio)
- ✓ El teléfono debe contener exactamente 10 dígitos
- ✓ Se genera automáticamente un registro en el sistema
- ✓ Se muestra mensaje de confirmación con los datos registrados
- ✓ En caso de error de validación, se muestra mensaje específico
- 

#### RF-002: Actualización de información de clientes

**Descripción**: El sistema debe permitir actualizar la información de contacto de clientes existentes.

**Historia de Usuario US-002**

**Título**: Actualización de información de cliente

*Como*: Cliente o Recepcionista del hotel

*Quiero*: Actualizar la información de contacto de un cliente existente

*Para que*: Los datos del cliente se mantengan actualizados y correctos en el sistema

**Criterios de Aceptación**:
- ✓ El sistema permite buscar al cliente por nombre
- ✓ Se pueden modificar: nombre, email y teléfono
- ✓ La identificación NO puede ser modificada (es identificador único)
- ✓ Se aplican las mismas validaciones que en el registro inicial
- ✓ Se muestra confirmación de actualización exitosa
- ✓ Si el cliente no existe, se muestra mensaje de error


### MÓDULO 2: GESTIÓN DE HABITACIONES 🏨

#### RF-003: Registro de habitaciones

**Descripción**: El sistema debe permitir registrar habitaciones con número, tipo y tarifa.

**Historia de Usuario US-003**

**Título**: Registro de nueva habitación en el sistema

*Como*: Administrador del hotel

*Quiero*: Registrar una nueva habitación con sus características

*Para que*: Esté disponible para ser reservada por los clientes

**Criterios de Aceptación**:
- ✓ Se solicita: número de habitación, tipo, tarifa por noche
- ✓ El número de habitación debe ser único en el sistema
- ✓ El tipo puede ser: Sencilla, Doble, Suite, etc.
- ✓ La tarifa debe ser un número mayor a 0
- ✓ El estado inicial de la habitación es "disponible"
- ✓ Se muestra confirmación con los datos de la habitación creada


#### RF-004: Gestión de estados de habitación

**Descripción**: El sistema debe gestionar diferentes estados de las habitaciones (disponible, ocupada, mantenimiento).

**Historia de Usuario US-004**

**Título**: Gestión de estados de habitaciones

*Como*: Recepcionista del hotel

*Quiero*: Cambiar el estado de una habitación según su situación actual

*Para que*: El sistema refleje correctamente la disponibilidad real de cada habitación

**Criterios de Aceptación**:
- ✓ Estados posibles: disponible, ocupada, mantenimiento
- ✓ Solo habitaciones "disponibles" pueden ser reservadas
- ✓ El estado cambia automáticamente a "ocupada" al crear reserva
- ✓ El estado cambia automáticamente a "disponible" al cancelar reserva
- ✓ Se puede cambiar manualmente a "mantenimiento" cuando sea necesario


### MÓDULO 3: GESTIÓN DE RESERVAS

#### RF-005: Creación de reservas

**Descripción**: El sistema debe permitir crear nuevas reservas validando disponibilidad de habitaciones.

**Historia de Usuario US-005**

**Título**: Creación de nueva reserva

*Como*: Recepcionista del hotel o Cliente

*Quiero*: Crear una reserva para un cliente

*Para que*: Pueda asegurar una habitación para su estadía

**Criterios de Aceptación**:
- ✓ Se requiere: cliente, habitación, fecha, hora
- ✓ El cliente debe estar registrado en el sistema
- ✓ La habitación debe existir y estar disponible
- ✓ Se verifica disponibilidad antes de confirmar reserva
- ✓ Se genera registro de reserva en el sistema
- ✓ El estado de la habitación cambia automáticamente a "ocupada"
- ✓ Se calcula automáticamente el monto total de la reserva
- ✓ Se muestra confirmación con todos los detalles de la reserva


#### RF-006: Modificación de reservas

**Descripción**: El sistema debe permitir modificar fechas, horas y habitaciones de reservas existentes.

**Historia de Usuario US-006**

**Título**: Modificación de reserva existente

*Como*: Recepcionista del hotel o Cliente

*Quiero*: Modificar los detalles de una reserva existente

*Para que*: Pueda ajustar la reserva según necesidades del cliente

**Criterios de Aceptación**:
- ✓ Se puede modificar: fecha, hora y habitación
- ✓ Se valida disponibilidad de la nueva habitación
- ✓ Se libera automáticamente la habitación anterior
- ✓ Se ocupa automáticamente la nueva habitación
- ✓ Se muestra confirmación de modificación exitosa


#### RF-007: Cancelación de reservas

**Descripción**: El sistema debe permitir cancelar reservas y liberar habitaciones automáticamente.

**Historia de Usuario US-007**

**Título**: Cancelación de reserva

*Como*: Recepcionista del hotel o Cliente

*Quiero*: Cancelar una reserva existente

*Para que*: Pueda liberar la habitación para otros clientes

**Criterios de Aceptación**:
- ✓ Se puede cancelar cualquier reserva activa
- ✓ Se libera automáticamente la habitación (estado "disponible")
- ✓ Se elimina el registro de reserva del sistema
- ✓ Se muestra confirmación de cancelación


### MÓDULO 4: GESTIÓN DE PAGOS

#### RF-008: Procesamiento de pagos

**Descripción**: El sistema debe permitir procesar pagos en efectivo y con tarjeta de crédito.

**Historia de Usuario US-008**

**Título**: Procesamiento de pagos de reservas

*Como*: Recepcionista del hotel o Cliente

*Quiero*: Procesar el pago de una reserva

*Para que*: Pueda confirmar la reserva y registrar el pago

**Criterios de Aceptación**:
- ✓ Se aceptan pagos en efectivo
- ✓ Se aceptan pagos con tarjeta de crédito/débito
- ✓ Para pagos con tarjeta se valida: número (16 dígitos) y CVV (3 dígitos)
- ✓ El monto debe ser mayor a 0
- ✓ Se registra fecha y hora del pago
- ✓ Se muestra confirmación del pago exitoso
- ✓ Se marca la reserva como pagada

---

## MANUAL DE USUARIO

### Para Administradores

#### Gestión de Clientes
- Ver todos los clientes registrados
- Actualizar información de clientes existentes

#### Gestión de Habitaciones
- Ver todas las habitaciones
- Agregar nuevas habitaciones
- Cambiar estado de habitaciones (disponible/ocupada/mantenimiento)

#### Gestión de Reservas
- Ver todas las reservas
- Crear nuevas reservas
- Modificar reservas existentes
- Cancelar reservas

#### Gestión de Pagos
- Procesar pagos de reservas

### Para Clientes

#### Registro e Inicio de Sesión
- Crear nueva cuenta de cliente
- Iniciar sesión con identificación

#### Gestión Personal
- Ver datos personales
- Actualizar información personal

#### Reservas
- Crear nuevas reservas
- Ver reservas propias
- Modificar reservas
- Cancelar reservas
- Pagar reservas pendientes


---

**Estado del Proyecto**: En desarrollo activo
**Última Actualización**: Octubre 2025
**Versión**: 1.0.0

