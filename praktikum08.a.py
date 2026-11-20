def penjumlahan(jumlah, urutan=1):
    if urutan > jumlah:
        return 0
    else:
        bilangan = int(input(f"Masukkan bilangan ke-{urutan}: "))
        return bilangan + penjumlahan(jumlah, urutan+1)

jumlah = int(input("Masukkan Jumlah: "))
hasil = penjumlahan(jumlah)

print(f"Hasil dari penjumlahan adalah: {hasil}")
