# Afra Nur Haerani Haeba
# 065002600035

print("Ordinal Number")
print("Ketik 0 untuk menghentikan program")

def ord_numb(angka):
    if angka % 100 in (11, 12, 13):
        akhiran = "th"
    elif angka % 10 == 1:
        akhiran = "st"
    elif angka % 10 == 2:
        akhiran = "nd"
    elif angka % 10 == 3:
        akhiran = "rd"
    else:
        akhiran = "th"
    return akhiran

while True:
    angka = int(input("Masukkan angka: "))
    if angka == 0:
        print("Terima kasih telah menggunakan program saya")
        break
    print((angka, ord_numb(angka)))
