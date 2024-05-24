---
# Capaian pembelajaran Pertemuan-12
  1. [Data cleaning (review)](#1-Data-cleaning-review)
  2. [Distribusi statistik](#2-Distribusi-statistik)
  3. [Kala ulang (analisis frekuensi)](#3-Kala-ulang-analisis-frekuensi)
  4. [Stationarity](#4-Stationarity)
  5. [Analisis korelasi dan regresi](#5-Analisis-korelasi-dan-regresi)
  6. [Ketidakpastian (uncertainty)](#6-Ketidakpastian-uncertainty)
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

# 4. Stationarity

# 5. Analisis korelasi dan regresi

# 6. Ketidakpastian (uncertainty)
