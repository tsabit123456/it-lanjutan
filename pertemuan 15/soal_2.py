# soal_2.py
# Import dictionary biodata dari soal_1.py
from soal_1 import biodata

# Menambahkan key-value baru
biodata["kota"] = "Jakarta"

# Mengubah umur jadi tahun depan
biodata["umur"] += 1

# Cetak hasil akhir
print("Biodata setelah diperbarui:", biodata)

