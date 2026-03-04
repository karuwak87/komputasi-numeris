def f(x):
    #Mendefinisikan fungsi f(x)
    return x**5 + x**3 + 3

def metode_secant(x0, x1, epsilon, max_iter=100):
    
    #Fungsi untuk menjalankan iterasi Metode Secant
    #x0, x1: dua tebakan awal
    #epsilon: batas ketelitian (toleransi error)
    #max_iter: batas aman maksimal iterasi
    
    print(f"Nilai awal: x0 = {x0}, x1 = {x1}")
    print("-" * 55)
    
    for i in range(1, max_iter + 1):
        fx0 = f(x0)
        fx1 = f(x1)
        
        # Mencegah pembagian dengan nol
        if fx1 - fx0 == 0:
            print("Peringatan: f(x1) - f(x0) bernilai nol. Pembagian dengan nol, iterasi dihentikan.")
            break
            
        # Rumus Metode Secant dari gambar
        # x_baru = x1 - f(x1) * [(x1 - x0) / (f(x1) - f(x0))]
        x_baru = x1 - fx1 * ((x1 - x0) / (fx1 - fx0))
        
        # Menghitung error (selisih x baru dengan x sebelumnya)
        error = abs(x_baru - x1)
        
        print(f"Iterasi {i}: x = {x_baru:.6f} | error = {error:.6f}")
        
        # Kriteria berhenti: jika error < epsilon
        if error < epsilon:
            print("-" * 55)
            print(f"Berhasil! Kriteria error < {epsilon} tercapai pada iterasi ke-{i}.")
            return x_baru
            
        # Update nilai x0 dan x1 untuk iterasi selanjutnya
        # x1 bergeser menjadi x0, dan x_baru bergeser menjadi x1
        x0 = x1
        x1 = x_baru
        
    print("-" * 55)
    print(f"Peringatan: Iterasi mencapai batas maksimum ({max_iter})")
    return x1

# --- Menjalankan Program ---
x_awal_0 = -1.0
x_awal_1 = -1.1
batas_error = 0.001

akar_hampiran = metode_secant(x_awal_0, x_awal_1, batas_error)
print(f"Hasil hampiran akar: {akar_hampiran:.6f}")