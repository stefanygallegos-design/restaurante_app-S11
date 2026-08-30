class Venta:
    def __init__(
        self,
        usuario_id: str,
        producto_codigo: str,
        cantidad: int
    ):
        if not usuario_id.strip():
            raise ValueError("La identificación del usuario no puede estar vacía.")

        if not producto_codigo.strip():
            raise ValueError("El código del producto no puede estar vacío.")

        if cantidad <= 0:
            raise ValueError("La cantidad vendida debe ser mayor que cero.")

        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad

    def a_diccionario(self) -> dict:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad
        }

    @classmethod
    def desde_diccionario(cls, datos: dict):
        try:
            return cls(
                datos["usuario_id"],
                datos["producto_codigo"],
                int(datos["cantidad"])
            )
        except KeyError as error:
            raise KeyError(
                f"Falta la clave {error.args[0]} en la venta."
            )
