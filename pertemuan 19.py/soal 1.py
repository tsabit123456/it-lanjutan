import re

data = "Pendapatan bulan ini adalah Rp 1,500,000, sedangkan pengeluaran sebesar Rp 850,000."
angka = re.findall(r'\d+', data.replace(',', ''))
print(angka)  # Output: ['1', '500', '000', '850', '000']
