# Simulasi Neraca Air DAS Menggunakan Model Thornthwaite-Mather

## Deskripsi Kasus
Neraca air suatu daerah aliran sungai (DAS) ditentukan oleh keseimbangan antara curah hujan, evapotranspirasi, limpasan permukaan, dan perubahan kelembaban tanah. Model Thornthwaite-Mather adalah salah satu metode sederhana untuk mensimulasikan keseimbangan air dalam suatu DAS dengan mempertimbangkan kelembaban tanah sebagai faktor utama.

Model ini menggunakan persamaan keseimbangan air:

$$\Delta S = P - ET_a - R$$

di mana:

- $$\Delta S$$ = perubahan kelembaban tanah (mm)  
- $$P$$ = curah hujan (mm)  
- $$ET_a$$ = evapotranspirasi aktual (mm)  
- $$R$$ = limpasan permukaan (mm)  

Evapotranspirasi aktual dihitung berdasarkan evapotranspirasi potensial ($$ET_p$$) dengan:

- Jika $$P \geq ET_p \Rightarrow ET_a = ET_p$$  
- Jika $$P < ET_p \Rightarrow ET_a = P + (\text{cadangan air tanah})$$  

Limpasan permukaan ($$R$$) dihitung dengan pendekatan:  
- Jika kapasitas tanah sudah penuh, kelebihan air akan menjadi limpasan.  

## Studi Kasus  
Diberikan data curah hujan harian ($$P$$) selama 30 hari untuk sebuah DAS kecil dengan parameter:

- **Kapasitas tampungan air tanah** ($$S_{\max}$$) = 100 mm  
- **Evapotranspirasi potensial harian** ($$ET_p$$) = 4 mm/hari  
- **Curah hujan harian** ($$P$$) = $$\{3, 0, 0, 5, 10, 0, 0, 2, 8, 20, \dots\}$$ (acak selama 30 hari)  

### Tugas Anda:
1. **Menghitung neraca air harian selama 30 hari dengan mempertimbangkan:**
   - Evapotranspirasi aktual
   - Perubahan kelembaban tanah
   - Limpasan permukaan
2. **Menggunakan iterasi numerik untuk memperbarui kondisi kelembaban tanah setiap hari.**
3. **Menampilkan hasil dalam bentuk tabel dan grafik.**
4. **Menganalisis dampak perubahan curah hujan dan kapasitas tampungan tanah terhadap keseimbangan air DAS.**

## Implementasi dalam Python

Berikut adalah kode Python untuk mensimulasikan neraca air menggunakan model Thornthwaite-Mather:

```python
import numpy as np
import matplotlib.pyplot as plt

# Parameter
S_max = 100  # Kapasitas tampungan air tanah (mm)
ET_p = 4  # Evapotranspirasi potensial (mm/hari)
P = [3, 0, 0, 5, 10, 0, 0, 2, 8, 20, 5, 3, 7, 1, 0, 12, 4, 6, 0, 0, 9, 2, 4, 0, 5, 8, 3, 10, 0]  # Curah hujan harian (mm)

# Inisialisasi variabel
S = 50  # Kondisi awal kelembaban tanah (mm)
S_list = []
ET_a_list = []
R_list = []

# Iterasi harian
for p in P:
    if p >= ET_p:
        ET_a = ET_p
    else:
        ET_a = min(S + p, ET_p)
    
    S_new = S + p - ET_a
    if S_new > S_max:
        R = S_new - S_max
        S_new = S_max
    else:
        R = 0
    
    S = S_new
    S_list.append(S)
    ET_a_list.append(ET_a)
    R_list.append(R)

# Visualisasi
plt.figure(figsize=(10,5))
plt.plot(S_list, label='Kelembaban Tanah (S)', marker='o')
plt.plot(ET_a_list, label='Evapotranspirasi Aktual (ET_a)', linestyle='--')
plt.plot(R_list, label='Limpasan Permukaan (R)', linestyle=':')
plt.xlabel('Hari')
plt.ylabel('mm')
plt.legend()
plt.title('Simulasi Neraca Air DAS')
plt.grid()
plt.show()
```

## Tambahan Tantangan:
✅ Tambahkan komponen aliran bawah tanah (baseflow) untuk model yang lebih kompleks.  
✅ Gunakan data curah hujan dan evapotranspirasi harian dari sumber nyata (misalnya BMKG).  
✅ Visualisasi grafik keseimbangan air DAS dalam bentuk grafik batang dan garis.  

## Keterampilan Python yang Diuji:
✅ Iterasi numerik untuk simulasi neraca air harian  
✅ Array dan perhitungan numerik menggunakan NumPy  
✅ Visualisasi data menggunakan Matplotlib

