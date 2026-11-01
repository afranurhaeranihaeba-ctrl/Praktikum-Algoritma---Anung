harga = 0
total = 0
while True:
    umur = input("masukkan umur: ")
    if umur == "":
        break
    umur = int(umur)
    if umur <= 2:
        harga = 0
        print("Gratis")
    elif 3 <= umur <= 12:
        harga = 14
        print(f"Harga ${harga:.2f}")
    elif umur >= 65:
        harga = 18
        print(f"Harga ${harga:.2f}")
    elif 12 < umur < 65:
        harga = 23
        print(f"Harga ${harga:.2f}")
    total += harga
    print(f"Running total: {total:.2f}")
uang = int(input("masukkan jumlah uang: "))
kembalian = 0
if uang > total:
    kembalian = uang - total
print(f"Running kembalian: {kembalian:.2f}")
