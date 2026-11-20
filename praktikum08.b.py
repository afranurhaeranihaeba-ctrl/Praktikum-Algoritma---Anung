# Afra Nur Haerani Haeba
# 065002600035

print("Ini merupakan program pemangkatan negatif dan positif. Tekan enter untuk berhenti.")

def pemangkatan(a, b):
    if b==0:
        return 1
    elif b>0:
        return a*pemangkatan(a, b-1)
    else:
        return 1/a*pemangkatan(a, b+1)

def program():
    angka = input("Masukkan angka: ")
    if angka == "":
        print("Program Selesai")
    else:
        angka = int(angka)
        pangkat = int(input("Masukkan pangkatnya: "))
        hasil = pemangkatan(angka, pangkat)
        print(f"Hasilnya adalah: {hasil}")
        program()

program()
