---
# Capaian pembelajaran Pertemuan-8
  1. Mengetahui Tipe data hidrologi
  2. Dapat mengunduh bermacam-macam tipe data hujan
  3. Read and write rainfall data
  4. Data cleaning
---

<h1>&#x2713; Tipe data Hidrologi </h1>

Pengumpulan data dasar yang dilakukan meliputi pengukuran curah hujan dan penguapan, serta pengukuran kedalaman air dan pengukuran aliran sungai. Berikut ini mencakup penjelasan singkat dari sistem pengumpulan data utama khususnya hujan yang digunakan dalam analisis informasi hidrologi.

### 1. Instrumen Pengukuran curah hujan
Data curah hujan diperoleh dari 3 jenis instrumen: pos pengukur hujan, radar, dan satelit.

a. **Pos pengukur hujan (_raingauge_)** mengukur kedalaman curah hujan titik yang terakumulasi selama periode tertentu di stasiun-stasiun tertentu dengan cara menangkap langsung ke dalam wadah pengumpul (per jam, harian, bulanan, dan sebagainya). Alat ini dioperasikan dan dimonitor oleh petugas pengamat secara manual atau tercatat secara otomatis (Automatic Rainfall Raingage). Di indonesia pos pengukur hujan dimiliki oleh banyak institusi seperti Kementerian PUPR, BMKG, Dinas-dinas Pekerjaan Umum daerah, dan Balai SDA daerah.

b. **Radar** menggunakan daya elektromagnetik (backscatter) dari sinyal radiofrekuensi yang dikirim menuju akumulasi awan hujan. Intensitas curah hujan dicatat di wilayah-wilayah sekitar biasanya dengan radius hingga 100 km.

c. **Teknologi satelit** mengukur radiasi yang dipancarkan (termal) dan mencatat tingkat intensitas curah hujan pada setiap saat di seluruh wilayah (skala global) (misalnya, CHIRPS, GSMAP, GPM, PERSIANN).

Dengan membandingkan pengukuran-pengukuran yang berbeda diatas, karakteristik intensitas curah hujan titik dan curah hujan area, baik nilai sesaat maupun terakumulasi, dapat diperoleh dan didiskusikan. 
Pengukuran curah hujan langsung melalui pos pengukur hujan akan sangat bermanfaat untuk menyediakan kalibrasi lokal dari data radar dan satelit. Sedangkan data radar dan satelit dapat memberikan indikasi nilai puncak sesaat yang lebih baik dari segi kerapatan waktu dibandingkan dengan pengukur hujan yang beroperasi selama periode waktu dan memerlukan kunjungan ke lokasi yang sering oleh petugas. Perbandingan antar data-data tersebut dan akurasinya sangat dan berharga dalam rangka membangun sistem peringkatan dini  _early warning_ dalam menghadapi kejadian-kejadian esktrem (hujan badai, banjir, dsb.).

### 2. Skala waktu pengukuran hujan
Penggunaan data dari pengukur hujan dapat dibedakan berdasarkan interval waktu di mana data tersebut dikumpulkan atau dirata-ratakan, yaitu sebagai berikut:

a. **Data Tahunan** digunakan untuk studi ketersediaan air dan kekeringan dengan mempertimbangkan tahun-tahun basah dan kering.

b. **Data Bulanan** dapat digunakan untuk studi ketersediaan air dan neraca air, kekeringan (indeks kekeringan), serta digunakan untuk mengkalibrasi data hujan harian dan data debit aliran sungai dengan menggunakan model hidrologi daerah tangkapan air (atau DAS) maupun stokastik. 

c. **Data Harian** digunakan untuk model banjir, model hidrologi DAS, serta model kelembaban tanah untuk pertanian.

d. **Data Per Jam** digunakan untuk analisis banjir desain DAS, perkotaan, dengan skala waktu yang lebih rapat.


Masalah dari pengukuran curah hujan adalah bahwa jumlah pengamatan pos _raingauge_ semakin berkurang dan keterbatasann pencatatan terlebih jika pos diamati secara manual oleh petugas. Oleh karena itu, seringkali terdapat data kosong, celah dan kesalahan serta kurangnya data dengan resolusi tinggi secara spasial dan temporal. Selain itu terdapat bias yang besar khususnya untuk perkiraan spasial untuk durasi waktu yang pendek.

<h1>&#x2713; Mengunduh Data hujan </h1>

