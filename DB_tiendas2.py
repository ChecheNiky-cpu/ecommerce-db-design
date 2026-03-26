import pymysql.cursors


class Cliente:
    def __init__(self, nombre, email):
        self.__nombre = ""
        self.__email = ""
        self.set_nombre(nombre)
        self.set_email(email)

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_email(self, email):
        self.__email = email

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email


class ConectotDB:
    def __init__(self, host, user, password, db):
        self.conection = pymysql.connect(host=host,
                                         user=user,
                                         password=password,
                                         database=db)


def validar_email():
    pass


def crear_pedido(cursor, conexion):
    try:
        nombre = input("Nombre del cliente: ")
        email = input("Email del cliente: ")
        clientes = Cliente(nombre, email)
        sql = "INSERT INTO helados (nombre, email)  VALUES (%s,%s)"
        cursor.execute(
            sql, (clientes.get_nombre(), clientes.get_email()))
        conexion.commit()
    except Exception:
        print("Problema en la DB")


def actualizar_cliente(cursor, conexion):
    try:
        id_cliente = input("ID del cliente a actualizar: ")
        nuevo_nombre = input("Nuevo nombre: ")
        cursor.execute(
            "UPDATE clientes SET nombre = %s WHERE id = %s", (nuevo_nombre, id_cliente))
        conexion.commit()
    except ValueError:
        print("Error en la bd")
        # %s se usa para evitar inyecciones SQL


def actualizar_email(cursor, conexion):
    try:
        id_cliente = input("ID del cliente a actualizar: ")
        nuevo_email = input("Nuevo email: ")
        cursor.execute(
            "UPDATE clientes SET email = %s WHERE id = %s", (nuevo_email, id_cliente))
        print("Email actualizado.")
    except ValueError:
        print("Error en la bd")


def menu_clientes():
    print("Menu Clientes")
    print("1. Agregar cliente")
    print("2. Actualizar cliente")
    print("3, Actualizar email")
    print("4. Eliminar cliente")
    print("5. Consultar cliente")
    print("6. Volver al menu principal")
    print("***********************************")


def menu_ventas():
    print("Menu Ventas")
    print("1. Agregar venta")
    print("2. Actualizar venta")
    print("3. Eliminar venta")
    print("4. Consultar venta")
    print("5. Volver al menu principal")
    print("***********************************")


def menu_detalle_ventas():
    print("Menu Detalle Ventas")
    print("1. Agregar detalle venta")
    print("2. Actualizar detalle venta")
    print("3. Eliminar detalle venta")
    print("4. Consultar detalle venta")
    print("5. Volver al menu principal")
    print("6. ver la tabla de detalle ventas")
    print("***********************************")


def menu_productos():
    print("Menu Productos")
    print("1. Agregar producto")
    print("2. Actualizar producto")
    print("3. Eliminar producto")
    print("4. Consultar producto")
    print("5. Volver al menu principal")
    print("************************************")


def eliminar_cliente(cursor, conexion):
    try:
        id_cliente = input("ID del cliente a eliminar: ")
        cursor.execute(
            "DELETE FROM clientes WHERE id = %s", (id_cliente,))
        conexion.commit()
        print("Cliente eliminado.")
    except ValueError:
        print("Error en la bd")


