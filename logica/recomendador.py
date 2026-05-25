from logica.base import AnalizadorBase
from modelos.ejercicios import EJERCICIOS

class Recomendador(AnalizadorBase):
    def __init__(self, sesiones_usuario: list, peso_usuario: float, nivel: str) -> None:
        super().__init__(sesiones_usuario)
        self.peso_usuario: float = peso_usuario
        self.nivel: str = nivel

    def obtener_pesos_ejercicio(self, nombre_ejercicio: str) -> list:
        pesos: list = []
        for sesion in self.sesiones_usuario:
            for ejercicio in sesion["ejercicios"]:
                if ejercicio["nombre"] == nombre_ejercicio:
                    pesos.append(ejercicio["peso"])
        return pesos
