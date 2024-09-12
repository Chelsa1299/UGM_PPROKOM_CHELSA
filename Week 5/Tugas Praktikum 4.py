# Program untuk menghitung rata-rata
jumlah_data = int(input("Masukkan jumlah data: "))
data = [float(input(f"Data ke-{i+1}: ")) for i in range(jumlah_data)]
rata_rata = sum(data) / jumlah_data

print(f"Rata-rata: {rata_rata}")