# Include library yang diperlukan
# Library math digunakan untuk menggunakan fungsi matematika seperti pow() dan exp()
# Library numpy digunakan untuk menggunakan array dan operasi matematika sederhana
import math
import numpy as np

# Fungsi yang akan diintegrasi
def f(x):
    return 1/(7 + x)

# Batas integral
a = 0
b = 1

# Jumlah perulangan untuk metode Integrasi Romberg
n = 8

# Matriks untuk menyimpan hasil perhitungan
R = np.zeros((n,n))

# Nilai h pertama
h = b - a

# Nilai R(0,0) adalah hasil dari metode trapesium
R[0][0] = (h/2) * (f(a) + f(b))

# Perulangan untuk menghitung nilai R(i,j) dengan i dan j dari 1 hingga n-1
for i in range(1, n):
    # Nilai h yang baru
    h = h/2
    
    # Menghitung jumlah f(x) dengan x sebagai titik tengah setiap interval
    s = 0
    for k in range(1, int(pow(2, i-1)) + 1):
        s += f(a + (2*k-1)*h)
    
    # Menghitung nilai R(i,0) dengan metode trapesium yang diperbaiki
    R[i][0] = R[i-1][0]/2 + h*s
    
    # Perulangan untuk menghitung nilai R(i,j) dengan j dari 1 hingga i
    for j in range(1, i+1):
        # Menghitung nilai R(i,j) dengan rumus Integrasi Romberg
        R[i][j] = (pow(4, j) * R[i][j-1] - R[i-1][j-1]) / (pow(4, j) - 1)

# Menampilkan hasil perhitungan Integrasi Romberg
print("Hasil Integrasi Romberg:", R[n-1][n-1])
