import numpy as np
import matplotlib.pyplot as plt

# 1. Masukkan data asli (x dan y)
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([2.1, 7.7, 13.6, 27.2, 40.9, 61.1])

# Menghitung jumlah data (n)
n = len(x_data)

# 2. Menghitung setiap kolom yang dibutuhkan untuk tabel
x2 = x_data**2
x3 = x_data**3
x4 = x_data**4
xy = x_data * y_data
x2y = (x_data**2) * y_data

# 3. Menghitung nilai Total / Sigma (Σ)
sum_x = np.sum(x_data)
sum_y = np.sum(y_data)
sum_x2 = np.sum(x2)
sum_x3 = np.sum(x3)
sum_x4 = np.sum(x4)
sum_xy = np.sum(xy)
sum_x2y = np.sum(x2y)

# 4. Menyusun Matriks Sistem Persamaan (Normal Equations)
# A: Matriks koefisien variabel (a, b, c)
A = np.array([
    [n,      sum_x,  sum_x2],
    [sum_x,  sum_x2, sum_x3],
    [sum_x2, sum_x3, sum_x4]
])

# B: Vektor hasil di ruas kanan
B = np.array([sum_y, sum_xy, sum_x2y])

# 5. Menyelesaikan Sistem Persamaan (Mencari a, b, c)
# Metode numerik otomatis untuk memecahkan matriks Ax = B
koefisien = np.linalg.solve(A, B)
a, b, c = koefisien

# Menampilkan Persamaan yang Ditemukan
print("=== PERSAMAAN HASIL REGRESI ===")
print(f"a (intercept)    = {a:.4f}")
print(f"b (koefisien x)   = {b:.4f}")
print(f"c (koefisien x^2) = {c:.4f}")
print(f"\nPersamaan polinomial orde 2 adalah:")
print(f"y = {a:.4f} + {b:.4f}x + {c:.4f}x^2\n")

plt.figure(figsize=(10, 6)) # Atur ukuran kanvas

# 1. Plot Titik Data Asli (Scatter Plot)
# Kita gunakan penanda 'o' berwarna merah untuk titik data asli dari tabel.
plt.scatter(x_data, y_data, color='red', label='Data Asli (Tabel)', marker='o', s=100)

# 2. Plot Kurva Regresi yang Mulus
x_curve = np.linspace(x_data.min(), x_data.max(), 100)

# Masukkan X_curve ini ke dalam persamaan model kita: y = a + bx + cx^2
# Menghitung nilai Y prediksi untuk setiap titik kurva tersebut.
y_curve = a + (b * x_curve) + (c * (x_curve**2))

# Kita plot X baru dan Y prediksi sebagai garis biru yang mulus.
plt.plot(x_curve, y_curve, color='blue', linewidth=2, label='Kurva Fit Polinomial Orde 2')

# 3. Mempercantik Tampilan Grafik
plt.title('Regresi Polinomial: Menyesuaikan Kurva Kuadratik ke Data Asli')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')

equation_text = f'$y = {a:.3f} + {b:.3f}x + {c:.3f}x^2$'
plt.text(1, 50, equation_text, fontsize=12, color='blue', fontweight='bold')

# Menampilkan legenda, kisi-kisi (grid), dan menampilkan plot
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7) # Alpha mengatur transparansi grid

# Tampilkan grafik
plt.show()