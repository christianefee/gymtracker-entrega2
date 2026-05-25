from logica.base import AnalizadorBase

class AnalizadorProgreso(AnalizadorBase):
    def __init__(self, sesiones_usuario: list) -> None:
        super().__init__(sesiones_usuario)

    def obtener_pesos_ejercicio(self, nombre_ejercicio: str) -> list:
        pesos: list = []
        for sesion in self.sesiones_usuario:
            for ejercicio in sesion["ejercicios"]:
                if ejercicio["nombre"] == nombre_ejercicio:
                    pesos.append(ejercicio["peso"])
        return pesos

