def main():
    jarakWarung = [10, 25, 30, 40, 50, 75, 80, 110, 130]
    minStops = float('inf')
    kombinasiTerbaik = []

    # Loop mencari kombinasi
    for i in range(1 << len(jarakWarung)):
        combination = []

        # cek warung terpilih atau tidak untuk berhenti
        for j in range(len(jarakWarung)):
            if i & (1 << j):
                combination.append(jarakWarung[j])

        # Memeriksa apakah kombinasi saat ini memenuhi persyaratan
        if is_valid_combination(combination, 140, 30):
            # Menghitung jumlah berhenti pada kombinasi saat ini
            numStops = len(combination)

            # Memeriksa apakah kombinasi saat ini lebih optimal
            if numStops < minStops:
                minStops = numStops
                kombinasiTerbaik = combination[:]

    # Menampilkan titik-titik warung Tono akan berhenti
    print("Warung yang terpilih untuk Tono berhenti:", end=" ")
    for i in range(len(kombinasiTerbaik)):
        print(kombinasiTerbaik[i], end=" ")
    print()

# Memeriksa apakah kombinasi titik-titik warung memenuhi persyaratan
def is_valid_combination(combination, totalJarak, jarakIstirahat):
    # Memeriksa apakah total jarak yang dapat ditempuh Tono dengan berhenti di warung-warnug memenuhi persyaratan
    jarak = 0
    for i in range(len(combination)):
        if combination[i] - jarak > jarakIstirahat:
            return False
        jarak = combination[i]
    if totalJarak - jarak > jarakIstirahat:
        return False
    return True

if __name__ == "__main__":
    main()
