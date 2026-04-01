import numpy as np
import matplotlib.pyplot as plt

# 1. Masukkan Data Asli
x = np.array([1, 2, 3])
y = np.array([2.4, 5, 9])
n = len(x)

# 2. Trik Linearisasi: Ubah y menjadi z = ln(y)
z = np.log(y)

# Hitung komponen tabel
x2 = x**2
xz = x * z

# Hitung total (Sigma)
sum_x = np.sum(x)
sum_z = np.sum(z)
sum_x2 = np.sum(x2)
sum_xz = np.sum(xz)

print(f"Sigma z = {sum_z:.5f}")
print(f"Sigma xz = {sum_xz:.5f}")

# 3. Susun Matriks (Sama persis dengan Regresi Linear)
A = np.array([
    [n, sum_x],
    [sum_x, sum_x2]
])
B = np.array([sum_z, sum_xz])

# Selesaikan matriks untuk mencari alpha dan b
koefisien = np.linalg.solve(A, B)
alpha, b = koefisien

print(f"\nHasil penyelesaian matriks:")
print(f"alpha = {alpha:.5f}")
print(f"b = {b:.5f}")

# 4. Kembalikan alpha menjadi a (Inverse Transform)
# Karena alpha = ln(a), maka a = e^alpha
a = np.exp(alpha)

print(f"\nMengembalikan nilai a:")
print(f"a = e^alpha = {a:.5f}")
print(f"Fungsi Final: f(x) = {a:.5f} e^({b:.5f}x)")

# 5. Visualisasi Kurva Eksponensial Asli
plt.figure(figsize=(8, 5))

# Plot titik data asli
plt.scatter(x, y, color='red', s=100, label='Data Asli', zorder=5)

# Buat kurva halus
x_curve = np.linspace(min(x) - 0.5, max(x) + 0.5, 100)
# Gunakan rumus eksponensial asli: y = a * e^(bx)
y_curve = a * np.exp(b * x_curve)

plt.plot(x_curve, y_curve, color='blue', linewidth=2, label='Kurva Eksponensial Fit')

plt.title('Regresi Eksponensial (via Linearisasi Logaritmik)')
plt.xlabel('x')
plt.ylabel('y')

# Menampilkan persamaan di dalam grafik
eq_text = f'$f(x) = {a:.4f} e^{{{b:.4f}x}}$'
plt.text(1, 6, eq_text, fontsize=14, color='blue', 
         bbox=dict(facecolor='white', edgecolor='blue', alpha=0.8, boxstyle='round,pad=0.5'))

plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()