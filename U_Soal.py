#Perpustakaan ============================================================================
import tkinter as tk # tk dan tkinter adalah perpustakaan untuk membuat sebuah GUI dalam sebuah program
from tkinter import messagebox # massagebox : adalah sebuah perpustakaan untuk menampilkan feedback tambahan
import random # import random : sebuah perpustakaan untuk membuat suatu sistem acak dalam sebuah pemrograman
import math # perhitungan matematis dalam sebuah perppustakaan
import datetime # datetime : adalah sebuah perpustakaan untuk menampilkan sebuah tanggal dan waktu yang ada di system komputer kita
import sys
import os

# Khusus untuk Program 11 -----------
import string
import pandas as pd
from prettytable import PrettyTable
#------------------------------------
#========================================================================================


# PROGRAM GAME ==========================================================================
class MastermindGame:
    def __init__(self, master):
        # Inisialisasi permainan dengan jendela utama (master)
        self.master = master
        self.master.title("Mastermind Game")
        self.master.geometry("400x350")
        
        # Dictionary untuk memetakan nomor warna ke namanya
        self.colors = {
            1: "Merah", 2: "Putih", 3: "Hitam", 4: "Kuning",
            5: "Hijau", 6: "Biru", 7: "Coklat", 8: "Ungu",
            9: "Pink", 10: "Cyan"
        }
        
        # Menghasilkan kode rahasia acak dengan 4 warna
        self.secret_code = [random.randint(1, 10) for _ in range(4)]
        
        # Jumlah percobaan yang diperbolehkan dan nilai percobaan saat ini
        self.attempts_left = 5
        self.current_attempt = [tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()]
        
        # Menyiapkan GUI
        self.create_gui()

    # Membuat komponen GUI permainan    
    def create_gui(self):
        self.create_guess_row()
        self.create_input_rows()
        self.create_feedback_area()
       
    # Membuat baris tempat warna yang ditebak akan ditampilkan
    def create_guess_row(self):
        guess_frame = tk.Frame(self.master)
        guess_frame.pack(pady=10)

        # Label untuk mewakili setiap warna yang ditebak
        self.guess_labels = []
        for i in range(4):
            label = tk.Label(guess_frame, text="?", width=5, height=2, bg="lightgray", relief="solid")
            self.guess_labels.append(label)
            label.grid(row=0, column=i, padx=5)

    def create_input_rows(self):
        # Membuat baris untuk input pengguna (menebak)
        input_frame = tk.Frame(self.master)
        input_frame.pack(pady=5)

        # Widget Entry untuk memasukkan warna, dan tombol untuk mengirimkan tebakan
        for i in range(4):
            entry = tk.Entry(input_frame, textvariable=self.current_attempt[i], width=5)
            entry.grid(row=0, column=i, padx=5)

        guess_button = tk.Button(input_frame, text="Tebak", command=self.check_guess)
        guess_button.grid(row=0, column=4, padx=5)

    def create_feedback_area(self):
        # Membuat area untuk menampilkan umpan balik, kesempatan tersisa, dan informasi warna
        feedback_frame = tk.Frame(self.master)
        feedback_frame.pack(pady=10)

        # Label untuk umpan balik, kesempatan tersisa, dan informasi warna
        self.feedback_label = tk.Label(feedback_frame, text="Umpan Balik: ")
        self.feedback_label.pack()

        self.chances_label = tk.Label(feedback_frame, text=f"Kesempatan: {self.attempts_left}")
        self.chances_label.pack()

        info_label_1 = tk.Label(feedback_frame, text="1=Merah, 2=Putih, 3=Hitam, 4=Kuning, 5=Hijau,")
        info_label_1.pack()

        info_label_2 = tk.Label(feedback_frame, text="6=Biru, 7=Coklat, 8=Ungu, 9=Pink, 10=Cyan")
        info_label_2.pack()

    def check_guess(self):
        # Memeriksa tebakan pengguna terhadap kode rahasia
        guess = [var.get() for var in self.current_attempt]
        correct_positions = sum([1 for i in range(4) if guess[i] == self.secret_code[i]])

        # Memeriksa apakah semua posisi benar, jika ya, akhiri permainan
        if correct_positions == 4:
            self.end_game("100% benar. Anda berhasil menebak semua warna.")
        else:
            # Mengurangi percobaan dan memperbarui GUI
            self.attempts_left -= 1
            
            # Jika tidak ada percobaan lagi, akhiri permainan
            if self.attempts_left == 0:
                self.end_game("Anda kehabisan kesempatan. Game direset.")
            else:
                # Memperbarui warna yang ditebak, umpan balik, dan kesempatan tersisa
                self.update_guess_labels(guess, correct_positions)
                self.update_feedback(correct_positions)
                self.update_chances()
                
    # Memperbarui warna yang ditebak berdasarkan posisi yang benar
    def update_guess_labels(self, guess, correct_positions):
        for i, label in enumerate(self.guess_labels):
            if guess[i] == self.secret_code[i]:
                label.config(text=self.colors[guess[i]], bg="lightgray")
            elif guess[i] in self.secret_code:
                label.config(text="?", bg="white")
            else:
                label.config(text="?", bg="lightgray")
                
    # Memperbarui label umpan balik berdasarkan jumlah posisi yang benar
    def update_feedback(self, correct_positions):
        percentage = (correct_positions / 4) * 100
        self.feedback_label.config(text=f"{correct_positions} warna benar. Coba lagi!")

    # Memperbarui label kesempatan tersisa
    def update_chances(self):
        self.chances_label.config(text=f"Kesempatan: {self.attempts_left}")

    # Mengakhiri permainan dan menampilkan kotak pesan dengan kode yang benar
    def end_game(self, message):
        correct_code = [self.colors[color] for color in self.secret_code]
        messagebox.showinfo("Game Over", f"{message}\nJawaban yang benar: {correct_code}")
        self.reset_game()

    # Mereset permainan dengan menghasilkan kode rahasia baru dan mereset percobaan
    def reset_game(self):
        self.secret_code = [random.randint(1, 10) for _ in range(4)]
        self.attempts_left = 5

        # Mereset elemen GUI
        for label in self.guess_labels:
            label.config(text="?", bg="lightgray")

        self.feedback_label.config(text="Umpan Balik: ")
        self.chances_label.config(text=f"Kesempatan: {self.attempts_left}")

        for var in self.current_attempt:
            var.set(0)


