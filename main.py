from kendaraan import Mobil, Motor
from data import tambah_kendaraan, tampilkan_kendaraan

while True:
    print("\n=== SISTEM DATA KENDARAAN ===")
    print("1. Tambah Mobil")
    print("2. Tambah Motor")
    print("3. Tampilkan Data Kendaraan")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        plat = input("Masukkan plat nomor: ")
        merk = input("Masukkan merk mobil: ")
        pintu = input("Masukkan jumlah pintu: ")
        mobil = Mobil(plat, merk, pintu)
        tambah_kendaraan(mobil)
        print("Data mobil berhasil ditambahkan")

    elif pilihan == "2":
        plat = input("Masukkan plat nomor: ")
        merk = input("Masukkan merk motor: ")
        jenis = input("Masukkan jenis motor: ")
        motor = Motor(plat, merk, jenis)
        tambah_kendaraan(motor)
        print("Data motor berhasil ditambahkan")

    elif pilihan == "3":
        tampilkan_kendaraan()

    elif pilihan == "4":
        print("Terima kasih, program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
