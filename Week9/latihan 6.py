data = [1, 5, 4, 6, 7, 12, 45, 9, 99, 55, 100, 88, 75, 60]

angka_genap = [i for i in data if i % 2 == 0]
angka_ganjil = [i for i in data if i % 2 != 0]

print("Daftar angka:", data)
print("Ini adalah angka genap:", angka_genap)
print("Jumlah angka genap:", len(angka_genap), "angka")
print("Ini adalah angka ganjil:", angka_ganjil)
print("Jumlah angka ganjil:", len(angka_ganjil), "angka")