# Fungsi yang menjalankan game Mastermind dalam program_11
def program_12():
    # Membuat jendela utama dan memulai permainan
    root = tk.Tk()
    game = MastermindGame(root)
    root.mainloop()
#=================================================================================


# Menjalankan Program ============================================================
def run_program(choice):
    if choice == 1:
        program_1()
    elif choice == 2:
        program_2()
    elif choice == 3:
        program_3()
    elif choice == 4:
        program_4()
    elif choice == 5:
        program_5()
    elif choice == 6:
        program_6()
    elif choice == 7:
        program_7()
    elif choice == 8:
        program_8()
    elif choice == 9:
        program_9()
    elif choice == 10:
        program_10()
    elif choice == 11:
        program_11()
    elif choice == 12:
        program_12()
#=================================================================================




#Program 1 =======================================================================
def program_1():

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("===========Program 1===========")
        
    # Menerima input dari pengguna
    bilangan1 = float(input("Masukkan bilangan pertama: "))
    bilangan2 = float(input("Masukkan bilangan kedua: "))
    bilangan3 = float(input("Masukkan bilangan ketiga: "))

    # Melakukan perhitungan
    hasil_penjumlahan = bilangan1 + bilangan2 + bilangan3
    hasil_perkalian = bilangan1 * bilangan2 * bilangan3

    # Menampilkan hasil perhitungan
    print(f"Hasil Penjumlahan: {hasil_penjumlahan}")
    print(f"Hasil Perkalian  : {hasil_perkalian}\n")
    
    print(f"Tekan Enter Untuk Kembali :")
    input()
