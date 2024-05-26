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

Download terlebih dahulu data `Pamarayan-debit-hujan.csv` di [https://vempi.staff.ugm.ac.id/dataset/](https://vempi.staff.ugm.ac.id/dataset/)

```{python}
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('E:/Downloads/Pamarayan-debit-hujan.csv', index_col=0)

# 1. Distribution plot untuk data hujan
fig, ax = plt.subplots()
ax.hist(df.Rainfall, bins='auto', edgecolor='black', color='tab:blue', alpha=0.8)
ax.set_xlabel('Rainfall [mm/hari]')
ax.set_ylabel('Frekuensi')
```
![image](https://github.com/vempi/course-python-programming/assets/34568583/5d761152-6d10-4373-8581-e1d540ab060b)

```{python}
# 2. Untuk data hujan tapi dengan garis density
fig, ax = plt.subplots()
sns.distplot(df['Discharge'], hist=True, kde=True,  
             color = 'darkblue',  hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 2})
ax.set_xlabel('Debit [m3/d]')
ax.set_ylabel('Probability Density')
```
![image](https://github.com/vempi/course-python-programming/assets/34568583/c406ecb1-c48a-4333-858c-32fc5ea61146)

Statistik deskriptif digunakan untuk meringkas suatu kumpulan data. Statistik deskriptif setidaknya meliputi:
(1) lokasi suatu kumpulan data (central tendency)
(2) jumlah variasi data (yaitu, penyebaran), dan 
(3) tingkat simetri (yaitu, kecondongan). 

Metrik lokasi suatu kumpulan data meliputi rata-rata aritmetika, geometrik, dan harmonik. Median dan modus dari distribusi mono-modal juga mengukur lokasi data. Penyebaran total data adalah perkiraan variasi, sedangkan varians, simpangan baku, dan rentang inter-kuartil memberikan perkiraan penyebaran data yang lebih akurat. 

```{python}
# Distribution plot untuk data hujan Tahunan
# Read data hujan tahunan
df_ann = pd.read_csv('E:/Downloads/Ciujung_rainfall-annual_demo.csv', index_col=0)

# Menghitung variance dan standard deviation
variance =  df['Rainfall'].var()
stddev =  df['Rainfall'].std()
average =  df['Rainfall'].mean()

# Untuk print hasil di console Spyder
print ('-------')
print ('Varians')
print("{0:.0f} [square mm]".format(variance))
print ('-------')
print ('Deviasi Standar')
print("{0:.0f} [mm]".format(stddev))
print ('-------')
print ('Rata-rata')
print("{0:.0f} [mm]".format(average))
print ('-------')

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

```{python}
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

# 3. Kala ulang (analisis frekuensi)

# 4. Stationarity [ADVANCE]
Stasioneritas (stationarity), tren, musiman (seasonality), dan periodisitas adalah konsep dasar dalam analisis data dengan deret waktu (timeseries). Stasioneritas merujuk pada sifat deret waktu di mana fitur statistiknya seperti rata-rata, varians, dan autokorelasi tetap konstan dari waktu ke waktu. Hal ini penting karena banyak teknik pemodelan statistik mengasumsikan atau memerlukan deret waktu yang stasioner, termasuk untuk data hidrologi seperti hujan dan debit.

i. Tren mengacu pada pergerakan jangka panjang dalam deret waktu. Tren dapat berupa tren naik, turun, atau mendatar, yang menunjukkan peningkatan, penurunan, atau tidak ada perubahan pada variabel yang dianalisis seiring waktu.

ii. Musiman adalah karakteristik deret waktu di mana data menunjukkan perubahan yang teratur dan dapat diprediksi yang berulang setiap musim kalender (contoh: pola hujan yang berbeda di musim penghujan dan kemarau). Sedangkan, periodisitas, mirip dengan musiman, merujuk pada pola yang berulang dalam periode waktu yang dapat diprediksi dan tetap. Perbedaannya adalah pola periodik tidak terikat pada kalender. Misalnya, pola tertentu dalam deret waktu yang berulang setiap 10 titik data menunjukkan periodisitas.

Sebelum memulai, silahkan install package `statsmodels`
`
conda install statsmodels
`

Lalu kita gunakan data `Pamarayan-debit-hujan.csv` untuk mendemonstrasikan topik ini.

```{python}
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller as ADF
from statsmodels.tsa.seasonal import seasonal_decompose

# Read data
data = pd.read_csv("E:/Downloads/Pamarayan-debit-hujan.csv",index_col=0)
data["Date"] = pd.to_datetime(data['Date'])

df = data[["Date", "Rainfall"]]

# Downsample the time series
resampled = df.resample('2M', on="Date").sum()

#Transform the data
def transform(x):
    x = x - minx + 10.0
    return x

def inverse_transform(x):
    x = x - 10.0 + minx
    return x

#Transform data
minx = resampled.min()
resampled = transform(resampled)

#Decompose a signal (multiplicative/additive)
decom = seasonal_decompose(resampled, model="multiplicative")
```

Setelah kita dapatkan variabel hasil `decom` mari kita plot data tersebut:

```{python}
fig, ax = plt.subplots(nrows=3, ncols=1, sharex=True,figsize=(8, 6))
ax[0].plot(decom.observed, label='Time series')
ax[1].plot(decom.seasonal, label='Seasonal')
ax[2].plot(decom.trend, label='Trend')
ax[0].set_ylabel('Series')
ax[1].set_ylabel('Seasonal')
ax[2].set_ylabel('Trend')
ax[2].set_xlabel('Year')
ax[0].grid(ls='--')
ax[1].grid(ls='--')
ax[2].grid(ls='--')
plt.tight_layout()
#plt.savefig('seasonal.pdf', dpi=300)
```
![image](https://github.com/vempi/course-python-programming/assets/34568583/1cdac1cd-1222-45b0-b43d-ff3fb90d07b1)

Code di bawah ini akan mendeskripsikan apakah data memiliki trend beserta informasi lainnya yang terkait. Topik ini akan di eksplor lebih lanjut pada materi pengayaan selanjutnya (hasil dari coding di bawah ini sementara hanya digunakan sebagai referensi). 

```{python}
# Stationarity check
def stationarity_adf_test(x, alpha=0.05):
    adftest_res = ADF(x, autolag="AIC")
    dfout = pd.Series(adftest_res[0:4], index=["ADF statistic", "ADF p-value",
                                               "ADF lags used", "ADF number of obs used"])
    for key, value in adftest_res[4].items():
        dfout[" Critical Value (%s)" % key] = value
        print(dfout)
        if dfout["ADF p-value"] > alpha:
            print(" Result: Non-stationary time series", "\n")
        else:
            print(" Result: Stationary time series", "\n")
        print("\nChecking stationarity:")
        
stationarity_adf_test(resampled)
```


# 5. Analisis korelasi dan regresi
Materi dapat dilihat [disini](https://github.com/vempi/course-python-programming/blob/main/08-Hydrological-data.md#4-Data-cleaning).

# 6. Ketidakpastian (uncertainty) [ADVANCE]
Mengestimasi ketidakpastian adalah bagian penting dari analisis sumber daya air, karena memberikan ukuran kepercayaan terhadap prediksi model dan membantu dalam pengambilan keputusan di bawah risiko. Ketidakpastian dapat datang dari data input pemodelan hidrologi seperti curah hujan, suhu, karakteristik tanah, dsb. dapat memiliki ketidakpastian akibat kesalahan pengukuran, kekosongan data, atau variabilitas spasial dan temporal. 

Dalam tutorial ini, ketidakpastian diartikan pada konteks data input (misal: hujan). Bagian ini tidak akan mendemonstrasikan bagaimana kita menguantifikasi ketidakpastian dari seluruh tahapan mulai dari input data, representasi model fisik, hingga ketidakpastian keluaran dari model tersebut. Secara sederhana kita akan diskusikan bagaimana data hujan dari berbagai data satelit menunjukkan hasil yang berbeda dan memuat ketidakpastian akan akurasi pengamatan.

Gunakan file keluaran "ann-max_Data_hujan_multi_harian.csv" yang didapatkan pada [bab ini](https://github.com/vempi/course-python-programming/blob/main/08-Hydrological-data.md).

```{python}
# Membaca data curah hujan/debit dari file CSV
f = "ann-max_Data_hujan_multi_harian.csv"
df = pd.read_csv(f)

# make date as x axis index of the plot
df = df.set_index('Date')

# Menghitung rata-rata dan standar deviasi (sebagai ketidakpastian) untuk setiap baris
df['Mean'] = df.mean(axis=1)
df['StdDev'] = df.std(axis=1)

# Visualisasi dengan error bar
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, markers=True, palette=['grey'] * df.columns.size)
#df.plot()
plt.errorbar(df.index, df['Mean'], yerr=df['StdDev'], fmt='o', ecolor='blue', capsize=5, 
             label='Data Hujan (Mean ± StdDev)')
plt.title('Data Hujan Satelit dengan Uncertainty Bar')
plt.xlabel('Tahun')
plt.ylabel('Hujan Harian Maksimum Tahunan (mm)')
plt.legend()
plt.show()
```
![image](https://github.com/vempi/course-python-programming/assets/34568583/c1532ae0-e4a1-4b61-a1a6-b875a32196c0)

