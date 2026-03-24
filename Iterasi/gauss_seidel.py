def gauss_seidel_iteration(A, b, tebakan_awal, epsilon, max_iter=100):
    n = len(b)
    x = tebakan_awal.copy()
    
    # Membuat header tabel
    header_x = " | ".join([f"x_{i+1:<8}" for i in range(n)])
    print(f"{'Iterasi':<9} | {header_x} | {'Error':<10}")
    print("-" * (25 + 11 * n))
    
    # Cetak tebakan awal
    awal_str = " | ".join([f"{val:10.5f}" for val in x])
    print(f"{0:<9} | {awal_str} | {'-':<10}")
    
    # Memulai perulangan iterasi
    for iterasi in range(1, max_iter + 1):
        x_lama = x.copy() # Simpan state lama khusus untuk menghitung error nanti
        
        for i in range(n):
            if A[i][i] == 0:
                print(f"Metode gagal: Elemen diagonal A[{i}][{i}] bernilai nol.")
                return None
                
            sum_ax = 0.0
            for j in range(n):
                if i != j:
                    # PERBEDAAN KUNCI: x[j] di sini otomatis memakai nilai terbaru
                    # jika nilai tersebut sudah dihitung di baris sebelumnya.
                    sum_ax += A[i][j] * x[j]
                    
            # Rumus Iterasi Gauss-Seidel (sama dengan Jacobi, tapi x langsung di-update)
            x[i] = (b[i] - sum_ax) / A[i][i]
            
        # Menghitung error dengan membandingkan x yang baru selesai dengan x_lama
        error = max([abs(x[i] - x_lama[i]) for i in range(n)])
        
        # Cetak hasil iterasi
        x_str = " | ".join([f"{val:10.5f}" for val in x])
        print(f"{iterasi:<9} | {x_str} | {error:10.5f}")
        
        # Kondisi berhenti
        if error < epsilon:
            print("-" * (25 + 11 * n))
            print(f"Berhenti pada iterasi ke-{iterasi} karena error < epsilon")
            return x
            
    print("-" * (25 + 11 * n))
    print("Peringatan: Iterasi mencapai batas maksimal tanpa mencapai konvergensi.")
    return x

A = [
    [ 10.0, -3.0,  6.0],
    [  1.0,  8.0, -2.0],
    [ -2.0,  4.0, -9.0]
]

b = [24.5, -9.0, -50.0]

# Tebakan awal dan batas error
tebakan_awal = [0.0, 0.0, 0.0]
batas_error = 1e-5

# Menjalankan fungsi
hasil_x = gauss_seidel_iteration(A, b, tebakan_awal, batas_error)

# Menampilkan hasil akhir
if hasil_x is not None:
    print("\n=== HASIL AKHIR ITERASI GAUSS-SEIDEL ===")
    print(f"x = {hasil_x[0]:.5f}")
    print(f"y = {hasil_x[1]:.5f}")
    print(f"z = {hasil_x[2]:.5f}")