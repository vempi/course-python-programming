---
# Capaian pembelajaran Pertemuan-8
  1. [Mengetahui Tipe data hidrologi](#1-tipe-data-hidrologi)
  2. [Dapat mengunduh berbagai tipe data hujan](#2-mengunduh-data-hujan)
  3. [Read and write rainfall data](#3-Read-and-write-data-hujan)
  4. [Data cleaning](#4-Data-cleaning)
---

# 1. Tipe data Hidrologi

Pengumpulan data dasar yang dilakukan meliputi pengukuran curah hujan dan penguapan, serta pengukuran kedalaman air dan pengukuran aliran sungai. Berikut ini mencakup penjelasan singkat dari sistem pengumpulan data utama khususnya hujan yang digunakan dalam analisis informasi hidrologi.

### I. Instrumen Pengukuran curah hujan
Data curah hujan diperoleh dari 3 jenis instrumen: pos pengukur hujan, radar, dan satelit.

| No | Metode Pengukuran | Deskripsi |
|----|-------------------|-----------|
| 1  | Pos Pengukur Hujan (Raingauge) | Mengukur kedalaman curah hujan di titik tertentu dengan menangkap air hujan ke dalam wadah pengumpul. Pengukuran dapat dilakukan per jam, harian, atau bulanan. Alat ini bisa manual atau otomatis (Automatic Rainfall Raingage). Dioperasikan oleh berbagai institusi seperti Kementerian PUPR, BMKG, Dinas PU daerah, dan Balai SDA daerah. |
| 2  | Radar | Menggunakan daya elektromagnetik (backscatter) dari sinyal radiofrekuensi yang dikirim ke akumulasi awan hujan. Mampu mencatat intensitas curah hujan dalam radius hingga 100 km. |
| 3  | Teknologi Satelit | Mengukur radiasi termal dan mencatat intensitas curah hujan secara global. Contoh teknologi: CHIRPS, GSMAP, GPM, PERSIANN. |

![Picture1](https://github.com/vempi/course-python-programming/assets/34568583/87dddb19-73d2-44b0-945d-49e041e109c8)
Gambar diolah dari[ Sun et al. (2017)](https://doi.org/10.1002/2017RG000574)  

Dengan membandingkan pengukuran-pengukuran yang berbeda diatas, karakteristik intensitas curah hujan titik dan curah hujan area, baik nilai sesaat maupun terakumulasi, dapat diperoleh dan didiskusikan. 
Pengukuran curah hujan langsung melalui pos pengukur hujan akan sangat bermanfaat untuk menyediakan kalibrasi lokal dari data radar dan satelit. Sedangkan data radar dan satelit dapat memberikan indikasi nilai puncak sesaat yang lebih baik dari segi kerapatan waktu dibandingkan dengan pengukur hujan yang beroperasi selama periode waktu dan memerlukan kunjungan ke lokasi yang sering oleh petugas. Perbandingan antar data-data tersebut dan akurasinya sangat dan berharga dalam rangka membangun sistem peringkatan dini  _early warning_ dalam menghadapi kejadian-kejadian esktrem (hujan badai, banjir, dsb.).

### II. Skala waktu pengukuran hujan
Penggunaan data dari pengukur hujan dapat dibedakan berdasarkan interval waktu di mana data tersebut dikumpulkan atau dirata-ratakan, yaitu sebagai berikut:

| No | Jenis Data | Penggunaan |
|----|-----------|------------|
| 1  | **Data Tahunan** | Digunakan untuk studi ketersediaan air dan kekeringan dengan mempertimbangkan tahun-tahun basah dan kering. |
| 2  | **Data Bulanan** | Digunakan untuk studi ketersediaan air, neraca air, indeks kekeringan, serta kalibrasi data hujan harian dan data debit sungai menggunakan model hidrologi DAS atau stokastik. |
| 3  | **Data Harian** | Digunakan untuk model banjir, model hidrologi DAS, serta model kelembaban tanah untuk pertanian. |
| 4  | **Data Per Jam** | Digunakan untuk analisis banjir desain DAS dan perkotaan dengan skala waktu yang lebih rapat. |


Masalah dari pengukuran curah hujan adalah bahwa jumlah pengamatan pos _raingauge_ semakin berkurang dan keterbatasann pencatatan terlebih jika pos diamati secara manual oleh petugas. Oleh karena itu, seringkali terdapat data kosong, celah dan kesalahan serta kurangnya data dengan resolusi tinggi secara spasial dan temporal. Selain itu terdapat bias yang besar khususnya untuk perkiraan spasial untuk durasi waktu yang pendek.

# 2. Mengunduh Data hujan

1. Data Raingauge yang dimiliki oleh BMKG: https://dataonline.bmkg.go.id/home
2. Data Satelit

   a. GSMAP melalui [website JAXA](https://sharaku.eorc.jaxa.jp/GSMaP/)
   b. PERSIANN: [https://chrsdata.eng.uci.edu/]
   c. GPM: [https://giovanni.gsfc.nasa.gov/giovanni/]
   d. Others: [https://app.climateengine.org/]

Untuk panduan kuliah ini, silahkan download data hujan pada link berikut (gunakan EMAIL Google UGM):
https://drive.google.com/file/d/1tkxLyisrqBiWrey4tFGM4odWTCzdnY-4/view?usp=sharing

Data curah hujan ini telah diolah dan dihimpun dari data beberapa sumber satelit (GSMAP, GPM, PERSIANN, CHIRPS).
Detil metodenya akan disampaikan di panduan yang akan datang.

# 3. Read and write data hujan

---
Contoh mengolah data hujan pos (_raingauge_) menggunakan Python
---

Berikut tutorial contoh sederhana mengolah data hujan dalam bentuk tabel (csv, excel) menggunakan Python.
Jangan lupa untuk download [file data curah hujan harian](https://drive.google.com/file/d/1tkxLyisrqBiWrey4tFGM4odWTCzdnY-4/view?usp=sharing) diatas, yang didalam penulisan coding di bawah ini adalah "Data_hujan_multi_harian.csv".

![image](https://github.com/vempi/course-python-programming/assets/34568583/0da47cd9-a2c0-4a00-a8ef-e1ab089b3afc)

Link Video: (https://www.youtube.com/watch?v=CPTw-HKk5Ss)

Berikut teks coding yang digunaan pada tutorial diatas.

```python
import pandas as pd
import matplotlib.pyplot as plt
import calendar
import os,glob

# Set directory
os.chdir("E:/Downloads/")

# =========================== 1. Hujan Harian Maks =========================== #
# Membaca data curah hujan/debit dari file CSV
f = "Data_hujan_multi_harian.csv"
df = pd.read_csv(f)

# Remove blank rows
df = df.dropna()

# Convert date column to date format 
df['Date'] = df['Date'].apply(lambda x: pd.to_datetime(x, format="%m/%d/%Y"))

# get Hujan harian maksimum tahunan "HMT"
ann = df.groupby(df['Date'].dt.year).max()

# save
ann.to_csv('ann-max_'+f)

# make date as x axis index of the plot
ann = ann.set_index('Date')

# PLot as image
ann.plot()
plt.ylabel('Annual Maximum Rainfall (mm/day)')
plt.savefig('test.jpg')
```
![image](https://github.com/vempi/course-python-programming/assets/34568583/6c6a12ed-1ed9-4551-b1f1-606eaf86dbf3)


```python
# ================================ 2. Bulanan ================================ #

# Grouping menjadi data bulanan
df['year_month'] = df['Date'].dt.to_period('M')

# Penjumlahan seluruh hujan harian tiap bulan
m = df.groupby('year_month').sum()

# save and plot
m.to_csv('monthly-sum_'+f)
m.plot()
```
![image](https://github.com/vempi/course-python-programming/assets/34568583/3b83bfb6-fd52-4ffd-a25c-7fd0880f4caf)

---
# 4. Data cleaning
Dataset sumber daya air memiliki beberapa masalah umum yang ditemukan, seperti nilai yang hilang, format tanggal yang tidak konsisten, dan nilai yang ekstrem (outlier). 
Pertama, mari buat contoh dataset yang masih terdapat belum dibersihkan tsb.:

```python
import pandas as pd
import numpy as np

# Generate an hypotetical dataset
np.random.seed(0)
dates = pd.date_range('2022-01-01', periods=100)

# Data akan dibuat sebagai "string"
rainfall = np.random.randint(0, 20, size=100).astype(str)
discharge = np.random.randint(50, 100, size=100).astype(str)

# Introduce missing values
rainfall[10:15] = '-'
rainfall[16:20] = 'kosong'
discharge[30:35] = 'Alat rusak'
discharge[36:40] = '  '

# Introduce missing values
rainfall[50:55] = np.nan
discharge[55:60] = np.nan

# Introduce inconsistent date format
dates = dates.strftime('%d/%m/%Y')

# Create DataFrame
dirty_df = pd.DataFrame({'Date': dates, 'Rainfall': rainfall, 'Discharge': discharge})

# Display first few rows
print(dirty_df.head())
```

Kita telah memiliki dataset yang harus dibersihkan.
Contoh item pembersihan antara lain:
- Format Tanggal: Mengonversi tanggal ke format yang konsisten (misalnya, 'YYYY-MM-DD').
- Nilai yang Hilang: Mengisi nilai yang hilang menggunakan metode yang sesuai.
- Nilai Ekstrem: menghapus nilai ekstrem dalam data.
- Menghapus karakter yang tidak diinginkan

Dalam contoh ini, kita menggunakan replace untuk mengganti nilai-nilai yang tidak terduga seperti "/", ".", "NA", dan "kosong" dengan nilai NaN. 
Kemudian, kita mengonversi kolom 'Rainfall' dan 'Discharge' ke float dengan mengabaikan nilai-nilai yang tidak dapat dikonversi. 
Hasilnya adalah dataset yang sudah dibersihkan dan siap untuk analisis lebih lanjut.

```python


# Clean the "dirty" dataset
clean_df = dirty_df.copy()

# Fix date format
clean_df['Date'] = pd.to_datetime(clean_df['Date'], errors='coerce')

# Code ini hanya akan mengonversi ke numeric untuk string yang berisi angka
# Yang tidak terdeteksi sebagai angka akan diabaikan atau menjadi np.nan `errors='coerce'` 
clean_df['Discharge'] = pd.to_numeric(clean_df['Discharge'], errors='coerce')

# Handle outliers (for demonstration, kita ganti nilai debit diatas 200 dengan median)
# Anda juga bisa mengganti dengan angka lain misal: np.nan
med = clean_df['Discharge'].median()
clean_df.loc[clean_df['Discharge'] > 200, 'Discharge'] = med

# Display cleaned DataFrame
print("After cleaning:")
print(clean_df.head())

# plot after cleaned
clean_df.set_index('Date',inplace=True)
clean_df.plot()

```


---
# Check Pembelajaran Pertemuan-8 (Kuis singkat)
  1. Ditahun berapa hujan harian maksimum (HMT) tertinggi tercatat (berdasarkan 4 sumber data hujan tersebut). Apakah 4 summber data tersebut menunjukkan hasil yang identik?
  2. Berapa rerata HMT sepanjang tahun 2001-2022 untuk masing-masing sumber data hujan?
  3. Sumber data apa yang menunjukkan tendensi nilai HMT yang lebih rendah dan tinggi dibandingkan dengan data lain?
---
