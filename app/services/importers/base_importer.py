from abc import ABC, abstractmethod
from time import perf_counter


class BaseImporter(ABC):
    """
    Classe base para todos os importadores do GV Radar.
    """

    def __init__(self):
        self.total = 0
        self.processados = 0
        self.criados = 0
        self.atualizados = 0
        self.ignorados = 0

    @abstractmethod
    def executar(self):
        """
        Método principal do importador.
        """
        pass

    def iniciar(self):
        self._inicio = perf_counter()

    def finalizar(self):
        tempo = perf_counter() - self._inicio

        print()
        print("=" * 60)
        print("Importação concluída")
        print("=" * 60)
        print(f"Processados : {self.processados}")
        print(f"Criados     : {self.criados}")
        print(f"Atualizados : {self.atualizados}")
        print(f"Ignorados   : {self.ignorados}")
        print(f"Tempo       : {tempo:.2f} segundos")