def menu():
    while True:
        conector = ConectotDB('localhost', 'root', '123456789', 'tiendas')
        conexion = conector.conection
        cursor = conexion.cursor()

        print("***********************************")
        print("********** BIENVENIDO *************")
        print("********** A LA TIENDA  ***********")
        print("***********************************")
        print("0. Ver menu principal")
        print("1. Clientes")
        print("2. Ventas")
        print("3. Detalle Ventas")
        print("4. Productos")
        print("5. Salir")
        print(input("Para ver el menu preciona 0: "))
        opcion = input("Elige una opción: ")
        print("***********************************")
        if opcion == "0":
            continue  # Vuelve a mostrar el menú
        elif opcion == "1":  # Clientes
            menu_clientes()
            opcion_cliente = input("Elige una opción: ")
            if opcion_cliente == "1":
                crear_pedido(cursor, conexion)
            elif opcion_cliente == "2":
                actualizar_cliente(cursor, conexion)
            elif opcion_cliente == "3":
                actualizar_email(cursor, conexion)
            elif opcion_cliente == "4":  # Eliminar cliente
                eliminar_cliente(cursor, conexion)
            elif opcion_cliente == "5":
                try:
                    cursor.execute("SELECT * FROM clientes")
                    result = cursor.fetchall()  # Obtener todos los registros
                # cursor.fetchone() obtiene un solo resultado de la consulta
                    for row in result:
                        print("Cliente:", row)
                except ValueError:
                    print("Error con la bd")
            elif opcion_cliente == "6":
                continue  # Volver al menú principal
        elif opcion == "2":  # Ventas
            menu_ventas()
            opcion_venta = input("Elige una opción: ")
            if opcion_venta == "1":  # Agregar venta
                # input es para ingresar datos
                try:
                    id_cliente = input("ID del cliente: ")
                    fecha = input("Fecha (YYYY-MM-DD): ")
                    cursor.execute(
                        "INSERT INTO ventas (id_cliente, fecha) VALUES (%s, %s)", (id_cliente, fecha))
                    conexion.commit()
                    print("Venta agregada.")
                except ValueError:
                    print("Error en la bd")
            elif opcion_venta == "2":  # Actualizar venta
                try:
                    id_venta = input("ID de la venta a actualizar: ")
                    nueva_fecha = input("Nueva fecha (YYYY-MM-DD): ")
                    cursor.execute(
                        "UPDATE ventas SET fecha = %s WHERE id = %s", (nueva_fecha, id_venta))
                    conexion.commit()
                    print("Venta actualizada.")
                except ValueError:
                    print("Error en la bd")
            elif opcion_venta == "3":  # Eliminar venta
                try:
                    id_venta = input("ID de la venta a eliminar: ")
                    cursor.execute(
                        "DELETE FROM ventas WHERE id = %s", (id_venta,))
                    conexion.commit()
                    print("Venta eliminada.")
                except ValueError:
                    print("Error en la bd")
            elif opcion_cliente == "4":  # Consultar venta
                try:
                    cursor.execute("SELECT * FROM ventas")
                    result = cursor.fetchall()  # Obtener todos los registros
                    # cursor.fetchone() obtiene un solo resultado de la consulta
                    for row in result:
                        print("Ventas:", row)
                except ValueError:
                    print("Error con la bd")
            elif opcion_cliente == "5":
                continue
        elif opcion == "3":  # Detalle Ventas
            menu_detalle_ventas()
            # Aquí puedes agregar lógica similar para detalles de venta
            opcion_cliente = input("Elige una opción: ")
            if opcion_cliente == "1":
                try:
                    nombre = input("Nombre del cliente: ")
                    email = input("Email del cliente: ")
                    cursor.execute(
                        "INSERT INTO clientes (nombre, email) VALUES (%s, %s)", (nombre, email))
                    conexion.commit()  # comando para guardar cambios
                    print("Cliente agregado.")
                except ValueError:
                    print("Error en la bd")
            elif opcion_cliente == "2":
                try:
                    id_cliente = input("ID del cliente a actualizar: ")
                    nuevo_nombre = input("Nuevo nombre: ")
                    cursor.execute(
                        "UPDATE clientes SET nombre = %s WHERE id = %s", (nuevo_nombre, id_cliente))
                    conexion.commit()
                except ValueError:
                    print("Error en la bd")
            # %s se usa para evitar inyecciones SQL
            elif opcion_cliente == "3":
                try:
                    id_cliente = input("ID de de venta a eliminar: ")
                    cursor.execute(
                        "DELETE FROM DetalleVentas WHERE id = %s", (id_cliente,))
                    conexion.commit()
                    print("Cliente eliminado.")
                except ValueError:
                    print("Error en la bd")
            elif opcion_cliente == "4":  # Consultar detalle venta
                try:
                    cursor.execute("SELECT * FROM detallesventa")
                    result = cursor.fetchmany()  # Obtener todos los registros
                    # cursor.fetchone() obtiene un solo resultado de la consulta
                    for row in result:
                        print("Detalle de Ventas:", row)
                except ValueError:
                    print("Error con la bd")
            elif opcion_cliente == "5":
                continue
            elif opcion_cliente == "6":
                try:
                    cursor.execute("SHOW TABLES")
                    print(cursor.fetchmany(
                        kwargs={"table": "DetalleVentas"}))
                except ValueError:
                    print("Error con la bd")
            elif opcion == "4":  # Productos
                menu_productos()
                opcion_cliente = input("Elige una opción: ")
                if opcion_cliente == "1":  # Agregar producto
                    try:
                        nombre_producto = input("Agregar producto: ")
                        nombre_producto = input("nombre del producto: ")
                        precio = input("Precio del producto: ")
                        cursor.execute(
                            "INSERT INTO productos (nombre, precio) VALUES (%s, %s)", (nombre_producto, nombre_producto, precio))
                        conexion.commit()  # comando para guardar cambios
                        print("Producto agregado.")
                    except ValueError:
                        print("Error en la bd")
            elif opcion_cliente == "2":  # Actualizar producto
                try:
                    id_cliente = input("ID del cliente a actualizar: ")
                    nuevo_nombre = input("Nuevo nombre: ")
                    cursor.execute(
                        "UPDATE clientes SET nombre = %s WHERE id = %s", (nuevo_nombre, id_cliente))
                    conexion.commit()
                except ValueError:
                    print("Error en la bd")
            elif opcion_cliente == "3":  # Eliminar producto
                try:
                    id_cliente = input("ID del cliente a eliminar: ")
                    cursor.execute(
                        "DELETE FROM clientes WHERE id = %s", (id_cliente,))
                    conexion.commit()
                    print("Cliente eliminado.")
                except ValueError:
                    print("Error en la bd")
            elif opcion_cliente == "4":  # Consultar producto
                try:
                    cursor.execute("SELECT * FROM Productos")
                    result = cursor.fetchall()  # Obtener todos los registros
                    # cursor.fetchone() obtiene un solo resultado de la consulta
                    for row in result:
                        print("Productos:", row)
                except ValueError:
                    print("Error con la bd")
            elif opcion_cliente == "6":
                continue
            elif opcion == "5":
                print("Gracias por usar el sistema. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")


menu()
