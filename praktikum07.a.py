# Afra Nur Haerani Haeba
# 065002600035

def prima(bilangan):
    if bilangan <= 1:
        return False
    for i in range(2, bilangan):
        if bilangan % i == 0:
            return False
    return True

angka = int(input("Masukkan angka: "))

def hasil(angka, prima):
    if prima(angka):
        return(f"{angka} adalah bilangan Prima")
    else:
        return(f"{angka} bukanlah bilangan Prima")

hasil = hasil(angka, prima)
print(hasil)
