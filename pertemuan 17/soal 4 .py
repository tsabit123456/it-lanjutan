# Membuat dictionary papan_catur
papan_catur = {}

# Mengisi beberapa posisi
papan_catur[(1, 'a')] = "Benteng Putih"
papan_catur[(8, 'h')] = "Benteng Hitam"
papan_catur[(1, 'b')] = "Kuda Putih"
papan_catur[(8, 'g')] = "Kuda Hitam"

# Mengakses dan mencetak bidak yang ada di posisi (1, 'a')
bidak_posisi = papan_catur[(1, 'a')]
print("Bidak di posisi (1, 'a'):", bidak_posisi)
