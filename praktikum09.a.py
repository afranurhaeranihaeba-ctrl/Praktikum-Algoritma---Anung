# Afra Nur Haerani Haeba
# 065002600035

def tulis_data():
    nama = input("Masukkan Namamu: ")
    umur = input("Masukkan Umurmu: ")
    alamat = input("Masukkan Alamatmu: ")
    email = input("Masukkan Emailmu: ")
    dosen = input("Masukkan Dosen Walimu: ")

    file = open("Biodata.txt", "w")
    file.write("Nama: " + nama + "\n")
    file.write("Umur: " + umur + "\n")
    file.write("Alamat: " + alamat + "\n")
    file.write("Email: " + email + "\n")
    file.write("Dosen Wali: " + dosen + "\n")
    file.close()


def baca_data():
    file = open("Biodata.txt", "r")
    print("\nBerikut Ini Data Kamu")
    text = file.read()
    print(text)
    file.close()

tulis_data()
baca_data()
