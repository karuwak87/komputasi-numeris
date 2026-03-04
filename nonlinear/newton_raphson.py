def f(x):
    # Mendefinisikan fungsi f(x)
    return x**3 - 2*x**2 + x - 3

def f_prime(x):
    # Mendefinisikan turunan fungsi f'(x)
    return 3*x**2 - 4*x + 1

def newton_raphson_epsilon(x0, epsilon, max_iter=100):
    
    # Fungsi Newton-Raphson dengan kriteria berhenti epsilon
    # x0: tebakan awal
    # epsilon: batas ketelitian (toleransi error)
    # max_iter: batas aman maksimal iterasi

    x = x0
    print(f"Nilai awal: x = {x}")
    print("-" * 50)
    
    for i in range(1, max_iter + 1):
        fx = f(x)
        fpx = f_prime(x)
        
        if fpx == 0:
            print("Peringatan: Turunan bernilai nol, iterasi dihentikan.")
            break
            
        # Menghitung nilai x selanjutnya
        x_baru = x - (fx / fpx)
        selisih = abs(x_baru - x)
        
        print(f"Iterasi {i}: x = {x_baru:.6f} | selisih = {selisih:.6f}")
        
        # Kriteria berhenti: jika selisih < epsilon
        if selisih < epsilon:
            print("-" * 50)
            print(f"Berhasil! Kriteria epsilon tercapai pada iterasi ke-{i}.")
            return x_baru
            
        # Update nilai x untuk iterasi selanjutnya
        x = x_baru
        
    print("-" * 50)
    print(f"Peringatan: Iterasi mencapai batas maksimum ({max_iter})")
    return x

# --- Menjalankan Program ---
x_awal = 4
batas_ketelitian = 0.0001  # Epsilon (contoh: 10 pangkat -4)

akar_hampiran = newton_raphson_epsilon(x_awal, batas_ketelitian)
print(f"Hasil hampiran akar: {akar_hampiran:.6f}")