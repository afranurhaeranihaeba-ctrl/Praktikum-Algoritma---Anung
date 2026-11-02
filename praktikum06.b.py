# Afra Nur Haerani Haeba
# 065002600035

print("Program ini akan menentukan jumlah hari dalam bulan tertentu")
print("Masukkan 0 untuk menghentikan program")

def kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or tahun % 400 == 0:
        return True
    else:
        return False

def jumlah_hari(bulan, tahun=0):
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    elif bulan == 2:
        if kabisat(tahun):
            return 29
        else:
            return 28
    
while True:
    bulan = int(input("masukkan bulan (1-12): "))
    hari = jumlah_hari(bulan, tahun=0)
    if bulan == 0:
        break
    elif bulan == 2:
        tahun = int(input("masukkan tahun (e.g., 2021): "))
        hari = jumlah_hari(bulan, tahun)
        print(f"{hari} hari dalam sebulan")
        print("Masukkan 0 untuk menghentikan program")
    else:
        print(f"{hari} hari dalam sebulan")
        print("Masukkan 0 untuk menghentikan program")
print("Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.")
    
