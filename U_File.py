from tabulate import tabulate
import os

class Mahasiswa:
    def __init__(self, nim, nama, nilai):
        self.nim = nim
        self.nama = nama
        self.nilai = nilai

class PengelolaDataMahasiswa:
    def __init__(self):
        self.data_mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.data_mahasiswa.append(mahasiswa)
        print("Mahasiswa berhasil ditambahkan.")

    def hapus_mahasiswa(self, nim):
        for mhs in self.data_mahasiswa:
            if mhs.nim == nim:
                self.data_mahasiswa.remove(mhs)
                print("Mahasiswa dengan NIM {} berhasil dihapus.".format(nim))
                return
        print("Mahasiswa dengan NIM {} tidak ditemukan.".format(nim))

    def tampilkan_mahasiswa(self):
        if not self.data_mahasiswa:
            print("Belum ada data mahasiswa.")
        else:
            table = [["NIM", "Nama Mahasiswa", "Nilai"]]
            for mhs in self.data_mahasiswa:
                table.append([mhs.nim, mhs.nama, mhs.nilai])
            print(tabulate(table, headers="firstrow", tablefmt="grid"))

    def cari_mahasiswa(self, nim):
        for mhs in self.data_mahasiswa:
            if mhs.nim == nim:
                print("Mahasiswa ditemukan:")
                print("NIM:", mhs.nim)
                print("Nama Mahasiswa:", mhs.nama)
                print("Nilai:", mhs.nilai)
                return
        print("Mahasiswa dengan NIM {} tidak ditemukan.".format(nim))

    def perbaiki_mahasiswa(self, nim, nama, nilai):
        for mhs in self.data_mahasiswa:
            if mhs.nim == nim:
                mhs.nama = nama
                mhs.nilai = nilai
                print("Data mahasiswa berhasil diperbarui.")
                return
        print("Mahasiswa dengan NIM {} tidak ditemukan.".format(nim))

    def menu_pengelola_mahasiswa(self):
        pengelola = PengelolaDataMahasiswa()
        
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nMenu:")
            print("1. Tambah Mahasiswa")
            print("2. Hapus Mahasiswa")
            print("3. Tampilkan Data Mahasiswa")
            print("4. Cari Data Mahasiswa")
            print("5. Perbaiki Data Mahasiswa")
            print("6. Kembali")

            pilihan = input("Masukkan pilihan Anda: ")

            if pilihan == '1':
                nim = input("Masukkan NIM mahasiswa: ")
                nama = input("Masukkan nama mahasiswa: ")
                nilai = input("Masukkan nilai mahasiswa: ")
                mahasiswa_baru = Mahasiswa(nim, nama, nilai)
                pengelola.tambah_mahasiswa(mahasiswa_baru)
                input()
                
            elif pilihan == '2':
                nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
                pengelola.hapus_mahasiswa(nim)
                input()
                
            elif pilihan == '3':
                pengelola.tampilkan_mahasiswa()
                input()
                
            elif pilihan == '4':
                nim = input("Masukkan NIM mahasiswa yang ingin dicari: ")
                pengelola.cari_mahasiswa(nim)
                input()
                
            elif pilihan == '5':
                nim = input("Masukkan NIM mahasiswa yang ingin diperbaiki: ")
                nama = input("Masukkan nama baru: ")
                nilai = input("Masukkan nilai baru: ")
                pengelola.perbaiki_mahasiswa(nim, nama, nilai)
                input()
            
            elif pilihan == '6':
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
