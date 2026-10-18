# Afra Nur Haerani Haeba
# 065002600035

bulan = int(input("Masukkan angka bulan (1-12): "))
tahun = int(input("Masukkan angka tahun (misal 2000): "))

while bulan < 1 or bulan > 12:
    print("Angka bulan tidak valid!")
    bulan = int(input("Masukkan angka bulan (1-12): "))

hari = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

jumlah = hari[bulan]
kabisat = (tahun % 4 == 0 and tahun % 100 != 0) or tahun % 400 == 0
jumlah += (bulan == 2) * kabisat

print(f"Ada {jumlah} hari dalam bulan tersebut")
