class Warga:
    def __init__(self):
        self.__nik = None

    def set_nik(self, nik):
        self.__nik = nik
   
    def get_nik(self):
        return self.__nik

galuh = Warga()

galuh.set_nik(1234567890)
print(galuh.get_nik())

