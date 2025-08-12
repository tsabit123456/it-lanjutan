#1
# Membuat list jadwal_senin
jadwal_senin = ["Matematika", "Bahasa Indonesia", "Olahraga", "Sejarah"]

# Cetak seluruh list
print(jadwal_senin)

# Cetak hanya mata pelajaran pertama
print(jadwal_senin[0])

# Cetak mata pelajaran terakhir menggunakan indeks negatif
print(jadwal_senin[-1])

#2
# Mengubah elemen "Olahraga" menjadi "Kimia"
jadwal_senin[2] = "Kimia"

# Cetak list jadwal_senin yang sudah diperbarui
print(jadwal_senin)
#3
# Membuat list nilai_mentah
nilai_mentah = [55, 63, 72, 81, 90]

# Menggunakan for loop untuk menambahkan 5 poin ke setiap nilai
for i in range(len(nilai_mentah)):
    nilai_mentah[i] += 5  # Menambahkan nilai bonus

# Cetak list nilai_mentah yang sudah berisi nilai-nilai baru
print(nilai_mentah)
#4
# Membuat dua buah list
awal_minggu = ["Senin", "Selasa", "Rabu"]
akhir_minggu = ["Kamis", "Jumat", "Sabtu", "Minggu"]

# Menggabungkan kedua list menjadi list baru bernama seminggu
seminggu = awal_minggu + akhir_minggu

# Menggunakan slicing untuk membuat list baru bernama hari_kerja
hari_kerja = seminggu[:5]  # Hanya mengambil hari Senin sampai Jumat

# Cetak list hari_kerja
print(hari_kerja)
