class Warga:
    def menyapa(self):
        print("halo..")

class WargaCibodas(Warga):
    def menyapa(self):
        print("halo saya adalah warga cibodas")

class WargaSukatani(Warga):
    def menyapa(self):
        print("halo saya adalah warga sukatani")


galuh = WargaCibodas()
galuh.menyapa()

ayyash = WargaSukatani()
ayyash.menyapa()