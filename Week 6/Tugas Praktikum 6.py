# Mendefinisikan himpunan
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e'}
C = set()  # Himpunan kosong

# Menghitung selisih
hasil_a = A.difference(B)
hasil_b = B.difference(A)
hasil_c = A.difference(C)
hasil_d = B.difference(C)

# Menampilkan hasil
print("A difference B =", hasil_a)
print("B difference A =", hasil_b)
print("A difference C =", hasil_c)
print("B difference C =", hasil_d)