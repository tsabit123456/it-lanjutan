produk = {
    "PROD001": {"nama": "Laptop", "harga": 15000000, "stok": 10},
    "PROD002": {"nama": "Smartphone", "harga": 5000000, "stok": 20}
}

# Mencetak nama dan harga dari produk dengan ID "PROD002"
produk_id = "PROD002"
print(f"Nama: {produk[produk_id]['nama']}, Harga: Rp {produk[produk_id]['harga']}")
