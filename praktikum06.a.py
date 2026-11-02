# Afra Nur Haerani Haeba
# 065002600035

def ord_nilai_huruf(huruf):
    huruf = huruf.upper()
    if huruf=="A":
        nilai = 4.00
    elif huruf=="A-":
        nilai = 3.75
    elif huruf=="B+":
        nilai = 3.50
    elif huruf=="B":
        nilai = 3.00
    elif huruf=="B-":
        nilai = 2.75
    elif huruf=="C+":
        nilai = 2.50
    elif huruf=="C":
        nilai = 2.00
    elif huruf=="C-":
        nilai = 1.75
    elif huruf=="D":
        nilai = 1.50
    elif huruf=="E":
        nilai = 1.25
    else:
        nilai = None
    return nilai

jumlah = 0
total = 0
while True:
    huruf = input("masukkan nilai: ")
    nilai = ord_nilai_huruf(huruf)
    if huruf == "":
        break
    else:
        print(f"nilai = {nilai}")
    total += nilai
    jumlah += 1
average = total/jumlah
print(f"Rata-ratanya adalah: {average}")
