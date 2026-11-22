# Afra Nur Haerani Haeba
# 065002600035

pilihan = 0
while pilihan != 4:
    print('''===== Program File Handling =====
1. Membuat dan Menulis File
2. Membaca File
3. Menambahkan Text pada File
4. Keluar dari Program
''')
    pilihan = int(input("Masukkan Pilihan Berupa Angka (1/2/3/4): "))
    if pilihan == 1:
        def tulis_data():
            nama_file = input("Masukkan Nama File: ")
            nama = input("Masukkan Namamu: ")
            nim = input("Masukkan NIM kamu: ")
            akt = input("Masukkan tahun angkatanmu: ")
            file = open(nama_file, "w")
            file.write("Nama: " + nama + "\n")
            file.write("NIM: " + nim + "\n")
            file.write("Angkatan: " + akt + "\n")
            file.close()
        tulis_data()
        print()
        print()
        print("File Berhasil Dibuat")
        print()
        print()
    elif pilihan == 2:
        def baca_data():
            nama_file = input("Masukkan Nama File: ")
            print()
            print()
            file = open(nama_file, "r")
            text = file.read()
            print(text)
            file.close()
        baca_data()
        print()
        print()
    elif pilihan == 3:
        def tambah_data():
            nama_file = input("Masukkan Nama File: ")
            sahabat = input("Masukkan Nama Sahabatmu: ")
            catatan = input("Masukkan Catatan Tambahan Kamu: ")
            file = open(nama_file, "a")
            file.write("Sahabat: " + sahabat + "\n")
            file.write("Catatan: " + catatan + "\n")
            file.close()
        tambah_data()
        print()
        print()
        print("Data Berhasil Ditambahkan")
        print()
        print()
    else:
        print("Terima Kasih Sudah Menggunakan Program Saya")
