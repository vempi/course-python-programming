---
# Capaian pembelajaran Pertemuan-12
  1. [Data cleaning (review)](#1-Data-cleaning-review)
  2. [Distribusi statistik](#2-Distribusi-statistik)
  3. [Kala ulang (analisis frekuensi)](#3-Kala-ulang-analisis-frekuensi)
  4. [Trend, stationarity, periodicity](#4-Trend-stationarity-periodicity)
  5. [Analisis korelasi dan regresi](#5-Analisis-korelasi-dan-regresi)
  6. [Ketidakpastian (uncertainty)](#6-Ketidakpastian-uncertainty)
---

# 1. Data cleaning (review)
Materi dapat dilihat [disini](https://github.com/vempi/course-python-programming/blob/main/08-Hydrological-data.md#4-Data-cleaning).

# 2. Descriptive Statistics
Dalam mendeskripsikan suatu data secara statistik. Langkap awam yang yang bisa dilakukan adalah dengan memvisuaisasikan distribusi data menggunakan Histogram.
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

# 3. Kala ulang (analisis frekuensi)

# 4. Trend, stationarity, periodicity

# 5. Analisis korelasi dan regresi

# 6. Ketidakpastian (uncertainty)
