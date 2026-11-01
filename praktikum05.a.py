# Afra Nur Haerani Haeba
# 065002600035


jumlah = 0
total = 0
while True :
    huruf=input("Masukkan nilai: ")
    huruf = huruf.upper()
    if huruf == "":
        break
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
        print("Masukkan huruf dengan benar!")
        continue
    total += nilai
    jumlah += 1
    print(f'nilai = {nilai}')
average = total/jumlah
print(f"rata-ratanya adalah: {average}")
