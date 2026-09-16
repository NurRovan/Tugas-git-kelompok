print("SISTEM TOKO UTAMA - Versi Anggota A")
from input_data import input_data
from laporan import buat_laporan

def main():
    data_penjualan = input_data()
    buat_laporan(data_penjualan)

if __name__ == "__main__":
    main()
