import numpy as np
import matplotlib.pyplot as plt

# 1. Memasukkan data asli dari gambar (x dan y)
x = np.array([1, 2, 3])
y = np.array([5.1, 5.9, 6.3])

n = len(x) # Jumlah data (n = 3)

# 2. Menghitung elemen tabel (x^2 dan xy)
x2 = x**2
xy = x * y

# 3. Menghitung total (Sigma Σ)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_x2 = np.sum(x2)
sum_xy = np.sum(xy)

# 4. Menyusun Matriks Sistem Persamaan
# Baris 1: n*a      + (Σx)*b   = Σy
# Baris 2: (Σx)*a   + (Σx^2)*b = Σxy
A = np.array([
    [n,     sum_x],
    [sum_x, sum_x2]
])

B = np.array([sum_y, sum_xy])

# 5. Menyelesaikan sistem persamaan untuk mencari a dan b
a, b = np.linalg.solve(A, B)

print("=== HASIL REGRESI LINEAR ===")
print(f"a (intercept) = {a:.4f}")
print(f"b (gradien/slope) = {b:.4f}")
print(f"Persamaan garis: y = {a:.4f} + {b:.4f}x")

# 6. VISUALISASI GRAFIK
plt.figure(figsize=(8, 5))

# Plot titik data asli
plt.scatter(x, y, color='red', label='Data Asli', zorder=5)

# Plot garis regresi
# Untuk garis lurus, kita cukup menggunakan titik x asli atau membuat garis halus
x_line = np.linspace(min(x) - 0.5, max(x) + 0.5, 100)
y_line = a + b * x_line

plt.plot(x_line, y_line, color='blue', label='Garis Regresi Linear')

# Mempercantik grafik
plt.title('Regresi Linear (Linear Regression)')
plt.xlabel('x')
plt.ylabel('y')

# Menambahkan teks persamaan di dalam grafik
equation_text = f'$y = {a:.2f} + {b:.2f}x$'
plt.text(1.5, 6.0, equation_text, fontsize=12, color='blue', fontweight='bold')

plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()