def print_matrix(M):
    """Fungsi bantuan untuk mencetak matriks agar rapi"""
    for row in M:
        print(" | ".join([f"{val:8.1f}" for val in row]))
    print("-" * 65)

def gauss_jordan(A, b):
    n = len(b)
    
    # 1. Membuat Matriks Augmented
    M = []
    for i in range(n):
        row = A[i].copy()
        row.append(b[i])
        M.append(row)
        
    print("Matriks Augmented Awal:")
    print_matrix(M)
    
    # 2. Proses Eliminasi Gauss-Jordan
    for i in range(n):
        if M[i][i] == 0.0:
            print("Peringatan: Elemen pivot bernilai nol. Perlu teknik Partial Pivoting.")
            return None
        
        # Langkah A: Membagi baris pivot agar elemen diagonalnya menjadi 1
        pivot = M[i][i]
        for j in range(n + 1):
            M[i][j] = M[i][j] / pivot
            
        # Langkah B: Eliminasi baris LAIN (di atas dan di bawah pivot) agar menjadi 0
        for k in range(n):
            if k != i:
                pengali = M[k][i]
                for j in range(n + 1):
                    M[k][j] = M[k][j] - pengali * M[i][j]
                    
        print(f"Matriks setelah proses pivot baris/kolom ke-{i+1}:")
        print_matrix(M)
        
    # 3. Solusi langsung diambil dari kolom paling kanan
    x = [M[i][n] for i in range(n)]
    return x

# --- Bagian Input Soal 3x3 Terbaru ---
A = [
    [ 2.0, -2.0,  2.0],
    [ 4.0,  2.0, -1.0],
    [ 2.0, -2.0,  4.0]
]

b = [0.0, 7.0, 2.0]

# Menjalankan fungsi
hasil_x = gauss_jordan(A, b)

# Menampilkan hasil akhir
if hasil_x is not None:
    print("=== HASIL AKHIR GAUSS-JORDAN ===")
    for i in range(len(hasil_x)):
        print(f"x_{i+1} = {hasil_x[i]:.1f}")