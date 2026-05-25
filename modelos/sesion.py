from dataclasses import dataclass, field
from modelos.ejercicio import Ejercicio

@dataclass
class Sesion:
    nombre: str
    fecha: str
    ejercicios: list = field(default_factory=list)

    def agregar_ejercicio(self, ejercicio: Ejercicio) -> None:
        self.ejercicios.append(ejercicio)

    def calcular_volumen_total(self) -> float:
        total: float = 0
        for ejercicio in self.ejercicios:
            total += ejercicio.calcular_volumen()
        return total
