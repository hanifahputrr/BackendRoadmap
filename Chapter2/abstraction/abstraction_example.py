from abc import ABC, abstractmethod

class Warga(ABC):
    @abstractmethod
    def menyapa(self):
        pass

class WargaCibodas(Warga):
    def menyapa(self):
        print("halo halo cibodas")

asep = WargaCibodas()
asep.menyapa()

