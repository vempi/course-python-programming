<blockquote style="background-color: #f9f9f9; border-left: 5px solid #ccc; padding: 10px;">
This is a callout box. You can use it to highlight important information or provide additional context.
</blockquote>

# Hidraulika Saluran Terbuka 1D (Manning-Strickler Formula)
## Persamaan Manning
Persamaan ini adalah rumus empiris dalam hidraulika saluran terbuka yang mendeskripsikan hubungan antara kecepatan di dalam saluran (V) dan geometri lebar dan kedalaman saluran (B,H), kemiringan (S), dan koefisien gesekan yang dinyatakan sebagai koefisien Manning n.

![image](https://github.com/vempi/course-python-programming/assets/108465312/7f6e0748-5a19-4e88-a11f-8fa7c4cb3e97)
$Q = \frac{\sqrt{S} (BH)^{5/3}}{n (B+2H)^{2/3}}$

## Metode Iterasi
Metode iterasi dilakukan untuk menghitung nilai kedalaman sementara parameter lainnya diketahui. Nilai variabel kedalaman dalam persamaan Manning yang memiliki derajat ganda dapat diselesaikan dengan melakukan iterasi perhitungan kedalaman secara terus menerus hingga nilai kedalaman pada iterasi ke n mendekati nilai kedalaman iterasi ke n-1.
Persamaan Manning dapat diubah menjadi bentuk pengulangan

$H_{i+1} =  \frac{1}{B} \left( \frac{nQ(B+2H_{i})^{2/3}}{\sqrt{S}} \right)^{3/5}$




---
Contoh mengolah perhitungan kedalaman saluran menggunakan Python
---

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ── Data saluran (langsung bisa dijalankan, tidak perlu file eksternal!) ───────
# Kolom: [No. Saluran, Q (m³/s), S (kemiringan), n (Manning), B (lebar, m)]
data_saluran = np.array([
    [1,  5.0,  0.001, 0.025, 3.0],
    [2,  8.0,  0.002, 0.030, 4.0],
    [3, 12.0,  0.0005,0.020, 5.0],
    [4,  3.0,  0.003, 0.035, 2.5],
    [5, 20.0,  0.001, 0.025, 6.0],
])
# ── Untuk data dari file TXT: ─────────────────────────────────────────────────
# with open('Channel_data.txt', 'r') as file:
#     next(file)
#     data_saluran = np.array([line.strip().split() for line in file], dtype=float)
# ─────────────────────────────────────────────────────────────────────────────

Ch    = data_saluran[:, 0]
Q     = data_saluran[:, 1]
S0    = data_saluran[:, 2]
nm    = data_saluran[:, 3]
B     = data_saluran[:, 4]
ndata = len(Q)

# ── Fungsi iterasi kedalaman normal Manning ────────────────────────────────────
def kedalaman_normal(Q, n, S, B, toleransi=0.001, maks_iterasi=1000):
    """Hitung kedalaman normal H untuk setiap saluran dengan iterasi."""
    ndata = len(Q)
    H = np.ones(ndata) * 0.5   # tebakan awal kedalaman 0.5 m

    for k in range(ndata):
        for _ in range(maks_iterasi):
            H_baru = ((Q[k] * n[k] * (B[k] + 2 * H[k]) ** (2/3)
                       / S[k] ** 0.5) ** (3/5)) / B[k]
            if abs(H_baru - H[k]) < toleransi:
                H[k] = H_baru
                break
            H[k] = H_baru

    return H

H = kedalaman_normal(Q, nm, S0, B)

# ── Tampilkan hasil ────────────────────────────────────────────────────────────
hasil = pd.DataFrame({
    'Saluran' : Ch.astype(int),
    'Q (m³/s)': Q,
    'S'       : S0,
    'n'       : nm,
    'B (m)'   : B,
    'H (m)'   : H.round(3)
})
print(hasil.to_string(index=False))

# Hitung debit balik (verifikasi): Q_check = (1/n)*A*R^(2/3)*S^(1/2)
A       = B * H
P       = B + 2 * H
R       = A / P
Q_check = (1 / nm) * A * R ** (2/3) * S0 ** 0.5
print(f"\nVerifikasi — maks. error Q: {np.abs(Q - Q_check).max():.4f} m³/s")

# ── Simpan ke file ─────────────────────────────────────────────────────────────
output = np.column_stack([Ch, Q, S0, nm, B, H])
header = "Saluran\tQ\tS\tnm\tB\tH"
np.savetxt('Output_Manning.txt', output, fmt='%.3f', delimiter='\t',
           header=header, comments='')
print("Hasil disimpan ke Output_Manning.txt")

# ── Plot: kedalaman vs debit untuk setiap saluran ─────────────────────────────
plt.figure(figsize=(8, 5))
plt.bar([f'S-{int(c)}' for c in Ch], H, color='steelblue', edgecolor='black', alpha=0.8)
for i, (h, q) in enumerate(zip(H, Q)):
    plt.text(i, h + 0.02, f'Q={q:.0f}\nH={h:.2f}m', ha='center', fontsize=9)
plt.ylabel('Kedalaman Normal H (m)', fontsize=12)
plt.xlabel('Nomor Saluran', fontsize=12)
plt.title('Kedalaman Normal Saluran – Persamaan Manning', fontsize=13)
plt.tight_layout()
plt.savefig('manning_kedalaman.png', dpi=150)
plt.show()
```