#=================================================================================



#Program 2========================================================================
def program_2():

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("===========Program 2===========")
        
    # Menerima input panjang sisi dari pengguna
    panjang_sisi = float(input("Masukkan panjang sisi segitiga sama sisi (S): "))

    # Menghitung luas segitiga (LS)
    luas_segitiga = (panjang_sisi**2 * (3**0.5)) / 4
 
    # Menghitung keliling segitiga (KS)
    keliling_segitiga = 3 * panjang_sisi

    # Menampilkan hasil perhitungan
    print(f"Luas Segitiga    : {luas_segitiga}")
    print(f"Keliling Segitiga: {keliling_segitiga}\n")
    
    print(f"Tekan Enter Untuk Kembali :")
    input()
#=================================================================================



#Program 3 =======================================================================
def program_3():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("===========Program 3===========")
    
    # Menerima input panjang sisi siku-siku X dan Y dari pengguna
    panjang_sisi_x = float(input("Masukkan panjang sisi siku-siku X: "))
    panjang_sisi_y = float(input("Masukkan panjang sisi siku-siku Y: "))

    # Menghitung luas segitiga siku-siku (LSS)
    luas_segitiga_siku = 0.5 * panjang_sisi_x * panjang_sisi_y

    # Menghitung panjang sisi miring (hypotenuse)
    panjang_miring = (panjang_sisi_x**2 + panjang_sisi_y**2)**0.5

    # Menghitung keliling segitiga siku-siku (KSS) 
    keliling_segitiga_siku = panjang_sisi_x + panjang_sisi_y + panjang_miring

    # Menampilkan hasil perhitungan
    print(f"Luas Segitiga Siku-Siku    : {luas_segitiga_siku}")
    print(f"Keliling Segitiga Siku-Siku: {keliling_segitiga_siku}\n")
    
    print(f"Tekan Enter Untuk Kembali :")
    input()
#=================================================================================



#Program 4 =======================================================================
def program_4():

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("===========Program 4===========")
    
    # Menerima input diameter dari pengguna
    diameter = float(input("Masukkan diameter lingkaran (D): "))

    # Menghitung jari-jari lingkaran
    jari_jari = diameter / 2

    # Menghitung luas lingkaran (LL)
    luas_lingkaran = math.pi * jari_jari**2

    # Menghitung keliling lingkaran (KL)
    keliling_lingkaran = 2 * math.pi * jari_jari

    # Menampilkan hasil perhitungan
    print(f"Luas Lingkaran    : {luas_lingkaran}")
    print(f"Keliling Lingkaran: {keliling_lingkaran}\n")
    
    print(f"Tekan Enter Untuk Kembali :")
    input()
#=================================================================================



#Program 5 =======================================================================
def program_5():

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("===========Program 5===========")
    
    # Menerima input kecepatan (V1, V2, V3) dari pengguna
    kecepatan1 = float(input("Masukkan kecepatan pertama (V1): "))
    kecepatan2 = float(input("Masukkan kecepatan kedua (V2): "))
    kecepatan3 = float(input("Masukkan kecepatan ketiga (V3): "))

    # Menerima input waktu tempuh (T1, T2, T3) dari pengguna
    waktu_tempuh1 = float(input("Masukkan waktu tempuh pertama (T1): "))
    waktu_tempuh2 = float(input("Masukkan waktu tempuh kedua (T2): "))
    waktu_tempuh3 = float(input("Masukkan waktu tempuh ketiga (T3): "))

    # Menghitung jarak tempuh (S1, S2, S3)
    jarak_tempuh1 = kecepatan1 * waktu_tempuh1
    jarak_tempuh2 = kecepatan2 * waktu_tempuh2
    jarak_tempuh3 = kecepatan3 * waktu_tempuh3

    # Menghitung rata-rata jarak tempuh (Rata_jarak)
    rata_jarak = (jarak_tempuh1 + jarak_tempuh2 + jarak_tempuh3) / 3

    # Menampilkan hasil perhitungan
    print(f"")
    print(f"==================[Hasil Jarak Tempuh]==================")
    print(f"Jarak Tempuh 1: {jarak_tempuh1}")
    print(f"Jarak Tempuh 2: {jarak_tempuh2}")
    print(f"Jarak Tempuh 3: {jarak_tempuh3}")
    print(f"Rata-rata Jarak Tempuh: {rata_jarak}\n")
    
    print(f"Tekan Enter Untuk Kembali :")
    input()
