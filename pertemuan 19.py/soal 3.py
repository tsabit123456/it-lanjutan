import re

teks = "python adalah bahasa yang menyenangkan, python mudah dipelajari."

# Menggunakan re.search()
hasil_search = re.search('python', teks)
if hasil_search:
    print(hasil_search.group())  # Output: python

# Menggunakan re.findall()
hasil_findall = re.findall('python', teks)
print(hasil_findall)  # Output: ['python', 'python']

# Penjelasan perbedaan output
# re.search() mengembalikan objek match pertama yang ditemukan, 
# sedangkan re.findall() mengembalikan semua kemunculan yang ditemukan dalam bentuk list.
