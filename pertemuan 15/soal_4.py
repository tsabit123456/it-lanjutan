
# Meminta pengguna memasukkan sebuah kalimat
kalimat = input("Masukkan sebuah kalimat: ")

# Membuat histogram (dalam bentuk dictionary) yang menghitung frekuensi setiap kata
kata_list = kalimat.lower().split()  # Mengubah kalimat menjadi lowercase dan memisahkan kata
histogram = {}

for kata in kata_list:
    if kata in histogram:
        histogram[kata] += 1
    else:
        histogram[kata] = 1

# Mencetak dictionary histogram tersebut
print(histogram)
