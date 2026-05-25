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

    def calcular_peso_objetivo(self, nombre_ejercicio: str) -> float:
        if nombre_ejercicio not in EJERCICIOS:
            return 0.0
        multiplicadores: tuple = EJERCICIOS[nombre_ejercicio]
        if self.nivel == "principiante":
            return self.peso_usuario * multiplicadores[1]
        elif self.nivel == "promedio":
            return self.peso_usuario * multiplicadores[2]
        else:
            return self.peso_usuario * multiplicadores[3]

    def analizar(self, *args) -> str:
        nombre_ejercicio: str = args[0]
        pesos: list = self.obtener_pesos_ejercicio(nombre_ejercicio)

        if len(pesos) < 3:
            return "No hay suficientes sesiones para generar una recomendacion."

        peso_actual: float = pesos[-1]
        peso_objetivo: float = self.calcular_peso_objetivo(nombre_ejercicio)
        ultimos_pesos: list = pesos[-3:]
        todos_iguales: bool = len(set(ultimos_pesos)) == 1

        if peso_actual >= peso_objetivo:
            return f"Excelente nivel en {nombre_ejercicio}. Estas en tu peso objetivo o por encima ({peso_actual} kg)."
        elif todos_iguales:
            nuevo_peso: float = peso_actual + 2.5
            return f"Llevas 3 sesiones con el mismo peso en {nombre_ejercicio}. Intenta subir a {nuevo_peso} kg."
        else:
            diferencia: float = round(peso_objetivo - peso_actual, 1)
            return f"Vas bien en {nombre_ejercicio}. Te faltan {diferencia} kg para alcanzar tu peso objetivo ({peso_objetivo} kg)."

