def buat_laporan(data):
    """Fungsi untuk memproses dan menampilkan laporan penjualan."""
    print("\n" + "="*45)
    print("            LAPORAN PENJUALAN            ")
    print("="*45)
    
    if not data:
        print("Belum ada data penjualan yang dimasukkan.")
        print("="*45)
        return
        
    total_pendapatan = 0
    print(f"{'No':<3} | {'Nama Barang':<15} | {'Qty':<5} | {'Total (Rp)':<12}")
    print("-" * 45)
    
    for idx, item in enumerate(data, 1):
        print(f"{idx:<3} | {item['nama']:<15} | {item['jumlah']:<5} | Rp {item['total']:,.0f}")
        total_pendapatan += item['total']
        
    print("-" * 45)
    print(f"TOTAL PENDAPATAN : Rp {total_pendapatan:,.0f}")
    print("="*45)
