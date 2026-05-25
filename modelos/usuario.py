from dataclasses import dataclass, field

@dataclass
class Usuario:
    nombre: str
    edad: int
    peso: float
    altura: float
    nivel: str = "principiante"
    historial: str = field(default_factory=list)