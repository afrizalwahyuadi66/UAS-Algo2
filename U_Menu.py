import os
from U_File import PengelolaDataMahasiswa
from U_Sort import U_Sort

def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nMenu Utama:")
        print("1. Pengelola Data Mahasiswa")
        print("2. Sorting dari Data file")
        print("3. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            pengelola_mahasiswa = PengelolaDataMahasiswa()
            pengelola_mahasiswa.menu_pengelola_mahasiswa()
        elif pilihan == '2':
            U_Sort.sorting_menu()
        elif pilihan == '3':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main_menu()
