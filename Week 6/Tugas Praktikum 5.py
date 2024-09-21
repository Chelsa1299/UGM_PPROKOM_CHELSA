#Mendefinisikan himpunan
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e'}
C = set()  # Himpunan kosong

#Menghitung selisih simetris
hasil_a = A.symmetric_difference(B)
hasil_b = B.symmetric_difference(A)
hasil_c = A.symmetric_difference(C)
hasil_d = B.symmetric_difference(C)

#Menampilkan hasil
print("A symmetric difference B =", hasil_a)
print("B symmetric difference A =", hasil_b)
print("A symmetric difference C =", hasil_c)
print("B symmetric difference C =", hasil_d)