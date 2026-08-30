import json
from pathlib import Path


class ArchivoServicio:
    def __init__(self, carpeta_datos: str = "datos"):
        self.carpeta_datos = Path(carpeta_datos)
        self.carpeta_datos.mkdir(parents=True, exist_ok=True)

    def guardar(self, nombre_archivo: str, datos: list) -> None:
        ruta = self.carpeta_datos / nombre_archivo

        try:
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )
        except PermissionError:
            raise PermissionError(
                f"No existen permisos para escribir en {ruta}."
            )

    def cargar(self, nombre_archivo: str) -> list:
        ruta = self.carpeta_datos / nombre_archivo

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

                if not isinstance(datos, list):
                    raise ValueError(
                        f"El archivo {nombre_archivo} debe contener una lista."
                    )

                return datos

        except FileNotFoundError:
            return []

        except json.JSONDecodeError as error:
            raise ValueError(
                f"El archivo {nombre_archivo} contiene JSON inválido."
            ) from error

        except PermissionError:
            raise PermissionError(
                f"No existen permisos para leer {ruta}."
            )
