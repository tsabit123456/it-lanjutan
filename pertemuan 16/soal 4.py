# Membaca file dan menghitung frekuensi hari
filename = 'mbox-short.txt'
hari_frekuensi = {}

with open(filename, 'r') as file:
    for line in file:
        if line.startswith("From "):
            kata = line.split()
            hari = kata[2]  # Kata ketiga adalah hari
            if hari in hari_frekuensi:
                hari_frekuensi[hari] += 1
            else:
                hari_frekuensi[hari] = 1

# Mencetak dictionary hasil
print(hari_frekuensi)
