class Hotel:
    def __init__(self, nama, jumlah_kamar):
        self.nama = nama
        self.jumlah_kamar = jumlah_kamar
        self.kamar_terpesan = 0
        self.daftar_reservasi = {}

    def tampilkan_info(self):
        print(f"Hotel {self.nama} memiliki {self.jumlah_kamar} kamar.")
        print(f"Jumlah kamar yang sudah terpesan: {self.kamar_terpesan}")
        print(f"Sisa kamar yang tersedia: {self.jumlah_kamar - self.kamar_terpesan}")

    def lakukan_reservasi(self, nama_pelanggan, jumlah_kamar):
        if jumlah_kamar <= 0:
            print("Jumlah kamar yang dipesan harus lebih besar dari 0.")
            return
        if self.kamar_terpesan + jumlah_kamar > self.jumlah_kamar:
            print("Maaf, kamar tidak cukup tersedia.")
            return
        self.kamar_terpesan += jumlah_kamar
        self.daftar_reservasi[nama_pelanggan] = jumlah_kamar
        print(f"Reservasi berhasil untuk {nama_pelanggan} dengan {jumlah_kamar} kamar.")

    def tampilkan_reservasi(self):
        if not self.daftar_reservasi:
            print("Tidak ada reservasi yang terdaftar.")
        else:
            print("Daftar Reservasi:")
            for pelanggan, kamar in self.daftar_reservasi.items():
                print(f"{pelanggan}: {kamar} kamar")

    def batalkan_reservasi(self, nama_pelanggan):
        if nama_pelanggan in self.daftar_reservasi:
            self.kamar_terpesan -= self.daftar_reservasi[nama_pelanggan]
            del self.daftar_reservasi[nama_pelanggan]
            print(f"Reservasi untuk {nama_pelanggan} berhasil dibatalkan.")
        else:
            print(f"Tidak ada reservasi atas nama {nama_pelanggan}.")

# Contoh penggunaan
hotel = Hotel("Hotel Sejahtera", 10)

while True:
    print("\nMenu:")
    print("1. Tampilkan Info Hotel")
    print("2. Lakukan Reservasi")
    print("3. Tampilkan Reservasi")
    print("4. Batalkan Reservasi")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1-5): ")
    
    if pilihan == '1':
        hotel.tampilkan_info()
    elif pilihan == '2':
        nama = input("Nama pelanggan: ")
        jumlah = int(input("Jumlah kamar yang dipesan: "))
        hotel.lakukan_reservasi(nama, jumlah)
    elif pilihan == '3':
        hotel.tampilkan_reservasi()
    elif pilihan == '4':
        nama = input("Nama pelanggan yang ingin dibatalkan reservasinya: ")
        hotel.batalkan_reservasi(nama)
    elif pilihan == '5':
        print("Terima kasih telah menggunakan sistem manajemen hotel!")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
