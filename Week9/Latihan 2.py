angka = []

for i in range(5):
    nilai = float(input(f"Masukkan angka ke-{i+1}: "))
    angka.append(nilai)
    print(angka)

jumlah_total = sum(angka)
pilihan = input("Ingin melihat 'jumlah' atau 'rata-rata': ").lower()

if pilihan == "jumlah":
    print("Jumlah total dari angka-angka yang dimasukkan adalah:", jumlah_total)
elif pilihan == "rata-rata":
    rata_rata = jumlah_total / len(angka)
    print("Rata-rata dari angka-angka yang dimasukkan adalah:", rata_rata)
else:
    print("Input tidak sesuai. Harap masukkan 'jumlah' atau 'rata-rata'.")
