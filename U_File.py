from tabulate import tabulate
import os
import string
import pandas as pd
import random

class Mahasiswa:
    def __init__(self, nim, nama, nilai):
        self.nim = nim
        self.nama = nama
        self.nilai = nilai

class PengelolaDataMahasiswa:
    def __init__(self):
        self.data_mahasiswa = []
        self.load_data()  # Memuat data saat objek PengelolaDataMahasiswa dibuat

    # Fungsi untuk memuat data dari file jika ada
    def load_data(self):
        # Cek apakah ada file .xlsx yang tersedia
        if os.path.exists("data_mahasiswa.xlsx"):
            self.load_excel_data("data_mahasiswa.xlsx")
        else:
            input("Tidak ada file data mahasiswa yang ditemukan.")

    # Fungsi untuk memuat data dari file Excel (.xlsx)
    def load_excel_data(self, file_name):
        df = pd.read_excel(file_name)
        for index, row in df.iterrows():
            self.data_mahasiswa.append(Mahasiswa(row['NIM'], row['NAMA'], row['NILAI']))
        input("Load Success from Excel!!!")
        
#---------------DEFINE TAMBAH MAHASISWA--------------------------------
    def tambah_mahasiswa(self, nim, nama, nilai):
        mahasiswa_baru = Mahasiswa(nim, nama, nilai)
        self.data_mahasiswa.append(mahasiswa_baru)
#----------------------------------------------------------------------

#----------------------DEFINE HAPUS MAHASISWA--------------------------
    def hapus_mahasiswa(self, nim):
        for mhs in self.data_mahasiswa:
            if mhs.nim == nim:
                self.data_mahasiswa.remove(mhs)
                print("Mahasiswa dengan NIM {} berhasil dihapus.".format(nim))
                return
        print("Mahasiswa dengan NIM {} tidak ditemukan.".format(nim))
#----------------------------------------------------------------------        
        
#---------------------DEFINE MENAMPILKAN-------------------------------
    def tampilkan_mahasiswa(self):
        if not self.data_mahasiswa:
            print("Belum ada data mahasiswa.")
        else:
            table = [["NIM", "Nama Mahasiswa", "Nilai"]]
            for mhs in self.data_mahasiswa:
                table.append([mhs.nim, mhs.nama, mhs.nilai])
            print(tabulate(table, headers="firstrow", tablefmt="grid"))
#----------------------------------------------------------------------

#--------------------DEFINE SEARCHING----------------------------------------
    def cari_mahasiswa(self, nim):
        for mhs in self.data_mahasiswa:
            if mhs.nim == nim:
                print("Mahasiswa ditemukan:")
                print("NIM:", mhs.nim)
                print("Nama Mahasiswa:", mhs.nama)
                print("Nilai:", mhs.nilai)
                return
        print("Mahasiswa dengan NIM {} tidak ditemukan.".format(nim))
#----------------------------------------------------------------------

#--------------------DEFINE PERBAIKI----------------------------------
    def perbaiki_mahasiswa(self, nim, nama, nilai):
        for mhs in self.data_mahasiswa:
            if mhs.nim == nim:
                mhs.nama = nama
                mhs.nilai = nilai
                print("Data mahasiswa berhasil diperbarui.")
                return
        print("Mahasiswa dengan NIM {} tidak ditemukan.".format(nim))
#----------------------------------------------------------------------
        
        
#--------------------- DEFINE SIMPAN DATA -------------------------------
    def simpan_data(self, format_file):
        if not self.data_mahasiswa:
            print("Belum ada data mahasiswa yang dimasukkan.")
            return

        data = {
            "NIM": [m.nim for m in self.data_mahasiswa],
            "NAMA": [m.nama for m in self.data_mahasiswa],
            "NILAI": [m.nilai for m in self.data_mahasiswa],
        }

        df = pd.DataFrame(data)

        if format_file == "xlsx":
            file_path = "data_mahasiswa.xlsx"
            df.to_excel(file_path, index=False)
            input(f"Data mahasiswa berhasil disimpan ke {file_path}")

        elif format_file == "txt":
            file_path = "data_mahasiswa.txt"
            df.to_csv(file_path, index=False, sep='\t')
            input(f"Data mahasiswa berhasil disimpan ke {file_path}")
#----------------------------------------------------------------------   

#---------------------MESIN GENERATOR OTOMATIS---------------------
    def generate_nim(self):
        return ''.join(random.choices(string.digits, k=8))

    def generate_nama(self):
        return ''.join(random.choices(string.ascii_letters, k=10))

    def generate_nilai(self):
        return ''.join(random.choices(string.digits, k=2))
#------------------------------------------------------------------

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
            print("6. Simpan File")
            print("7. Tambah Mahasiswa Otomatis")
            print("8. Kembali")


            pilihan = input("Masukkan pilihan Anda: ")

            if pilihan == "1":
                # Memilih apakah ingin menambah satu data atau beberapa data
                multiple_entries = input("Ingin menambah lebih dari satu mahasiswa? (y/n): ")

                if multiple_entries.lower() == 'y':
                    while True:
                        nim = input("Masukkan NIM: ")
                        nama = input("Masukkan Nama: ")
                        nilai = input("Masukkan Nilai: ")
                        pengelola.tambah_mahasiswa(nim, nama, nilai)
                        print("Data mahasiswa berhasil ditambahkan!")
                        
                        lanjut = input("Tambah mahasiswa lagi? (y/n): ")
                        if lanjut.lower() == 'n':
                           break
                else:
                    nim = input("Masukkan NIM: ")
                    nama = input("Masukkan Nama: ")
                    nilai = input("Masukkan Nilai: ")
                    pengelola.tambah_mahasiswa(nim, nama, nilai)
                    input("Data mahasiswa berhasil ditambahkan!")
                    
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
                format_file = input("Simpan sebagai apa? (xlsx/txt): ")
                if format_file.lower() in ["xlsx", "txt"]:
                    pengelola.simpan_data(format_file.lower())
                input()
            
            elif pilihan == '7':
                multiple_entries = input("Ingin menambah lebih dari satu mahasiswa? (y/n): ")
                
                if multiple_entries.lower() == 'y':
                    num_data = int(input("Masukan jumlah data yang ingin ditambahkan: "))
                    for _ in range(num_data):
                        nim = pengelola.generate_nim()
                        nama = pengelola.generate_nama()
                        nilai = pengelola.generate_nilai()
                        pengelola.tambah_mahasiswa(nim, nama, nilai)
                        input("Data mahasiswa berhasil ditambahkan!")
                        
                else:
                    nim = pengelola.generate_nim()
                    nama = pengelola.generate_nama()
                    nilai = pengelola.generate_nilai()
                    pengelola.tambah_mahasiswa(nim, nama, nilai)
                    input("Data mahasiswa berhasil ditambahkan!")
                
            elif pilihan == '8':
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
