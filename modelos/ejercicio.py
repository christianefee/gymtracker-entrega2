from dataclasses import dataclass

@dataclass
class Ejercicio:
    nombre: str
    musculo: str
    peso: float
    series: int
    repeticiones: int

    def calcular_volumen(self) -> float:
        return self.peso * self.series * self.repeticiones
