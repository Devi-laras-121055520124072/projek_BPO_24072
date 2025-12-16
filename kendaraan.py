class Kendaraan:
    def _init_(self, plat, merk):
        self.plat = plat
        self.merk = merk

    def info(self):
        return f"Plat: {self.plat}, Merk: {self.merk}"


class Mobil(Kendaraan):
    def _init_(self, plat, merk, jumlah_pintu):
        super()._init_(plat, merk)
        self.jumlah_pintu = jumlah_pintu

    def info(self):
        return f"[Mobil] {super().info()}, Pintu: {self.jumlah_pintu}"


class Motor(Kendaraan):
    def _init_(self, plat, merk, jenis):
        super()._init_(plat, merk)
        self.jenis = jenis

    def info(self):
        return f"[Motor] {super().info()}, Jenis: {self.jenis}"
