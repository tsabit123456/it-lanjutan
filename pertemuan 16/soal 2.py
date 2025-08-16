kontak = {}

# Menambahkan kontak
kontak["Ibu"] = "081234567890"
kontak["Ayah"] = "081234567891"
kontak["Teman"] = "081234567892"

# Mengubah nomor telepon "Ibu"
kontak["Ibu"] = "089876543210"

# Menghapus "Teman"
kontak.pop("Teman")

# Mencetak dictionary kontak akhir
print(kontak)
