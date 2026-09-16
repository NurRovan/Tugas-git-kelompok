def input_data():
    """Fungsi untuk menerima input data penjualan dari pengguna."""
    data = []
    print("=== INPUT DATA PENJUALAN ===")
    try:
        n = int(input("Masukkan jumlah jenis barang: "))
        for i in range(n):
            print(f"\nData Barang ke-{i+1}:")
            nama = input("  Nama Barang  : ")
            harga = float(input("  Harga Satuan : Rp "))
            jumlah = int(input("  Jumlah Terjual: "))
            
            total = harga * jumlah
            data.append({
                "nama": nama,
                "harga": harga,
                "jumlah": jumlah,
                "total": total
            })
    except ValueError:
        print("Input tidak valid! Pastikan harga dan jumlah berupa angka.")
    
    return data
