import numpy as np

def cetak_tabel_newton():
    # 1. Masukkan data dari gambar
    x = np.array([2, 4, 5, 6, 7])
    y = np.array([3, 5, 1, 6, 9], dtype=float)
    n = len(x)
    
    # 2. Siapkan matriks untuk tabel selisih terbagi
    tabel = np.zeros([n, n])
    tabel[:, 0] = y
    
    # 3. Hitung selisih terbagi
    for j in range(1, n):
        for i in range(n - j):
            tabel[i][j] = (tabel[i+1][j-1] - tabel[i][j-1]) / (x[i+j] - x[i])
            
    # ==========================================
    # BAGIAN A: CETAK TABEL (Seperti Gambar)
    # ==========================================
    print("="*75)
    # Cetak Header
    header = "x\t| f(x)\t| " + " | ".join([f"f[ {',' * i} ]\t" for i in range(1, n)])
    print(header)
    print("-" * 75)
    
    # Cetak Isi Tabel
    for i in range(n):
        baris = f"{x[i]}\t| "
        for j in range(n - i):
            nilai = tabel[i][j]
            # Format tampilan agar rapi (4 angka di belakang koma jika desimal)
            if nilai.is_integer():
                baris += f"{int(nilai)}\t| "
            else:
                baris += f"{nilai:.4f}\t| "
        print(baris)
    print("="*75)
    
    # ==========================================
    # BAGIAN B: CETAK PERSAMAAN (Seperti Gambar)
    # ==========================================
    koefisien = tabel[0, :] # Ambil baris paling atas (yang berwarna merah di gambar)
    
    # Mulai susun string persamaan
    persamaan = f"f_{n-1} = {int(koefisien[0]) if koefisien[0].is_integer() else f'{koefisien[0]:.4f}'}"
    
    for i in range(1, n):
        nilai_koef = koefisien[i]
        tanda = "+" if nilai_koef >= 0 else "-"
        nilai_absolut = abs(nilai_koef)
        
        # Format koefisien
        if nilai_absolut.is_integer():
            str_koef = f"{int(nilai_absolut)}"
        else:
            str_koef = f"{nilai_absolut:.4f}"
            
        # Susun bagian (x - x0)(x - x1)...
        suku_x = ""
        for j in range(i):
            suku_x += f"(x - {x[j]})"
            
        persamaan += f" {tanda} {str_koef}{suku_x}"
        
    print("\nPersamaan yang terbentuk:")
    print(persamaan)

if __name__ == "__main__":
    cetak_tabel_newton()