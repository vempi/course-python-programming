
# Pengantar: Mengapa Civil Engineer Perlu Bisa Coding?

> **Mata Kuliah:** Algoritma dan Pemrograman Komputer  
> **Program:** Program Sarjana Teknik Sumber Daya Air, Fakultas Teknik, Universitas Gadjah Mada  
> **Pertemuan:** 14 pertemuan  
> **Instruktur:** Vempi Satriya Adi Hendrawan, S.T., M.Env., Ph.D. · Muhammad Farizqi Khaldirian, S.T., M.Eng.

---

## Tujuan Pertemuan Ini

Setelah pertemuan pertama, mahasiswa diharapkan dapat:

1. Menjelaskan *mengapa* pemrograman relevan untuk seorang water resources engineer
2. Memahami gambaran besar isi kuliah dari pertemuan 1 hingga 14
3. Mengetahui tools yang akan digunakan selama kuliah (Python, Jupyter, GitHub)
4. Memahami aturan main kuliah — termasuk kebijakan penggunaan AI

---

## 1. Motivasi: Dunia Kerja Engineer Sekarang

Bayangkan skenario berikut:

> *Kamu adalah engineer di BBWS. Ada laporan banjir besar di DAS Bengawan Solo. Atasanmu minta analisis tren curah hujan 30 tahun terakhir, peta distribusi stasiun hujan, dan estimasi debit puncak — dalam 2 hari.*

**Pertanyaan untuk diskusi:**
- Kalau kamu kerjakan manual di Excel, berapa lama?
- Kalau kamu punya script Python yang bisa dijalankan ulang, berapa lama?
- Kalau script-nya bisa dimodifikasi oleh rekan kerjamu, berapa nilainya?

Inilah alasan utama mengapa coding bukan sekadar skill tambahan — ini adalah **multiplier** untuk kemampuan teknis yang sudah kamu miliki.

---

## 2. Python di Dunia Water Resources Engineering

Python adalah bahasa pemrograman paling populer di dunia sains dan rekayasa saat ini. Di bidang TSA khususnya, Python digunakan untuk:

| Kebutuhan | Contoh Aplikasi |
|-----------|-----------------|
| Pengolahan data hidrologi | Baca data AWLR/ARR, cleaning, statistik dasar |
| Analisis frekuensi banjir | Fit distribusi (Gumbel, Log-Pearson III), hitung kala ulang |
| Data spasial & GIS | Peta isohyet, interpolasi data hujan, analisis DAS |
| Data iklim (NetCDF/GRIB) | Ekstrak data CMIP6, ERA5, PERSIANN dari file gridded |
| Pemodelan sederhana | Hujan-limpasan (Rational Method, NRCS-CN), routing |
| Visualisasi & pelaporan | Grafik otomatis, dashboard, laporan PDF |

> **Catatan:** Semua modul dalam kuliah ini menggunakan dataset nyata — data hujan BMKG, data debit BPBD, data satelit — bukan data artificial.

---

## 3. Gambaran Kuliah 16 Pertemuan

```

POST-MIDTERM (M9–M16): APLIKASI TSA
┌─────────────────────────────────────────────────────┐
│  M8  │ Data akuisisi & pengolahan data hidrologi     │
│  M9 │ Analisis data hujan & debit                   │
│  M10 │ Data spasial: GIS & peta dengan Python        │
│  M11 │ Data spatio-temporal (NetCDF/3D)              │
│  M12 │ Statistik hidrologi                           │
│  M13 │ Advance plotting & visualisasi ilmiah         │
│  M14 │ Integrasi: membuat user interface sederhana   │
└─────────────────────────────────────────────────────┘
```

**Benang merahnya:** Setiap pertemuan menggunakan data TSA nyata. Kamu tidak akan pernah latihan dengan data buatan yang tidak bermakna.

---

## 4. Tools yang Akan Kita Gunakan

### 4.1 Python (via Anaconda/Miniconda)
Python adalah bahasa utama. Kita akan menggunakan Python 3.x dengan ekosistem library ilmiah:
- `numpy`, `pandas` → manipulasi data
- `matplotlib`, `seaborn` → visualisasi
- `scipy` → analisis statistik & numerik
- `geopandas`, `rasterio` → data spasial
- `xarray`, `netCDF4` → data gridded iklim

### 4.2 Jupyter Notebook / JupyterLab
Lingkungan kerja interaktif di mana kode, grafik, dan penjelasan bisa ada dalam satu dokumen. Format `.ipynb` akan menjadi format utama tugas dan laporan.

### 4.3 GitHub (Repository Kuliah)
Semua materi kuliah tersedia di:  
👉 **https://github.com/vempi/course-python-programming**

Mahasiswa didorong untuk:
- **Fork** repository ini ke akun GitHub masing-masing
- Simpan semua tugas di repository GitHub pribadi
- Belajar membuat commit yang bermakna (bukan hanya `update file`)

---

## 5. Aturan Main Kuliah

### 5.1 Penilaian
| Komponen | Bobot |
|----------|-------|
| Tugas Mingguan | 20% |
| Ujian Akhir Semester (UAS) | 50% |
| Partisipasi | 20% |
| Praktik Studio | 10% |

