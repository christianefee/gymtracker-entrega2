import numpy as np
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

    def analizar(self, *args) -> str:
        nombre_ejercicio: str = args[0]
        pesos: list = self.obtener_pesos_ejercicio(nombre_ejercicio)

        if len(pesos) < 3:
            return "No hay suficientes sesiones para analizar este ejercicio."

        ultimos_pesos: list = pesos[-3:]
        diferencia: float = float(np.max(ultimos_pesos) - np.min(ultimos_pesos))

        if diferencia == 0:
            return f"Estancamiento detectado en {nombre_ejercicio}. Llevas 3 sesiones sin subir de peso."
        else:
            return f"Sigues progresando en {nombre_ejercicio}. Ultimo peso registrado: {pesos[-1]} kg."


