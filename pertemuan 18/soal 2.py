class RekeningBank:
    def __init__(self, nomor_rekening, nama_pemilik):
        self.nomor_rekening = nomor_rekening
        self.nama_pemilik = nama_pemilik
        self.saldo = 0

    def lihat_saldo(self):
        print(f"Saldo saat ini: {self.saldo}")

    def setor(self, jumlah):
        self.saldo += jumlah
        print(f"Setor {jumlah}. Saldo sekarang: {self.saldo}")

    def tarik(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak mencukupi")
        else:
            self.saldo -= jumlah
            print(f"Tarik {jumlah}. Saldo sekarang: {self.saldo}")

# Membuat objek rekening_tsabit
rekening_tsabit = RekeningBank("123456789", "Tsabit")

# Memanggil semua method
rekening_tsabit.setor(1000)
rekening_tsabit.lihat_saldo()
rekening_tsabit.tarik(500)
rekening_tsabit.lihat_saldo()
rekening_tsabit.tarik(600)  # Ini akan menampilkan pesan saldo tidak mencukupi
