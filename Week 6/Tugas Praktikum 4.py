#Mendefinisikan himpunan
A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3}
D = {100, 200, 300}

#Menghitung gabungan
hasil_a = A.union(B)
hasil_b = B.union(C)
hasil_c = B.union(C).union(D)
hasil_d = A.union(B).union(C).union(D)

#Menampilkan hasil
print("A U B =", hasil_a)
print("B U C =", hasil_b)
print("B U C U D =", hasil_c)
print("A U B U C U D =", hasil_d)