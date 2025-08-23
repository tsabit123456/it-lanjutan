import re

nomor_telepon = input("Masukkan nomor telepon: ")
if re.search(r'^\d{10,13}$', nomor_telepon):
    print("Format nomor telepon valid.")
else:
    print("Format tidak valid.")
