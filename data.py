data_kendaraan = []

def tambah_kendaraan(kendaraan):
    data_kendaraan.append(kendaraan)

def tampilkan_kendaraan():
    if not data_kendaraan:
        print("Data kendaraan masih kosong")
    else:
        for i, k in enumerate(data_kendaraan, start=1):
            print(f"{i}. {k.info()}")