#=================================================================================



#Program 6 =======================================================================
def program_6():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("===========Program 6===========")
        
    # Menerima input bilangan integer dari pengguna
    X = int(input("Masukkan sebuah bilangan integer (X): "))

    # Analisis kategori bilangan
    if X > 0 and X % 2 == 0:
        kategori = "Bilangan Genap Positif"
    elif X < 0 and X % 2 == 0:
        kategori = "Bilangan Genap Negatif"
    elif X > 0 and X % 2 != 0:
        kategori = "Bilangan Ganjil Positif"
    elif X < 0 and X % 2 != 0:
        kategori = "Bilangan Ganjil Negatif"
    else:
        kategori = "Nol"

    # Menampilkan hasil analisis
    print(f"")
    print(f"==================Hasil==================")
    print(f"Analisis Bilangan: {kategori}\n")
    
    print(f"Tekan Enter Untuk Kembali :")
    input()
#=================================================================================



#Program 7 =======================================================================
def program_7():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("===========Program 7===========")
    
    # Mendapatkan tanggal dan waktu saat ini
    tanggal_waktu_sekarang = datetime.datetime.now()
    hari = tanggal_waktu_sekarang.strftime("%A")
    tanggal = tanggal_waktu_sekarang.strftime("%x")
    waktu = tanggal_waktu_sekarang.strftime("%X")

    # Menerima input jumlah pembelian dalam Rp.
    jumlah_pembelian = float(input("Masukkan jumlah pembelian dalam Rp.: "))

    # Menerima input jenis konsumen (1 untuk pelanggan, 2 untuk non-pelanggan)
    jenis_konsumen = int(input("Masukkan jenis konsumen (1. Pelanggan; 2. Non-pelanggan): "))

    # Inisialisasi potongan dan cashback
    potongan = 0
    cashback = 0

    # Menghitung potongan untuk pelanggan
    if jenis_konsumen == 1:
        potongan = 0.10 * jumlah_pembelian

    # Menghitung cashback
    cashback = int(jumlah_pembelian / 1000000) * 30000

    # Menghitung total pembayaran setelah potongan dan cashback
    total_pembayaran = jumlah_pembelian - potongan + cashback

    # Menampilkan hasil transaksi
    print(f"\n===== Struk Pembayaran =====")
    print(f"Hari               : {hari}")
    print(f"Tanggal            : {tanggal}")
    print(f"Waktu              : {waktu}")
    print(f"Jumlah Pembelian   : Rp. {jumlah_pembelian:,.2f}")
    print(f"Potongan           : Rp. {potongan:,.2f}")
    print(f"Cashback           : Rp. {cashback:,.2f}")
    print(f"Total Pembayaran   : Rp. {total_pembayaran:,.2f}")
    print("============================\n")
    
    print(f"Tekan Enter Untuk Kembali :")
    input()
#=================================================================================



