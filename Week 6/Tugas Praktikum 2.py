#Mendefinisikan himpunan awal
nilai = {3, 6, 9, 2, 5, 7}

#Menambahkan elemen baru ke dalam himpunan
nilai.update({1, 4, 8, 10})

#Menampilkan hasil setelah ditambah
print("Himpunan setelah ditambah:", nilai)

#Menghapus elemen dari himpunan
nilai.difference_update({1, 3, 4, 5, 7, 8, 10})

#Menampilkan hasil setelah dihapus
print("Himpunan setelah dihapus:", nilai)