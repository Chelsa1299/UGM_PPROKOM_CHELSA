# Mendefinisikan himpunan
A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3}
D = {100, 200, 300}

# Menghitung irisan
hasil_a = A.intersection(D)
hasil_b = B.intersection(D)
hasil_c = C.intersection(D)
hasil_d = A.intersection(B).intersection(C).intersection(D)

# Menampilkan hasil
print("A ∩ D =", hasil_a)
print("B ∩ D =", hasil_b)
print("C ∩ D =", hasil_c)
print("A ∩ B ∩ C ∩ D =", hasil_d)