1. Data Raingauge yang dimiliki oleh BMKG: https://dataonline.bmkg.go.id/home
2. Data Satelit
   a. GSMAP melalui [website JAXA](https://sharaku.eorc.jaxa.jp/GSMaP/)
   b. PERSIANN: https://chrsdata.eng.uci.edu/

Untuk panduan kuliah ini, silahkan download data hujan pada link berikut (gunakan EMAIL Google UGM):
https://drive.google.com/file/d/1tkxLyisrqBiWrey4tFGM4odWTCzdnY-4/view?usp=sharing

Data curah hujan ini telah diolah dan dihimpun dari data beberapa sumber satelit (GSMAP, GPM, PERSIANN, CHIRPS).
Detil metodenya akan disampaikan di panduan yang akan datang.

<h1>&#10003; Read and write data hujan </h1>

---
Contoh mengolah data hujan pos (_raingauge_) menggunakan Python
---

Berikut tutorial contoh sederhana mengolah data hujan dalam bentuk tabel (csv, excel) menggunakan Python.
Jangan lupa untuk download [file data curah hujan harian](https://drive.google.com/file/d/1tkxLyisrqBiWrey4tFGM4odWTCzdnY-4/view?usp=sharing) diatas, yang didalam penulisan coding di bawah ini adalah "Data_hujan_multi_harian.csv".

![image](https://github.com/vempi/course-python-programming/assets/34568583/0da47cd9-a2c0-4a00-a8ef-e1ab089b3afc)

Link Video: (https://www.youtube.com/watch?v=CPTw-HKk5Ss)

Berikut teks coding yang digunaan pada tutorial diatas.

```{python}
import pandas as pd
import matplotlib.pyplot as plt
import calendar
import os,glob

# Set directory
os.chdir("C:/Users/lenovo/OneDrive - UGM 365/R-python/Dosen_miscelenaeous/")
f = "Data_hujan_multi_harian.csv"

# =========================== 1. Hujan Harian Maks =========================== #
# Read data
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

# ================================ 2. Bulanan ================================ #

# Grouping menjadi data bulanan
df['year_month'] = df['Date'].dt.to_period('M')

# Penjumlahan seluruh hujan harian tiap bulan
m = df.groupby('year_month').sum()

# save and plot
m.to_csv('monthly-sum_'+f)
m.plot()


```
---
<h1>&#10003; Data cleaning </h1>
Dataset sumber daya air memiliki beberapa masalah umum yang ditemukan, seperti nilai yang hilang, format tanggal yang tidak konsisten, dan nilai yang ekstrem (outlier). 
Pertama, mari buat contoh dataset yang "kotor" tsb.:

```{python}
import pandas as pd
import numpy as np

# Generate an hypotetical dataset
np.random.seed(0)
dates = pd.date_range('2022-01-01', periods=100)
rainfall = np.random.randint(0, 20, size=100)
discharge = np.random.randint(50, 100, size=100)
# Introduce missing values
rainfall[10:20] = np.nan
discharge[30:40] = np.nan
# Introduce inconsistent date format
dates = dates.strftime('%d/%m/%Y')

# Create DataFrame
dirty_df = pd.DataFrame({'Date': dates, 'Rainfall': rainfall, 'Discharge': discharge})

# Display first few rows
print(dirty_df.head())
```

Kita telah memiliki dataset dengan nilai yang hilang, format tanggal yang tidak konsisten, dan potensi nilai yang ekstrem.
Contoh item pembersihan:
- Memperbaiki Format Tanggal: Mengonversi tanggal ke format yang konsisten (misalnya, 'YYYY-MM-DD').
- Menangani Nilai yang Hilang: Mengisi nilai yang hilang menggunakan metode yang sesuai.
- Menangani Nilai Ekstrem: menghapus nilai ekstrem dalam data.

```{python}
# Clean the "dirty" dataset
clean_df = dirty_df.copy()

# Fix date format
clean_df['Date'] = pd.to_datetime(clean_df['Date'], format='%d/%m/%Y')

# Handle missing values
clean_df['Rainfall'] = clean_df['Rainfall'].fillna(method='ffill')
clean_df['Discharge'] = clean_df['Discharge'].fillna(method='bfill')

# Handle outliers (for demonstration, we'll replace any discharge values above 200 with the median)
discharge_median = clean_df['Discharge'].median()
clean_df.loc[clean_df['Discharge'] > 200, 'Discharge'] = discharge_median

# Display cleaned DataFrame
print(clean_df.head())

```

---
# Check Pembelajaran Pertemuan-8 (Kuis singkat)
  1. Ditahun berapa hujan harian maksimum (HMT) tertinggi tercatat (berdasarkan 4 sumber data hujan tersebut). Apakah 4 summber data tersebut menunjukkan hasil yang identik?
  2. Berapa rerata HMT sepanjang tahun 2001-2022 untuk masing-masing sumber data hujan?
  3. Sumber data apa yang menunjukkan tendensi nilai HMT yang lebih rendah dan tinggi dibandingkan dengan data lain?
---
