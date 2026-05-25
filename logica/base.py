from abc import ABC, abstractmethod

class AnalizadorBase(ABC):
    def __init__(self, sesiones_usuario: list) -> None:
        self.sesiones_usuario: list = sesiones_usuario

    @abstractmethod
    def analizar(self, *args) -> str:
        pass
