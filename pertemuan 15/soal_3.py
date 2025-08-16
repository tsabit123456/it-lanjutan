from soal_1 import biodata

# Akses key "pekerjaan" menggunakan .get()
pekerjaan = biodata.get("pekerjaan")
print(pekerjaan)  # None

# Akses key "pekerjaan" dengan nilai default
pekerjaan_default = biodata.get("pekerjaan", "Pelajar")
print(pekerjaan_default)  # Pelajar


