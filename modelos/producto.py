class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):
        if not codigo.strip():
            raise ValueError("El código del producto no puede estar vacío.")

        if not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")

        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if cantidad > self.stock:
            raise ValueError("No existe stock suficiente.")

        self.stock -= cantidad

    def a_diccionario(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

    @classmethod
    def desde_diccionario(cls, datos: dict):
        try:
            return cls(
                datos["codigo"],
                datos["nombre"],
                float(datos["precio"]),
                int(datos["stock"])
            )
        except KeyError as error:
            raise KeyError(
                f"Falta la clave {error.args[0]} en el producto."
            )
