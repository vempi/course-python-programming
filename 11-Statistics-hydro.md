---
# Capaian pembelajaran Pertemuan-11
  1. [Data cleaning (review)](#1-Data-cleaning-review)
  2. [Distribusi statistik](#2-Distribusi-statistik)
  3. [Kala ulang (analisis frekuensi)](#3-Kala-ulang-analisis-frekuensi)
  4. [Stationarity](#4-Stationarity-advance)
  5. [Analisis korelasi dan regresi](#5-Analisis-korelasi-dan-regresi)
  6. [Ketidakpastian (uncertainty)](#6-Ketidakpastian-uncertainty-advance)
---

# 1. Data cleaning (review)
Materi dapat dilihat [disini](https://github.com/vempi/course-python-programming/blob/main/08-Hydrological-data.md#4-Data-cleaning).

# 2. Descriptive Statistics
Dalam mendeskripsikan suatu data secara statistik. Langkah dasar yang yang bisa dilakukan adalah dengan memvisuaisasikan distribusi data menggunakan Histogram.
Histogram adalah grafik batang yang terdiri dari batang-batang sejajar yang tingginya mewakili suatu kuantitas yang diminati. Histogram memberikan deskripsi kualitatif dari distribusi sampel univariate (data dengan hanya satu variabel). 

Sumbu vertikal dari diagram histogram dapat mewakili frekuensi kelas, frekuensi kelas relatif, atau kepadatan probabilitas (probability density). Sedangkan sumbu horisontal biasanya menggunakan angka Interval (misalnya, bin) yang sering kali memiliki ukuran yang sama. 

Inspeksi visual dari diagram histogram memberikan informasi penting, termasuk:
(1) tingkat simetri distribusi; 
(2) penyebarannya; 
(3) adanya satu atau lebih kelas dengan frekuensi tinggi; 
(4) keberadaan celah; dan 
(5) adanya _outlier_ atau data yang terpencil.

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ── Generate data sintetik harian hujan & debit (langsung bisa dijalankan!) ───
np.random.seed(0)
dates    = pd.date_range('2012-01-01', '2021-12-31', freq='D')
doy      = dates.dayofyear
seasonal = np.maximum(0.3, 8 + 7 * np.cos(2 * np.pi * (doy - 15) / 365))

rainfall  = np.maximum(0, np.random.exponential(scale=seasonal))
discharge = np.maximum(0, rainfall * 12 + np.random.normal(0, 15, len(dates)))

df = pd.DataFrame({'Date': dates, 'Rainfall': rainfall, 'Discharge': discharge})
df.set_index('Date', inplace=True)
# ── Untuk data CSV asli: ──────────────────────────────────────────────────────
# df = pd.read_csv('Pamarayan-debit-hujan.csv', index_col=0)
# ─────────────────────────────────────────────────────────────────────────────

# 1. Distribution plot untuk data hujan
fig, ax = plt.subplots()
ax.hist(df.Rainfall, bins='auto', edgecolor='black', color='tab:blue', alpha=0.8)
ax.set_xlabel('Rainfall [mm/hari]')
ax.set_ylabel('Frekuensi')
ax.set_title('Distribusi Curah Hujan Harian')
plt.tight_layout()
plt.show()
```
![image](https://github.com/vempi/course-python-programming/assets/34568583/5d761152-6d10-4373-8581-e1d540ab060b)

```python
# 2. Untuk data debit dengan histogram + garis density (KDE)
fig, ax = plt.subplots()
sns.histplot(df['Discharge'], bins=30, kde=True, color='darkblue',
             edgecolor='black', ax=ax)
ax.set_xlabel('Debit [m³/s]')
ax.set_ylabel('Probability Density')
ax.set_title('Distribusi Debit Harian')
plt.tight_layout()
plt.show()
```
![image](https://github.com/vempi/course-python-programming/assets/34568583/c406ecb1-c48a-4333-858c-32fc5ea61146)

Statistik deskriptif digunakan untuk meringkas suatu kumpulan data. Statistik deskriptif setidaknya meliputi:
(1) lokasi suatu kumpulan data (central tendency)
(2) jumlah variasi data (yaitu, penyebaran), dan 
(3) tingkat simetri (yaitu, kecondongan). 

Metrik lokasi suatu kumpulan data meliputi rata-rata aritmetika, geometrik, dan harmonik. Median dan modus dari distribusi mono-modal juga mengukur lokasi data. Penyebaran total data adalah perkiraan variasi, sedangkan varians, simpangan baku, dan rentang inter-kuartil memberikan perkiraan penyebaran data yang lebih akurat. 

```python
# Distribution plot untuk data hujan Tahunan
# ── Data tahunan: agregasi dari df sintetik di atas ───────────────────────────
df_ann = df['Rainfall'].resample('YE').sum().to_frame(name='Rainfall')
# ── Untuk data CSV asli: ──────────────────────────────────────────────────────
# df_ann = pd.read_csv('Ciujung_rainfall-annual_demo.csv', index_col=0)
# ─────────────────────────────────────────────────────────────────────────────

# Menghitung variance dan standard deviation
variance = df_ann['Rainfall'].var()
stddev   = df_ann['Rainfall'].std()
average  = df_ann['Rainfall'].mean()
```

### Visualisasi data
```python
# Yuk plot!
fig, ax = plt.subplots()
ax.hist(df['Rainfall'], bins= 20, density = True, edgecolor='k', label='Measurements Hist') 
ax.axvline(df['Rainfall'].mean(), color='red', label=r'mean', linewidth=2)
ax.axvline(df['Rainfall'].mean()-stddev, color='purple', label=r'mean - 1$\sigma$', linewidth=2)
ax.axvline(df['Rainfall'].mean()+stddev, color='green', label=r'mean + 1$\sigma$', linewidth=2)
ax.axvspan(df['Rainfall'].mean()-stddev, df['Rainfall'].mean()+stddev, alpha=0.1, color='orange', 
           label=r'mean $\pm$ 1$\sigma$')
ax.set_xlabel('Hujan [mm/hari]')
ax.set_ylabel('Probability density')
ax.legend()
```
![image](https://github.com/vempi/course-python-programming/assets/34568583/ccc2394c-7093-4f05-a454-c2d86f476a4e)

Secara singkat parameter statistik dasar suatu data dalam bentuk dataframe dapat didapat dengan code sederhana berikut.

```python
df.set_index('Date',inplace=True)
df.describe()
```
Output:
| Statistic | Discharge    | Rainfall     |
|-----------|--------------|--------------|
| count     | 3652.000000  | 3653.000000  |
| mean      | 89.976906    | 8.460661     |
| std       | 123.994980   | 11.097191    |
| min       | 0.000000     | 0.000000     |
| 25%       | 14.030000    | 0.840337     |
| 50%       | 70.640000    | 4.760397     |
| 75%       | 127.130000   | 11.477631    |
| max       | 2600.000000  | 105.012581   |

# 3. Kala ulang (analisis frekuensi) [ADVANCE]
Materi ini akan diberikan terpisah pada materi pengayaan yang akan datang.

# 4. Stationarity [ADVANCE]
Stasioneritas (stationarity), tren, musiman (seasonality), dan periodisitas adalah konsep dasar dalam analisis data dengan deret waktu (timeseries). Stasioneritas merujuk pada sifat deret waktu di mana fitur statistiknya seperti rata-rata, varians, dan autokorelasi tetap konstan dari waktu ke waktu. Hal ini penting karena banyak teknik pemodelan statistik mengasumsikan atau memerlukan deret waktu yang stasioner, termasuk untuk data hidrologi seperti hujan dan debit.

![image](https://github.com/vempi/course-python-programming/assets/34568583/93ba4baa-b958-4f5a-badc-c65ecbcd99f9)

Sumber: [wellntel.com](https://wellntel.com/nonstationarity-the-importance-of-hydrologic-observations-and-data-to-water-management/)

i. Tren mengacu pada pergerakan jangka panjang dalam deret waktu. Tren dapat berupa tren naik, turun, atau mendatar, yang menunjukkan peningkatan, penurunan, atau tidak ada perubahan pada variabel yang dianalisis seiring waktu.

ii. Musiman adalah karakteristik deret waktu di mana data menunjukkan perubahan yang teratur dan dapat diprediksi yang berulang setiap musim kalender (contoh: pola hujan yang berbeda di musim penghujan dan kemarau). Sedangkan, periodisitas, mirip dengan musiman, merujuk pada pola yang berulang dalam periode waktu yang dapat diprediksi dan tetap. Perbedaannya adalah pola periodik tidak terikat pada kalender. Misalnya, pola tertentu dalam deret waktu yang berulang setiap 10 titik data menunjukkan periodisitas.

Sebelum memulai, silahkan install package `statsmodels`
`
conda install statsmodels
`

Lalu kita gunakan data `Pamarayan-debit-hujan.csv` untuk mendemonstrasikan topik ini.

```python
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller as ADF
from statsmodels.tsa.seasonal import seasonal_decompose

# ── Gunakan df sintetik dari blok sebelumnya ──────────────────────────────────
# Downsample ke 2-bulanan
resampled = df[['Rainfall']].resample('2ME').sum()
# ── Untuk data CSV asli: ──────────────────────────────────────────────────────
# data = pd.read_csv("Pamarayan-debit-hujan.csv", index_col=0)
# data["Date"] = pd.to_datetime(data['Date'])
# resampled = data[["Date","Rainfall"]].resample('2ME', on="Date").sum()
# ─────────────────────────────────────────────────────────────────────────────

# coba plot data
resampled.plot(figsize=(10, 4))
plt.xlabel('Waktu')
plt.ylabel('Hujan dua bulanan (mm)')
plt.title('Curah Hujan 2-Bulanan')
plt.tight_layout()
plt.show()
```
![image](https://github.com/vempi/course-python-programming/assets/34568583/c300baf5-4e1f-49e6-bf53-2aed1272a912)

Lalu gunakan `seasonal_decompose` untuk mengetahui apakah data stasioner atau tidak.

```python
# Geser data agar semua nilai positif (syarat multiplicative decomposition)
minx      = resampled['Rainfall'].min()
resampled = resampled.copy()
resampled['Rainfall'] = resampled['Rainfall'] - minx + 10.0

# Decompose a signal (multiplicative/additive)
decom = seasonal_decompose(resampled['Rainfall'], model="multiplicative", period=6)
```

Setelah kita dapatkan variabel hasil `decom` mari kita plot data tersebut:

```python
fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, figsize=(10, 7))
axes[0].plot(decom.observed, color='steelblue',  label='Data Asli')
axes[1].plot(decom.seasonal, color='seagreen',   label='Musiman')
axes[2].plot(decom.trend,    color='tomato',     label='Tren')
for ax, lbl in zip(axes, ['Data Asli (mm)', 'Komponen Musiman', 'Tren']):
    ax.set_ylabel(lbl, fontsize=9)
    ax.grid(ls='--', alpha=0.5)
    ax.legend(loc='upper right', fontsize=9)
axes[2].set_xlabel('Tahun')
plt.suptitle('Dekomposisi Musiman Curah Hujan 2-Bulanan', fontsize=12)
plt.tight_layout()
plt.show()
```
![image](https://github.com/vempi/course-python-programming/assets/34568583/1cdac1cd-1222-45b0-b43d-ff3fb90d07b1)

### Cek stationarity
Code di bawah ini akan mendeskripsikan apakah data memiliki trend beserta informasi lainnya yang terkait. Topik ini akan dieksplor lebih lanjut pada materi pengayaan selanjutnya (hasil dari coding di bawah ini sementara hanya digunakan sebagai referensi). 

```python
# Stationarity check
def stationarity_adf_test(x, alpha=0.05):
    adftest_res = ADF(x.dropna(), autolag="AIC")
    dfout = pd.Series(adftest_res[0:4],
                      index=["ADF statistic", "ADF p-value",
                             "ADF lags used", "ADF number of obs used"])
    for key, value in adftest_res[4].items():
        dfout["Critical Value (%s)" % key] = value

    print(dfout.round(4).to_string())
    if dfout["ADF p-value"] > alpha:
        print(f"\n Hasil: TIDAK stasioner (p = {dfout['ADF p-value']:.4f} > α = {alpha})")
    else:
        print(f"\n Hasil: STASIONER (p = {dfout['ADF p-value']:.4f} ≤ α = {alpha})")

stationarity_adf_test(resampled['Rainfall'])
```


# 5. Analisis korelasi dan regresi
Materi dapat dilihat di materi sebelum UTS.

# 6. Ketidakpastian (uncertainty) [ADVANCE]
Mengestimasi ketidakpastian adalah bagian penting dari analisis sumber daya air, karena memberikan ukuran kepercayaan terhadap prediksi model dan membantu dalam pengambilan keputusan di bawah risiko. Ketidakpastian dapat datang dari data input pemodelan hidrologi seperti curah hujan, suhu, karakteristik tanah, dsb. dapat memiliki ketidakpastian akibat kesalahan pengukuran, kekosongan data, atau variabilitas spasial dan temporal. 

Dalam tutorial ini, ketidakpastian diartikan pada konteks data input (misal: hujan). Bagian ini tidak akan mendemonstrasikan bagaimana kita menguantifikasi ketidakpastian dari seluruh tahapan mulai dari input data, representasi model fisik, hingga ketidakpastian keluaran dari model tersebut. Secara sederhana kita akan diskusikan bagaimana data hujan dari berbagai data satelit menunjukkan hasil yang berbeda dan memuat ketidakpastian akan akurasi pengamatan.

```python
# ── Generate data tahunan sintetik 4 sumber satelit (langsung bisa dijalankan!) ─
np.random.seed(7)
years = pd.date_range('2001', '2022', freq='YE')

df_unc = pd.DataFrame({
    'GSMAP'   : np.random.normal(80,  15, len(years)),
    'GPM'     : np.random.normal(75,  12, len(years)),
    'PERSIANN': np.random.normal(90,  20, len(years)),
    'CHIRPS'  : np.random.normal(70,  10, len(years)),
}, index=years.year)
df_unc.index.name = 'Tahun'
# ── Untuk data CSV asli (hasil Modul-8): ─────────────────────────────────────
# df_unc = pd.read_csv('ann-max_hujan_multi_harian.csv').set_index('Date')
# ─────────────────────────────────────────────────────────────────────────────
df = df_unc   # alias agar kode di bawah tetap berjalan

# make date as x axis index of the plot
df = df.set_index(df.index)

src_cols = ['GSMAP', 'GPM', 'PERSIANN', 'CHIRPS']

# Menghitung rata-rata dan standar deviasi (sebagai ketidakpastian) untuk setiap baris
df['Mean']   = df[src_cols].mean(axis=1)
df['StdDev'] = df[src_cols].std(axis=1)

# Visualisasi dengan error bar
plt.figure(figsize=(11, 6))
for col in src_cols:
    plt.plot(df.index, df[col], alpha=0.5, linewidth=1.2, label=col)

plt.errorbar(df.index, df['Mean'], yerr=df['StdDev'],
             fmt='ko-', ecolor='blue', capsize=5, linewidth=2,
             label='Mean ± StdDev')
plt.fill_between(df.index,
                 df['Mean'] - df['StdDev'],
                 df['Mean'] + df['StdDev'],
                 alpha=0.15, color='blue')
plt.title('Data Hujan Satelit dengan Uncertainty Bar')
plt.xlabel('Tahun')
plt.ylabel('Hujan Harian Maksimum Tahunan (mm)')
plt.legend(fontsize=9)
plt.tight_layout()
plt.show()
```
![image](https://github.com/vempi/course-python-programming/assets/34568583/c1532ae0-e4a1-4b61-a1a6-b875a32196c0)

---
# Check Pembelajaran Pertemuan-11 (Kuis singkat)
  1. Menggunakan data sintetik `df_ann` dari contoh di atas, visualisasikan **mean** dan **standar deviasi** curah hujan tahunan sebagaimana pada [Langkah visualisasi](#visualisasi-data). Di tahun mana curah hujan paling jauh dari rata-rata?
  2. Menggunakan metode `stationarity_adf_test()` pada [Langkah di atas](#cek-stationarity), apakah data hujan 2-bulanan (`resampled`) bersifat stasioner? Coba bandingkan hasilnya sebelum dan sesudah dilakukan `diff()` (differencing).
  3. Buat DataFrame multi-sumber hujan **bulanan** dari data sintetik `df` dengan cara `resample('ME').sum()`. Lalu plot data tersebut beserta uncertainty bar (mean ± std) sebagaimana pada [Langkah ke-6](#6-Ketidakpastian-uncertainty-advance). Bulan apa yang menunjukkan ketidakpastian antar-sumber terbesar?

```python
# Starter kode untuk soal no. 3
df_monthly = df[['GSMAP','GPM','PERSIANN','CHIRPS']].resample('ME').sum()
# Lanjutkan sendiri: hitung mean & std, lalu plot!
```

---

