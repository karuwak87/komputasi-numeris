def f(x):
    """Mendefinisikan fungsi f(x) = x^3 - 3x + 1"""
    return x**3 - 3*x + 1

def bisection_method(a, b, epsilon):
    # Start: Given a, b, and epsilon
    u = f(a)
    v = f(b)
    
    # Cek awal apakah ada akar dalam interval (syarat Bisection)
    if u * v >= 0:
        print("Metode bagi dua mungkin tidak berhasil. f(a) dan f(b) harus berbeda tanda.")
        return None

    # Memulai iterasi
    while True:
        # c = (a+b)/2 ; w = f(c)
        c = (a + b) / 2
        w = f(c)
        
        # is u*w < 0?
        if u * w < 0:
            # yes: b = c ; v = w
            b = c
            v = w
        else:
            # no: a = c ; u = w
            a = c
            u = w
            
        # is (b-a)/2 < epsilon?
        if (b - a) / 2 < epsilon:
            # yes -> Stop
            return c

# Nilai awal berdasarkan soal di gambar kedua
a = 0
b = 1

# Nilai epsilon (toleransi error) tidak disebutkan di soal, 
# jadi kita tentukan nilai yang kecil, misalnya 10^-5 (0.00001)
epsilon = 1e-5

# Menjalankan fungsi dan mencetak hasil
akar = bisection_method(a, b, epsilon)

if akar is not None:
    print(f"Akar perkiraan untuk fungsi tersebut pada interval [{a}, {b}] adalah: {akar:.5f}")
    print(f"Nilai f(x) pada akar tersebut adalah: {f(akar):.7f}")