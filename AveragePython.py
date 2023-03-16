#Tugas menghitung rata-rata waktu dan kompleksitas algoritma dengan bahasa pemrograman Python

import time

jumlah = 0
k = 1
n = int(input("Masukkan jumlah angka: "))
while k <= n:
    angka = int(input("angka : "))
    jumlah = jumlah + angka
    k +=1

startTime = time.time_ns()
r = jumlah/n

print("Rata-rata:", r)

endTime = time.time_ns()

executionTime = (endTime - startTime)/1000000
print("Waktu eksekusi:", executionTime)
