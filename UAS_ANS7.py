from U_File import PengelolaDataMahasiswa
from U_Sort import U_Sort
from U_Menu import main_menu
from U_Menu import logo_main
import U_Menu
import U_File
import os

def main():
    pengelola_mahasiswa = PengelolaDataMahasiswa()
    while True:
        U_Menu.logo_main()
        U_Menu.main_menu()
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            U_Menu.logo_main()
            pengelola_mahasiswa.menu_pengelola_mahasiswa()
        elif pilihan == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            U_Menu.logo_main()
            U_Sort.sorting_menu()
        elif pilihan == '3':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

                
if __name__ == "__main__":
    main()
