import numpy as np
import matplotlib.pyplot as plt

# Masukkan Data Asli
x = np.array([0.24, 0.65, 0.95, 1.24, 1.73, 2.01, 2.23, 2.52])
y = np.array([0.23, -0.23, -1.1, -0.45, 0.27, 0.1, -0.29, 0.24])

# Hitung Nilai Tabel & Total (Sigma)
# Mendefinisikan fungsi transformasinya
f1 = np.log(x)   # ln(x)
f2 = np.cos(x)   # cos(x)
f3 = np.exp(x)   # e^x

# Menghitung total (Sigma) dari setiap kombinasi
sum_f1_sq = np.sum(f1**2)            # Σ (ln x)^2
sum_f1_f2 = np.sum(f1 * f2)          # Σ (ln x * cos x)
sum_f1_f3 = np.sum(f1 * f3)          # Σ (ln x * e^x)
sum_y_f1  = np.sum(y * f1)           # Σ (y * ln x)

sum_f2_sq = np.sum(f2**2)            # Σ (cos x)^2
sum_f2_f3 = np.sum(f2 * f3)          # Σ (cos x * e^x)
sum_y_f2  = np.sum(y * f2)           # Σ (y * cos x)

sum_f3_sq = np.sum(f3**2)            # Σ (e^x)^2
sum_y_f3  = np.sum(y * f3)           # Σ (y * e^x)

# Menyusun Matriks A dari nilai total di atas
A = np.array([
    [sum_f1_sq, sum_f1_f2, sum_f1_f3],
    [sum_f1_f2, sum_f2_sq, sum_f2_f3],
    [sum_f1_f3, sum_f2_f3, sum_f3_sq]
])

# Menyusun Vektor B
B = np.array([sum_y_f1, sum_y_f2, sum_y_f3])

# Cetak Matriks agar bisa dicocokkan dengan slide presentasi Anda
print("=== MATRIKS A (Dari Nilai Tabel) ===")
print(A)
print("\n=== VEKTOR B (Dari Nilai Tabel) ===")
print(B)

# Memecahkan matriks untuk mencari a, b, c
koefisien = np.linalg.solve(A, B)
a, b, c = koefisien

print("\n=== HASIL PENYELESAIAN ===")
print(f"a = {a:.5f}")
print(f"b = {b:.5f}")
print(f"c = {c:.6f}")
print(f"Persamaan: f(x) = {a:.5f} ln(x) {b:.5f} cos(x) + {c:.6f} e^x")


# Visualisasi Grafik
plt.figure(figsize=(10, 6))

# 1. Gambar titik data asli (merah)
plt.scatter(x, y, color='red', s=80, label='Data Asli (Tabel)', zorder=5)

# 2. Gambar kurva hasil regresi (biru)
# Kita buat 100 titik x baru dari x terkecil sampai terbesar agar kurvanya halus
x_curve = np.linspace(min(x), max(x), 100)
# Hitung y prediksi menggunakan a, b, c yang sudah ditemukan
y_curve = a * np.log(x_curve) + b * np.cos(x_curve) + c * np.exp(x_curve)

plt.plot(x_curve, y_curve, color='blue', linewidth=2.5, label='Kurva Fit Regresi')

# 3. Percantik grafik
plt.title('General Linear Least Squares: Evaluasi Kurva', fontsize=14)
plt.xlabel('Nilai X', fontsize=12)
plt.ylabel('Nilai Y', fontsize=12)

# Menambahkan kotak teks berisi persamaan di dalam grafik
eq_text = f'$f(x) = {a:.3f} \ln(x) - {abs(b):.3f} \cos(x) + {c:.4f} e^x$'
plt.text(1.0, 0.0, eq_text, fontsize=12, color='black', 
         bbox=dict(facecolor='white', edgecolor='blue', alpha=0.8, boxstyle='round,pad=0.5'))

plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Tampilkan grafik
plt.show()