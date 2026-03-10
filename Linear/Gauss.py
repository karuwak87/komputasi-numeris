def print_matrix(M):
    """Fungsi bantuan untuk mencetak matriks agar rapi"""
    for row in M:
        print(" | ".join([f"{val:8.1f}" for val in row]))
    print("-" * 60)

def gauss_elimination(A, b):
    n = len(b)
    
    # 1. Membuat Matriks Augmented (Menggabungkan A dan b)
    # M = [A | b]
    M = []
    for i in range(n):
        row = A[i].copy()
        row.append(b[i])
        M.append(row)
        
    print("Matriks Augmented Awal:")
    print_matrix(M)
    
    # 2. Forward Elimination (Eliminasi Maju)
    for i in range(n):
        # Mengecek apakah elemen diagonal (pivot) bernilai 0
        if M[i][i] == 0.0:
            print("Peringatan: Elemen pivot bernilai nol. Perlu teknik Partial Pivoting.")
            return None
            
        for j in range(i+1, n):
            # Menghitung rasio pengali untuk baris di bawahnya
            ratio = M[j][i] / M[i][i]
            
            # Mengurangi baris ke-j dengan (rasio * baris ke-i)
            for k in range(n+1):
                M[j][k] = M[j][k] - ratio * M[i][k]
                
        print(f"Matriks setelah eliminasi kolom ke-{i+1}:")
        print_matrix(M)
        
    # 3. Back Substitution (Substitusi Mundur)
    x = [0 for _ in range(n)]
    
    # Mencari nilai x terakhir (paling bawah)
    x[n-1] = M[n-1][n] / M[n-1][n-1]
    
    # Mencari nilai x dari bawah ke atas
    for i in range(n-2, -1, -1):
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax += M[i][j] * x[j]
        
        x[i] = (M[i][n] - sum_ax) / M[i][i]
        
    return x

# --- Bagian Input Soal ---
# Matriks A (Koefisien)
A = [
    [ 6.0,  -2.0,   2.0,   4.0],
    [12.0,  -8.0,   6.0,  10.0],
    [ 3.0, -13.0,   9.0,   3.0],
    [-6.0,   4.0,   1.0, -18.0]
]

# Vektor b (Konstanta)
b = [16.0, 26.0, -19.0, -34.0]

# Menjalankan fungsi
hasil_x = gauss_elimination(A, b)

# Menampilkan hasil akhir
if hasil_x is not None:
    print("=== HASIL AKHIR ===")
    for i in range(len(hasil_x)):
        print(f"x_{i+1} = {hasil_x[i]:.1f}")