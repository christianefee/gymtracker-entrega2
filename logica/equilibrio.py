from logica.base import AnalizadorBase

class AnalizadorEquilibrio(AnalizadorBase):
    def __init__(self, sesiones_usuario: list) -> None:
        super().__init__(sesiones_usuario)

    def calcular_volumen_por_musculo(self) -> dict:
        volumen_por_musculo: dict = {}
        for sesion in self.sesiones_usuario:
            for ejercicio in sesion["ejercicios"]:
                musculo: str = ejercicio["musculo"]
                volumen: float = ejercicio["peso"] * ejercicio["series"] * ejercicio["repeticiones"]
                if musculo not in volumen_por_musculo:
                    volumen_por_musculo[musculo] = 0.0
                volumen_por_musculo[musculo] += volumen
        return volumen_por_musculo

    def calcular_distribucion(self) -> dict:
        volumen_por_musculo: dict = self.calcular_volumen_por_musculo()
        total: float = sum(volumen_por_musculo.values())
        distribucion: dict = {}
        for musculo, volumen in volumen_por_musculo.items():
            distribucion[musculo] = round((volumen / total) * 100, 1)
        return distribucion

    def detectar_desbalance(self) -> str:
        distribucion: dict = self.calcular_distribucion()
        musculos_bajos: list = []
        for musculo, porcentaje in distribucion.items():
            if porcentaje < 10.0:
                musculos_bajos.append(musculo)
        if len(musculos_bajos) == 0:
            return "No se detectaron desbalances musculares. Distribucion equilibrada."
        else:
            return f"Grupos musculares descuidados: {', '.join(musculos_bajos)}. Se recomienda trabajarlos mas."

    def analizar(self, *args) -> str:
        return self.detectar_desbalance()
