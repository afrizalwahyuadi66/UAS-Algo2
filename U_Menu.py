from U_File import PengelolaDataMahasiswa
from U_Sort import internal_sort_menu, selection_sort_menu, exchange_sort_menu

def main_menu():
    pengelola_mahasiswa = PengelolaDataMahasiswa()

    while True:
        print("\nMenu Utama:")
        print("1. Pengelola Data Mahasiswa")
        print("2. Simulasi Metode Internal-Sorting dari Data file")
        print("3. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            pengelola_mahasiswa.menu_pengelola_mahasiswa()
        elif pilihan == '2':
            sorting_menu()
        elif pilihan == '3':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def sorting_menu():
    while True:
        print("\nMenu Simulasi Metode Sorting:")
        print("1. Internal Sort")
        print("2. Selection Sort")
        print("3. Exchange Sort")
        print("4. Kembali ke Menu Utama")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            internal_sort_menu()
        elif pilihan == '2':
            selection_sort_menu()
        elif pilihan == '3':
            exchange_sort_menu()
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main_menu()
