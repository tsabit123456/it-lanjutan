class kuda:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

    def bersuara(self):
        print("Meow!")

    def perkenalkan_diri(self):
        print(f"Halo, saya kucing bernama {self.nama} dan warna saya {self.warna}.")

# Membuat dua objek dari class Kucing
kucing1 = Kucing("Oren", "Oranye")
kuda2 = kuda("Milo", "Coklat")

# Memanggil method perkenalkan_diri() dan bersuara() dari kedua objek
kucing1.perkenalkan_diri()
kucing1.bersuara()

kuda2.perkenalkan_diri()
kucing2.bersuara()
