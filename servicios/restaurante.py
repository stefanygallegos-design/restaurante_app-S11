from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class Restaurante:
    def __init__(self):
        self.archivo_servicio = ArchivoServicio()

        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []
        self.ventas: list[Venta] = []

        self.cargar_datos()

    # ---------------------------------------------------------
    # PRODUCTOS
    # ---------------------------------------------------------

    def buscar_producto(self, codigo: str):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto

        return None

    def registrar_producto(
        self,
        codigo: str,
        nombre: str,
        precio: float,
        stock: int
    ) -> bool:

        if self.buscar_producto(codigo) is not None:
            return False

        producto = Producto(
            codigo,
            nombre,
            precio,
            stock
        )

        self.productos.append(producto)
        self.guardar_productos()

        return True

    def listar_productos(self) -> list[Producto]:
        return self.productos

    # ---------------------------------------------------------
    # USUARIOS
    # ---------------------------------------------------------

    def buscar_usuario(self, identificacion: str):
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return usuario

        return None

    def registrar_usuario(
        self,
        identificacion: str,
        nombre: str
    ) -> bool:

        if self.buscar_usuario(identificacion) is not None:
            return False

        usuario = Usuario(
            identificacion,
            nombre
        )

        self.usuarios.append(usuario)
        self.guardar_usuarios()

        return True

    def listar_usuarios(self) -> list[Usuario]:
        return self.usuarios

    # ---------------------------------------------------------
    # VENTAS
    # ---------------------------------------------------------

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int
    ) -> bool:

        usuario = self.buscar_usuario(
            identificacion_usuario
        )

        producto = self.buscar_producto(
            codigo_producto
        )

        # Validar usuario y producto
        if usuario is None:
            return False

        if producto is None:
            return False

        # Validar cantidad
        if cantidad <= 0:
            return False

        # Validar stock
        if producto.stock < cantidad:
            return False

        # Crear la venta
        venta = Venta(
            usuario.identificacion,
            producto.codigo,
            cantidad
        )

        # Agregar venta a la colección
        self.ventas.append(venta)

        # Disminuir stock
        producto.vender(cantidad)

        # Guardar los cambios
        self.guardar_ventas()
        self.guardar_productos()

        return True

    # ---------------------------------------------------------
    # CONSULTAR VENTAS POR USUARIO
    # ---------------------------------------------------------

    def consultar_ventas_usuario(
        self,
        identificacion_usuario: str
    ) -> list[Venta]:

        ventas_usuario: list[Venta] = []

        for venta in self.ventas:
            if venta.usuario_id == identificacion_usuario:
                ventas_usuario.append(venta)

        return ventas_usuario

    # ---------------------------------------------------------
    # PERSISTENCIA
    # ---------------------------------------------------------

    def guardar_productos(self) -> None:
        datos = [
            producto.a_diccionario()
            for producto in self.productos
        ]

        self.archivo_servicio.guardar(
            "productos.json",
            datos
        )

    def guardar_usuarios(self) -> None:
        datos = [
            usuario.a_diccionario()
            for usuario in self.usuarios
        ]

        self.archivo_servicio.guardar(
            "usuarios.json",
            datos
        )

    def guardar_ventas(self) -> None:
        datos = [
            venta.a_diccionario()
            for venta in self.ventas
        ]

        self.archivo_servicio.guardar(
            "ventas.json",
            datos
        )

    # ---------------------------------------------------------
    # CARGAR DATOS
    # ---------------------------------------------------------

    def cargar_datos(self) -> None:
        self.cargar_productos()
        self.cargar_usuarios()
        self.cargar_ventas()

    def cargar_productos(self) -> None:
        datos = self.archivo_servicio.cargar(
            "productos.json"
        )

        self.productos = []

        for dato in datos:
            try:
                producto = Producto.desde_diccionario(dato)
                self.productos.append(producto)

            except (KeyError, ValueError) as error:
                print(
                    f"Advertencia: no se pudo cargar un producto: {error}"
                )

    def cargar_usuarios(self) -> None:
        datos = self.archivo_servicio.cargar(
            "usuarios.json"
        )

        self.usuarios = []

        for dato in datos:
            try:
                usuario = Usuario.desde_diccionario(dato)
                self.usuarios.append(usuario)

            except (KeyError, ValueError) as error:
                print(
                    f"Advertencia: no se pudo cargar un usuario: {error}"
                )

    def cargar_ventas(self) -> None:
        datos = self.archivo_servicio.cargar(
            "ventas.json"
        )

        self.ventas = []

        for dato in datos:
            try:
                venta = Venta.desde_diccionario(dato)
                self.ventas.append(venta)

            except (KeyError, ValueError) as error:
                print(
                    f"Advertencia: no se pudo cargar una venta: {error}"
                )
