from fractions import Fraction

def generate_lagrange_steps():
    # 1. Input data sesuai gambar
    x_data = [0, 1, 2, 3, 4]
    y_data = [1, 3, 2, 5, 4] # f(xi)
    n = len(x_data)
    
    print("="*60)
    print(" LANGRANGE INTERPOLATION STEP-BY-STEP ")
    print("="*60)
    
    # 2. Menampilkan Rumus Umum Summation
    suku_sum = []
    for i in range(n):
        if y_data[i] == 1:
            suku_sum.append(f"l_{i}")
        else:
            suku_sum.append(f"{y_data[i]}l_{i}")
            
    print(f"f_{n-1}(x) = {' + '.join(suku_sum)}\n")
    
    # 3. Menghitung dan Menampilkan Detail Tiap l_i
    for i in range(n):
        pembilang_str = ""
        penyebut_val = 1
        penyebut_str = ""
        
        for j in range(n):
            if i != j:
                # Membuat string pembilang: (x - xj)
                tanda = "-" if x_data[j] >= 0 else "+"
                val_x = abs(x_data[j])
                pembilang_str += f"(x {tanda} {val_x})"
                
                # Menghitung penyebut: (xi - xj)
                term_penyebut = x_data[i] - x_data[j]
                penyebut_val *= term_penyebut
                penyebut_str += f"({x_data[i]} - {x_data[j]})"
        
        # Cetak langkah per baris seperti di gambar
        print(f"l_{i} = {pembilang_str}   {pembilang_str}")
        print(f"     {' ' * len(pembilang_str)} = {'-' * len(pembilang_str)}")
        print(f"     {penyebut_str}   {penyebut_val}")
        print("-" * 40)

if __name__ == "__main__":
    generate_lagrange_steps()