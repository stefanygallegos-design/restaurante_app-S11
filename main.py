from servicios.restaurante import Restaurante


def mostrar_menu():
    print("\n" + "=" * 45)
    print("        RESTAURANTE APP - SEMANA 11")
    print("=" * 45)
    print("1. Registrar usuario")
    print("2. Registrar producto")
    print("3. Listar usuarios")
    print("4. Listar productos")
    print("5. Vender producto")
    print("6. Consultar ventas de un usuario")
    print("7. Salir")
    print("=" * 45)


def registrar_usuario(restaurante: Restaurante):
    print("\n--- REGISTRAR USUARIO ---")

    identificacion = input(
        "Ingrese la identificación: "
    ).strip()

    nombre = input(
        "Ingrese el nombre: "
    ).strip()

    try:
        resultado = restaurante.registrar_usuario(
            identificacion,
            nombre
        )

        if resultado:
            print("Usuario registrado correctamente.")
        else:
            print("El usuario ya existe.")

    except ValueError as error:
        print(f"Error: {error}")


def registrar_producto(restaurante: Restaurante):
    print("\n--- REGISTRAR PRODUCTO ---")

    codigo = input(
        "Ingrese el código del producto: "
    ).strip()

    nombre = input(
        "Ingrese el nombre del producto: "
    ).strip()

    try:
        precio = float(
            input("Ingrese el precio: ")
        )

        stock = int(
            input("Ingrese el stock: ")
        )

        resultado = restaurante.registrar_producto(
            codigo,
            nombre,
            precio,
            stock
        )

        if resultado:
            print("Producto registrado correctamente.")
        else:
            print("El producto ya existe.")

    except ValueError as error:
        print(f"Error: {error}")


def listar_usuarios(restaurante: Restaurante):
    print("\n--- USUARIOS REGISTRADOS ---")

    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print("No existen usuarios registrados.")
        return

    for usuario in usuarios:
        print(
            f"ID: {usuario.identificacion} | "
            f"Nombre: {usuario.nombre}"
        )


def listar_productos(restaurante: Restaurante):
    print("\n--- PRODUCTOS REGISTRADOS ---")

    productos = restaurante.listar_productos()

    if not productos:
        print("No existen productos registrados.")
        return

    for producto in productos:
        print(
            f"Código: {producto.codigo} | "
            f"Nombre: {producto.nombre} | "
            f"Precio: ${producto.precio:.2f} | "
            f"Stock: {producto.stock}"
        )


def vender_producto(restaurante: Restaurante):
    print("\n--- VENDER PRODUCTO ---")

    identificacion = input(
        "Ingrese la identificación del usuario: "
    ).strip()

    codigo = input(
        "Ingrese el código del producto: "
    ).strip()

    try:
        cantidad = int(
            input("Ingrese la cantidad: ")
        )

        usuario = restaurante.buscar_usuario(
            identificacion
        )

        producto = restaurante.buscar_producto(
            codigo
        )

        if usuario is None:
            print("Error: el usuario no existe.")
            return

        if producto is None:
            print("Error: el producto no existe.")
            return

        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor que cero.")
            return

        if producto.stock < cantidad:
            print(
                f"Stock insuficiente. "
                f"Stock disponible: {producto.stock}"
            )
            return

        resultado = restaurante.vender_producto(
            codigo,
            identificacion,
            cantidad
        )

        if resultado:
            print("Venta registrada correctamente.")
            print(
                f"Nuevo stock de {producto.nombre}: "
                f"{producto.stock}"
            )
        else:
            print("No fue posible realizar la venta.")

    except ValueError as error:
        print(f"Error: {error}")


def consultar_ventas_usuario(restaurante: Restaurante):
    print("\n--- CONSULTAR VENTAS DE UN USUARIO ---")

    identificacion = input(
        "Ingrese la identificación del usuario: "
    ).strip()

    usuario = restaurante.buscar_usuario(
        identificacion
    )

    if usuario is None:
        print("El usuario no existe.")
        return

    ventas = restaurante.consultar_ventas_usuario(
        identificacion
    )

    if not ventas:
        print("El usuario no tiene ventas registradas.")
        return

    print(
        f"\nVentas realizadas por "
        f"{usuario.nombre}:"
    )

    for venta in ventas:
        producto = restaurante.buscar_producto(
            venta.producto_codigo
        )

        if producto is not None:
            print(
                f"- Producto: {producto.nombre} | "
                f"Código: {venta.producto_codigo} | "
                f"Cantidad: {venta.cantidad}"
            )
        else:
            print(
                f"- Código: {venta.producto_codigo} | "
                f"Cantidad: {venta.cantidad}"
            )


def main():
    restaurante = Restaurante()

    while True:
        mostrar_menu()

        opcion = input(
            "Seleccione una opción: "
        ).strip()

        if opcion == "1":
            registrar_usuario(restaurante)

        elif opcion == "2":
            registrar_producto(restaurante)

        elif opcion == "3":
            listar_usuarios(restaurante)

        elif opcion == "4":
            listar_productos(restaurante)

        elif opcion == "5":
            vender_producto(restaurante)

        elif opcion == "6":
            consultar_ventas_usuario(restaurante)

        elif opcion == "7":
            print("\nPrograma finalizado.")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
