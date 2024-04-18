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

### Egreso :
- nro_egreso INT **PK**
- monto INT
- descripcion TEXT (opcional)
- fecha DATETIME
- id_registro **FK**

### Categoria:
- id_categoria INT **PK**
- nombre VARCHAR(50)

### categoria_x_ingreso:
- id_cxi INT **PK**
- nro_ingreso INT **FK**
- id_categoria INT **FK**

### categoria_x_egreso:
- id_cxe INT **PK**
- nro_egreso INT **FK**
- id_categoria INT **FK**


# Relacion del Sistema:
1. Usuario **tiene** Registro (_1 a N_) 
1. Registro **tiene** Ingreso (_1 a N_)
1. Registro **tiene** Egreso (_1 a N_)
1. Ingreso **tiene** Categoria (_N a N_)
1. Egreso **tiene** Categoria (_N a N_)


## Reglas de Negocio:

### Usuarios:
- Crear un usuario
- Leer todos los usuarios
- Leer un usuario en particular
- Actualizar un usuario
- Validar un usuario
- Actualizar datos de un usuario
- Actualizar Password de un usuario
- Eliminar un usuario

### Registro:
- Crear un registros
- Leer todos los registros
- Leer un registro en particular
- Actualizar un registro 
- Eliminar un registro

### Ingreso:
- Crear un ingreso
- Leer todos los ingresos
- Leer todos los ingresos de un usuario
- Leer un ingreso en particular
- Actualizar un ingreso 
- Eliminar un ingreso

### Egreso:
- Crear todos los egresos
- Leer todos los egresos
- Leer todos los egresos de un usuario
- Leer un egreso en particular
- Actualizar un egreso 
- Eliminar un egreso

### categoria_x_ingreso:
- Crear todos las cxi
- Leer todos los cxi
- Leer un cxi en particular
- Leer todos los cxi de un ingreso
- Eliminar un cxi

### categoria_x_egreso:
- Crear todos los cxe
- Leer todos los cxe
- Leer un cxe en particular
- Leer todos los cxe de un egreso
- Eliminar un cxe
