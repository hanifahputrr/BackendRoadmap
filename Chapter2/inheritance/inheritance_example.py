class Warga:
    def __init__(self, nik):
        self.nik = nik

    def menyapa(self):
        print("halo..")

class WargaCibodas(Warga):
    def __init__(self, nik):
        super().__init__(nik)

galuh = WargaCibodas(1234567890)
print(galuh.nik)