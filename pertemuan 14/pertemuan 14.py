#1

# Membuat list kosong
belanjaan = []

# Menambahkan item ke dalam list
belanjaan.append("Telur")
belanjaan.append("Susu")
belanjaan.append("Roti")

# Menambahkan "Apel" di posisi paling awal
belanjaan.insert(0, "Apel")

# Menghapus "Susu"
belanjaan.remove("Susu")

# Mencetak list akhir
print(belanjaan)

#2
# Membuat list nilai
nilai = [98, 76, 88, 100, 54]

# Mendapatkan versi terurut dari list
nilai_terurut = sorted(nilai)

# Mencetak list nilai yang asli
print("List nilai yang asli:", nilai)

# Mencetak list baru yang sudah terurut
print("List nilai yang terurut:", nilai_terurut)
#3
# Meminta pengguna memasukkan sebuah kalimat
kalimat = input("Masukkan sebuah kalimat: ")

# Mengubah kalimat menjadi list kata-kata
kata_kata = kalimat.split()

# Menghitung dan mencetak jumlah kata dalam kalimat
jumlah_kata = len(kata_kata)
print("Jumlah kata dalam kalimat:", jumlah_kata)

# Mengurutkan kata-kata berdasarkan abjad
kata_kata.sort()

# Mencetak list yang sudah terurut
print("Kata-kata yang sudah terurut:", kata_kata)
#4
a = [1, 2, 3, 4, 5]
b = a
c = a.copy()
b[1] = 20
c[1] = 30
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")



