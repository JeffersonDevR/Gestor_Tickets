git # Sistema de Gestión Hotelera - Gestor de Tickets

## Descripción General del Proyecto

**Gestor de Tickets** es un sistema de gestión hotelera desarrollado en Python que permite administrar clientes, habitaciones, reservas y pagos de manera integrada.

**Versión:** 1.0
**Fecha:** Octubre 2025
**Tecnología:** Python (CLI)
**Arquitectura:** Modular con clases especializadas

## Características Implementadas

### ✅ Módulo de Gestión de Clientes
- Registro de nuevos clientes con validación de datos únicos
- Actualización de información de contacto (nombre, email, teléfono)
- Búsqueda de clientes por nombre o documento de identificación
- Listado completo de clientes registrados
- Historial de reservas por cliente

### ✅ Módulo de Gestión de Habitaciones
- Registro de habitaciones con número, tipo y tarifa
- Gestión de estados (disponible, ocupada, mantenimiento)
- Búsqueda por tipo y estado
- Estadísticas de ocupación
- Habitaciones predefinidas: Sencilla, Doble, Suite

### ✅ Módulo de Gestión de Reservas
- Creación de reservas con validación de disponibilidad
- Modificación de reservas existentes
- Cancelación de reservas
- Consulta de reservas por cliente y fecha
- Integración automática con gestión de habitaciones
- Estadísticas de reservas activas

### ✅ Módulo de Gestión de Pagos
- Procesamiento de pagos en efectivo
- Pagos con tarjeta de crédito/débito
- Pagos por transferencia bancaria
- Pagos con cheque
- Validación automática de métodos de pago

## Arquitectura del Sistema

El sistema utiliza un patrón de arquitectura modular con las siguientes características:

- **Separación de responsabilidades:** Cada módulo maneja una funcionalidad específica
- **Integración entre módulos:** Los módulos se comunican entre sí para mantener la consistencia de datos
- **Persistencia en memoria:** Los datos se mantienen durante la ejecución del programa
- **Interfaz de consola:** Menús interactivos para navegación intuitiva

## Tecnologías Utilizadas

- **Lenguaje:** Python 3.x
- **Paradigma:** Programación Orientada a Objetos
- **Patrones:** Clases especializadas y métodos de instancia/clase
- **Estructura:** Módulos independientes con imports cruzados para integración

## Requisitos del Sistema

- Python 3.6 o superior
- Sistema operativo: Windows, Linux o macOS
- Memoria RAM: 512 MB mínimo
- Espacio en disco: 50 MB

## Funcionalidades Destacadas

1. **Autenticación dual:** Administrador y Cliente con diferentes niveles de acceso
2. **Validación de datos:** Unicidad de documentos y emails, formatos válidos
3. **Gestión de estados:** Control automático de disponibilidad de habitaciones
4. **Integración completa:** Los módulos trabajan en conjunto para mantener consistencia
5. **Interfaz intuitiva:** Menús claros y navegación secuencial

## Instalación y Uso

1. Clonar o descargar el proyecto
2. Ejecutar `python main.py` desde el directorio raíz
3. Seleccionar modo de acceso (Administrador o Cliente)
4. Navegar por los diferentes módulos según las necesidades

## Estructura del Proyecto

```
Gestor_Tickets/
├── main.py                 # Punto de entrada y menú principal
├── README.md              # Información básica del proyecto
├── requirements.txt       # Dependencias (vacío - usa librerías estándar)
├── Documentacion/         # Documentación del proyecto
│   ├── README_Sistema.md  # Esta documentación actualizada
│   └── Gestor_Tickets_Doc.docx # Documentación original
└── Modulos/              # Módulos funcionales
    ├── Clientes.py       # Gestión de clientes
    ├── Habitaciones.py   # Gestión de habitaciones
    ├── Reservas.py       # Sistema de reservas
    └── Pagos.py          # Procesamiento de pagos
```

## Especificaciones Técnicas Detalladas

### Módulo de Clientes (`Clientes.py`)

**Clase Principal:** `Cliente`

**Características:**
- Almacenamiento en memoria de clientes registrados
- Validación de unicidad de documento de identificación
- Métodos de clase para registro y actualización
- Sistema de búsqueda por nombre y documento

**Métodos principales:**
- `registrar_cliente()` - Registro con validación de duplicados
- `actualizar_info_clientes()` - Actualización parcial de datos
- `mostrar_reservas_de_un_cliente()` - Historial de reservas

### Módulo de Habitaciones (`Habitaciones.py`)

**Clases Principales:** `Habitacion`, `GestorHabitaciones`

**Características:**
- Gestión de estados de habitación
- Habitaciones predefinidas al iniciar
- Estadísticas de ocupación en tiempo real
- Búsqueda y filtrado por criterios

**Métodos principales:**
- `agregar_habitacion()` - Registro de nuevas habitaciones
- `cambiar_estado()` - Modificación de estados
- `get_habitaciones_disponibles()` - Consulta de disponibilidad

### Módulo de Reservas (`Reservas.py`)

**Clase Principal:** `Reservas`

**Características:**
- Integración automática con habitaciones
- Validación de disponibilidad antes de crear reservas
- Actualización automática del historial del cliente
- Persistencia de reservas durante la sesión

**Métodos principales:**
- `crear_reserva()` - Creación con validación de disponibilidad
- `modificar_reserva()` - Modificación con liberación/ocupación automática
- `cancelar_reserva()` - Cancelación con liberación de habitación

### Módulo de Pagos (`Pagos.py`)

**Arquitectura:** Patrón Abstract Factory con clases especializadas

**Características:**
- Diferentes métodos de pago implementados
- Validación específica por tipo de pago
- Procesamiento simulado de transacciones
- Extensible para nuevos métodos de pago

**Clases de pago:**
- `PagoEnEfectivo` - Validación de monto positivo
- `PagoConTarjeta` - Validación de número y CVV
- `PagoConTransferencia` - Validación de cuenta y banco
- `PagoConCheque` - Validación de número de cheque y banco

## Flujos de Trabajo

### Flujo de Administrador
1. Inicio de sesión con credenciales
2. Acceso completo a todos los módulos
3. Gestión integral del sistema hotelero

### Flujo de Cliente
1. Selección o registro de cliente
2. Gestión de reservas personales
3. Consulta de historial personal

## Características de Seguridad

- **Autenticación básica:** Usuario/contraseña para administrador
- **Validación de datos:** Unicidad y formato de información crítica
- **Control de acceso:** Diferentes niveles según rol de usuario

## Limitaciones Actuales

- **Persistencia:** Los datos se pierden al cerrar la aplicación
- **Base de datos:** No utiliza sistema de almacenamiento permanente
- **Interfaz:** Solo disponible en modo consola/terminal
- **Reportes:** Funcionalidades básicas de estadísticas

## Posibles Mejoras Futuras

- Implementación de base de datos para persistencia
- Interfaz gráfica de usuario (GUI)
- Sistema de reportes avanzado
- Integración con sistemas externos
- API REST para integración con otros sistemas
- Sistema de notificaciones
- Módulo de mantenimiento preventivo
- Gestión de temporadas y tarifas dinámicas

---

## Información del Desarrollador

Este proyecto fue desarrollado como parte de ejercicios prácticos de programación en Python, enfocándose en:

- Programación Orientada a Objetos
- Diseño modular
- Integración entre componentes
- Validación de datos
- Manejo de errores básico
- Arquitectura de software

**Estado del proyecto:** Funcional para demostración y aprendizaje