#Program 8 =======================================================================
def program_8():
   
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("===========Program 8===========")
    
    # Menerima input bilangan integer dari pengguna
    X = int(input("Masukkan sebuah bilangan integer (0 s/d 9): "))
    
    # Menampilkan tulisan teks bilangan
    if 0 <= X <= 9:
        if X == 0:
            print("nol")
        elif X == 1:
            print("satu")
        elif X == 2:
            print("dua")
        elif X == 3:
            print("tiga")
        elif X == 4:
            print("empat")
        elif X == 5:
            print("lima")
        elif X == 6:
            print("enam")
        elif X == 7:
            print("tujuh")
        elif X == 8:
            print("delapan")
        elif X == 9:
            print("sembilan")
    else:
        print("")
        print("---------------------------------")
        print("Salah entri: ketik bilangan 0..9")
        
    print(f"\nTekan Enter Untuk Kembali :")
    input()
# ================================================================================



#Program 9 =======================================================================
def program_9():

    os.system('cls' if os.name == 'nt' else 'clear')

    print("===========Program 9===========")
    
    # Input nilai UTS, UAS, TUGAS, dan KEHADIRAN
    UTS = float(input("Masukkan nilai UTS (0-100): "))
    UAS = float(input("Masukkan nilai UAS (0-100): "))
    TUGAS = float(input("Masukkan nilai TUGAS (0-100): "))
    KEHADIRAN = float(input("Masukkan nilai KEHADIRAN (0-16): "))

    # Hitung KEHADIRAN
    KEHADIRAN = (KEHADIRAN / 16) * 100

    # Hitung Nilai Akhir (NA)
    NA = (0.3 * UTS) + (0.4 * UAS) + (0.2 * TUGAS) + (0.1 * KEHADIRAN)

    # Tentukan Indeks Mutu (IM) berdasarkan Nilai Akhir (NA)
    if 0 <= NA <= 100:
        if NA > 80:
            IM = 'nilai A'
        elif NA > 65:
            IM = 'nilai B'
        elif NA > 50:
            IM = 'nilai C'
        elif NA > 40:
            IM = 'nilai D'
        else:
            IM = 'nilai E'
    else:
        IM = 'Salah nilai'

    # Tampilkan Nilai Akhir dan Indeks Mutu
    print("===========================")
    print(f"Nilai Akhir (NA)    : {NA:.2f}")
    print(f"Indeks Mutu (IM)    : {IM}")
    print("===========================")
    
    print(f"\nTekan Enter Untuk Kembali :")
    input()
#==================================================================================



#Program 10 =======================================================================
def program_10():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("===========Program 10===========")
    
    # Menerima input dua bilangan bulat AWAL dan AKHIR dari pengguna
    AWAL = int(input("Masukkan bilangan AWAL: "))
    AKHIR = int(input("Masukkan bilangan AKHIR: "))

    # Periksa apakah AWAL lebih kecil dari AKHIR
    if AWAL >= AKHIR:
        print("AWAL harus kurang dari AKHIR.")
        return

    # Mencetak semua bilangan dari AWAL hingga AKHIR
    print("Deret bilangan dari", AWAL, "sampai", AKHIR, ":")
    for i in range(AWAL, AKHIR + 1):
        print(i)
        
    print(f"\nTekan Enter Untuk Kembali :")
    input()
#==================================================================================



#Program 11 =======================================================================
class Mahasiswa:
    def __init__(self, nim, nama, nilai):
        self.nim = nim
        self.nama = nama
        self.nilai = nilai