### 5.2 Kebijakan Penggunaan AI (Penting!)

Di kuliah ini, **penggunaan AI (ChatGPT, Claude, GitHub Copilot, dsb.) diizinkan** dengan syarat berikut:

✅ **Boleh:**
- Menggunakan AI untuk membantu *debug* kode
- Bertanya ke AI untuk memahami konsep yang belum jelas
- Menggunakan AI untuk mempercepat penulisan kode boilerplate
- Mendokumentasikan bantuan AI yang kamu gunakan

❌ **Tidak boleh:**
- Submit kode yang kamu sendiri tidak bisa jelaskan baris per baris
- Menyalin output AI tanpa memahami logikanya
- Menggunakan AI untuk menjawab soal UTS (closed-book)

> **Prinsipnya:** AI adalah asisten, bukan pengganti pemikiran. Kamu yang harus paham, AI yang bantu eksekusi. Dalam UTS dan presentasi, kamu akan diminta jelaskan kode yang kamu tulis — tanpa bantuan AI.

### 5.3 Proyek Akhir
Proyek akhir dikerjakan secara **berkelompok (2–3 orang)** dan menghasilkan:
1. Jupyter Notebook yang bisa dijalankan ulang (reproducible)
2. Presentasi 10 menit di pertemuan terakhir
3. README yang menjelaskan cara menjalankan kode

Topik proyek bebas selama relevan dengan TSA — analisis banjir, mapping hujan, model sederhana, dsb.

---

## 6. Setup Environment (Dikerjakan Sekarang!)

Ikuti langkah berikut sebelum pertemuan selesai:

### Langkah 1 — Install Anaconda atau Miniconda
Download dari: https://www.anaconda.com/download  
*(Miniconda direkomendasikan untuk laptop dengan storage terbatas)*

### Langkah 2 — Buat environment baru
```bash
conda create -n hydro-python python=3.11
conda activate hydro-python
```

### Langkah 3 — Install library dasar
```bash
conda install numpy pandas matplotlib scipy jupyter
```

### Langkah 4 — Uji instalasi
Buka Jupyter Notebook, buat file baru, jalankan kode berikut:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Setup berhasil!")
print(f"NumPy version: {np.__version__}")
print(f"Pandas version: {pd.__version__}")
```

Jika tidak ada error, setup kamu sudah siap. 🎉

### Langkah 5 — Buat akun GitHub (jika belum punya)
- Daftar di: https://github.com
- Fork repository kuliah: https://github.com/vempi/course-python-programming

---

## 7. Demo: Python Bisa Apa? (Live Coding)

Berikut contoh singkat yang akan didemonstrasikan di kelas — dari data mentah ke grafik dalam ~10 baris kode:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Simulasi data hujan harian (mm) selama sebulan
import numpy as np
np.random.seed(42)
tanggal = pd.date_range('2024-01-01', periods=30, freq='D')
hujan = np.random.exponential(scale=8, size=30)  # distribusi hujan tipikal

# Buat DataFrame
df = pd.DataFrame({'tanggal': tanggal, 'hujan_mm': hujan})

# Hitung statistik
print(f"Total hujan  : {df['hujan_mm'].sum():.1f} mm")
print(f"Hari hujan   : {(df['hujan_mm'] > 1).sum()} hari")
print(f"Hujan max    : {df['hujan_mm'].max():.1f} mm")

# Plot
fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(df['tanggal'], df['hujan_mm'], color='steelblue', alpha=0.7)
ax.set_xlabel('Tanggal')
ax.set_ylabel('Curah Hujan (mm)')
ax.set_title('Data Hujan Harian — Januari 2024')
plt.tight_layout()
plt.show()
```

> **Yang perlu diperhatikan:** 10 baris kode ini melakukan apa yang di Excel butuh klik-klik manual berkali-kali — dan bisa dijalankan ulang untuk bulan dan stasiun yang berbeda hanya dengan ganti 2 baris.

---

## 8. Penutup: Mindset yang Perlu Dibawa

Kuliah ini bukan tentang *menghafal syntax*. Kuliah ini tentang:

1. **Berpikir algoritmik** — memecah masalah besar menjadi langkah-langkah kecil yang bisa dikerjakan komputer
2. **Membangun kebiasaan** — coding adalah skill motorik, makin sering makin lancar
3. **Tidak takut error** — error bukan tanda gagal, itu adalah informasi tentang apa yang perlu diperbaiki
4. **Memanfaatkan komunitas** — Stack Overflow, dokumentasi resmi, dan AI adalah sumber daya yang sah

> *"You don't learn to code to become a programmer. You learn to code so the computer can work for you while you sleep."*

---

## Referensi & Bacaan Awal

- [Python for Data Analysis — Wes McKinney](https://wesmckinney.com/book/) *(open access)*
- [Hydrology with Python — Jupyter Notebook examples](https://github.com/vempi/course-python-programming)
- [Software Carpentry: Programming with Python](https://swcarpentry.github.io/python-novice-inflammation/)
- [Real Python Tutorials](https://realpython.com/) — untuk belajar mandiri

---

*Materi ini tersedia di: https://github.com/vempi/course-python-programming*  
*Last updated: 2026*
