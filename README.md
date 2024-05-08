# Aplicacion de Control de Gastos

**Idea General**:
- Poder ingresar un monto ,y que de ese monto se pueda ir descontando o sumando dinero ,y que este se vea reflejado en un gráfico con diferentes colores dependiendo de las categorías ,y tener la opción para ver en forma cuantitativa por categorías o sino por porcentajes 
- Además de poder tener diferentes Gastos apartes ,osea que no sea necesariamente de un solo INGRESO que se descuente todo ,pero lo preferible si 
- Los ingresos y egresos pueden tener multiples categorias
- Obviamente a una cuenta le pertenecen sus registros 


## Entidades:

### Usuario
- id_usuario INT **PK**
- email VARCHAR (100) **PK** ó **UQ**
- nombre VARCHAR(50)
- apellido VARCHAR(50)
- username VARCHAR(100) **UQ**
- avatar VARCHAR(255) (opcional)
- password VARCHAR(100)

### Registro :
- id_registro INT **PK**
- id_usuario INT **FK**

### Ingreso :
- nro_ingreso INT **PK**
- monto INT
- descripcion TEXT (opcional)
- fecha DATETIME
- id_registro **FK**
- id_categoria **FK**

### Egreso :
- nro_egreso INT **PK**
- monto INT
- descripcion TEXT (opcional)
- fecha DATETIME
- id_registro **FK**
- id_categoria **FK**

### Categoria:
- id_categoria INT **PK**
- nombre VARCHAR(50)



# Relacion del Sistema:
1. Usuario **tiene** Registro (_1 a N_) 
1. Registro **tiene** Ingreso (_1 a N_)
1. Registro **tiene** Egreso (_1 a N_)
1. Ingreso **tiene** Categoria (_N a 1_)
1. Egreso **tiene** Categoria (_N a 1_)


## Reglas de Negocio:

### Usuarios:
- Crear un usuario ✅
- Leer todos los usuarios ❌
- Leer un usuario en particular ✅
- Actualizar un usuario ✅
- Validar un usuario ✅
- Actualizar Password de un usuario ✅
- Eliminar un usuario ✅

### Registro:
- Crear un registros ✅
- Leer todos los registros ❌
- Leer todos los registros asociados a un usuario ✅
- Eliminar un registro ✅

### Ingreso:
- Crear un ingreso ✅
- Leer todos los ingresos ❌
- Leer todos los ingresos de un usuario✅
- Leer un ingreso en particular ✅
- Actualizar un ingreso ✅
- Eliminar un ingreso ✅

### Egreso:
- Crear un egreso ✅
- Leer todos los egresos ❌
- Leer todos los egresos de un usuario ✅
- Leer un egreso en particular ✅
- Actualizar un egreso ✅
- Eliminar un egreso ✅

### Categoria:
- Crear todas las categorias ✅
- Leer todas las categorias ✅
- Leer una categoria en particular ✅
- Editar una categoria ✅
- Eliminar una categoria ✅
 



## Categorias De BASE:

**Ingresos:** 

1. Salario
1. Ingresos por freelance/trabajo independiente
1. Ingresos por alquiler de propiedad
1. Ingresos por inversiones (dividendos, intereses, etc.)
1. Reembolsos
1. Bonificaciones
1. Regalos
1. Otros ingresos (venta de artículos, trabajos esporádicos, etc.)

**Egresos:**

1. Vivienda (alquiler/hipoteca)
1. Alimentación
1. Transporte (combustible, transporte público, mantenimiento de vehículos)
1. Servicios públicos (electricidad, agua, gas, internet, teléfono)
1. Salud (seguro médico, consultas médicas, medicamentos)
1. Entretenimiento (cine, conciertos, actividades recreativas)
1. Educación (matrículas, libros, cursos)
1. Ahorros e inversiones
1. Ropa y accesorios
1. Cuidado personal (productos de belleza, peluquería, gimnasio)
1. Viajes y vacaciones
1. Donaciones y caridad
1. Deudas (pagos de préstamos, tarjetas de crédito)
1. Seguros (seguro de automóvil, seguro de hogar)
1. Impuestos