class ProgramMahasiswa:
    def __init__(self):
        self.mahasiswa_list = []

    def tambah_mahasiswa(self, nim, nama, nilai):
        mahasiswa_baru = Mahasiswa(nim, nama, nilai)
        self.mahasiswa_list.append(mahasiswa_baru)

    def tampilkan_data(self):
        if not self.mahasiswa_list:
            print("Belum ada data mahasiswa yang dimasukkan.")
            return

        table = PrettyTable()
        table.field_names = ["NIM", "Nama", "Nilai"]

        for mahasiswa in self.mahasiswa_list:
            table.add_row([mahasiswa.nim, mahasiswa.nama, mahasiswa.nilai])

        print(table)
        
    def generate_nim(self):
        return ''.join(random.choices(string.digits, k=8))

    def generate_nama(self):
        return ''.join(random.choices(string.ascii_letters, k=10))

    def generate_nilai(self):
        return ''.join(random.choices(string.digits, k=2))
        
    def simpan_data(self, format_file):
        if not self.mahasiswa_list:
            print("Belum ada data mahasiswa yang dimasukkan.")
            return

        data = {
            "NIM": [m.nim for m in self.mahasiswa_list],
            "Nama": [m.nama for m in self.mahasiswa_list],
            "Nilai": [m.nilai for m in self.mahasiswa_list],
        }

        df = pd.DataFrame(data)

        if format_file == "xlsx":
            file_path = "data_mahasiswa.xlsx"
            df.to_excel(file_path, index=False)
            print(f"Data mahasiswa berhasil disimpan ke {file_path}")

        elif format_file == "txt":
            file_path = "data_mahasiswa.txt"
            df.to_csv(file_path, index=False, sep='\t')
            print(f"Data mahasiswa berhasil disimpan ke {file_path}")

def program_11():
    program = ProgramMahasiswa()

    while True:
        print("\n=== PROGRAM INPUT DATA MAHASISWA ===")
        print("1. Tambah Data Mahasiswa")
        print("2. Tambah Mahasiswa Otomatis")
        print("3. Tampilkan Data Mahasiswa")
        print("4. Simpan File Berbentuk (.txt/.xlsx)")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            # Memilih apakah ingin menambah satu data atau beberapa data
            multiple_entries = input("Ingin menambah lebih dari satu mahasiswa? (y/n): ")

            if multiple_entries.lower() == 'y':
                while True:
                    nim = input("Masukkan NIM: ")
                    nama = input("Masukkan Nama: ")
                    kelas = input("Masukkan Nilai: ")
                    program.tambah_mahasiswa(nim, nama, nilai)
                    print("Data mahasiswa berhasil ditambahkan!")

                    lanjut = input("Tambah mahasiswa lagi? (y/n): ")
                    if lanjut.lower() == 'n':
                        break
            else:
                nim = input("Masukkan NIM: ")
                nama = input("Masukkan Nama: ")
                nilai = input("Masukkan Nilai: ")
                program.tambah_mahasiswa(nim, nama, nilai)
                print("Data mahasiswa berhasil ditambahkan!")
                
        elif pilihan == "2":
            # Memilih apakah ingin menambah satu data atau beberapa data
            multiple_entries = input("Ingin menambah lebih dari satu mahasiswa? (y/n): ")

            if multiple_entries.lower() == 'y':
                num_data = int(input("Masukan jumlah data yang ingin ditambahkan: "))
                for _ in range(num_data):
                    nim = program.generate_nim()
                    nama = program.generate_nama()
                    nilai = program.generate_nilai()
                    program.tambah_mahasiswa(nim, nama, nilai)
                    print("Data mahasiswa berhasil ditambahkan!")
            else:
                nim = program.generate_nim()
                nama = program.generate_nama()
                nilai = program.generate_nilai()
                program.tambah_mahasiswa(nim, nama, nilai)
                print("Data mahasiswa berhasil ditambahkan!")        

        elif pilihan == "3":
            program.tampilkan_data()

        elif pilihan == "4":
            # Pilihan untuk menyimpan data ke dalam format Excel atau teks
            format_file = input("Simpan sebagai apa? (xlsx/txt): ")
            if format_file.lower() in ["xlsx", "txt"]:
                program.simpan_data(format_file.lower())
            else:
                print("Format tidak valid. Pilih 'xlsx' atau 'txt'.")
                
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program.")
            break

        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
#==================================================================================
