---
# Capaian pembelajaran Pertemuan-9
  1. Dapat memodifikasi dataframe
  2. Filtering and grouping seri waktu
  3. Analisis historis curah hujan/debit dan visualisasi
  4. Analisis hubungan debit-hujan 
  6. Perhitungan dasar metriks/indikator curah hujan rerata dan ekstrem
---

<h1>&#x2713; Modifikasi dataframe </h1>

Indonesian Rivers

| Name           | Length (km) | Drainage Area (km2) |
|----------------|-------------|---------------------|
| Sungai Musi    | 750         | 26,810              |
| Sungai Kapuas  | 1,143       | 98,000              |
| Sungai Barito  | 880         | 100,000             |
| Sungai Rajang  | 563         | 50,702              |
| Sungai Mahakam | 980         | 77,400              |

Pertama kita buat dataframe seperti tabel di bawah. File dibuat dari Dictionary.

```{python}
import pandas as pd

# Define a dictionary containing river details
river_details = {
    'Name': ['Sungai Musi', 'Sungai Kapuas', 'Sungai Barito', 'Sungai Rajang', 'Sungai Mahakam'],
    'Length (km)': [750, 1143, 880, 563, 980],
    'Drainage Area (km2)': [26810, 98000, 100000, 50702, 77400]
}

# Convert the dictionary into DataFrame
river_df = pd.DataFrame(river_details)

# Print the data frame
print(river_df)
```

Anda bisa memodifikasi dataframe diantaranya adalah menambahkan column baru dan mengganti nama column.

```(python)
# Modify the DataFrame by adding a new column
river_df['Countries'] = ['Indonesia', 'Indonesia', 'Indonesia', 'Indonesia', 'Indonesia']

# Modify the DataFrame by changing the column name
river_df = river_df.rename(columns={'Length (km)': 'Length_km'})

# Print the modified data frame
print("Modified DataFrame:")
print(river_df)
```
Anda juga bisa melakukan langkah-langkah modifikasi antara lain sebagai berikut:

```(python)
# Menambah baris baru
new_row = {'Name': 'Sungai Baliem', 'Length (km)': 373, 'Drainage Area (km2)': 14850, 'Countries': 'Indonesia'}
river_df = river_df.append(new_row, ignore_index=True)

# Menghapus kolom 'Countries'
river_df = river_df.drop('Countries', axis=1)

# Mengganti nilai dalam kolom 'Length_km'
river_df['Length_km'] = river_df['Length_km'].replace(880, 900)

# Menambah kolom baru 'Length_miles' yang menghitung panjang sungai dalam mil
river_df['Length_miles'] = river_df['Length_km'] * 0.621371

# Menyortir DataFrame berdasarkan panjang sungai
river_df = river_df.sort_values('Length_km', ascending=False)

# Mengganti indeks menjadi 'Name'
river_df = river_df.set_index('Name')

print(river_df)
```

<h1>&#x2713; Filtering and grouping seri waktu </h1>

Kita pertama-tama bisa membuat data hipotetikal, lalu melakukan beberapa langkah filtering dan grouping seri waktu sbb. 

```{python}
import pandas as pd
import numpy as np

# Membuat DataFrame dengan index datetime
date_rng = pd.date_range(start='2022-01-01', end='2022-01-10', freq='D')
df = pd.DataFrame(date_rng, columns=['date'])
df['data'] = np.random.randint(0, 100, size=(len(date_rng)))

# Menjadikan kolom 'date' sebagai indeks
df.set_index('date', inplace=True)

# Filtering data berdasarkan tanggal
filtered_df = df.loc['2022-01-03':'2022-01-07']

# Grouping data berdasarkan minggu
weekly_df = df.resample('W').sum()
```

<h1>&#10003; Analisis historis curah hujan/debit dan visualisasi </h1>

```{python}

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data curah hujan/debit dari file CSV
df = pd.read_csv("Data_hujan_multi_harian.csv")

# Mengubah kolom tanggal menjadi tipe datetime
df['Date'] = pd.to_datetime(df['Date'])

df = df.dropna()

# Mengatur kolom tanggal sebagai indeks
df.set_index('Date', inplace=True)

# Analisis statistik sederhana
print("Statistik Curah Hujan/Debit:")
print(df.describe())

# Visualisasi time series plot
plt.figure(figsize=(12, 6))
df.plot()
plt.xlabel('Tanggal')
plt.ylabel('Curah Hujan (mm)')
plt.title('Time Series Curah Hujan')
plt.legend()
plt.show()


# Visualisasi histogram
plt.figure(figsize=(10, 6))
# Kita pilih data CHIRPS untuk diplot
sns.histplot(df['CHIRPS'], bins=30, kde=True, color='skyblue')
plt.xlabel('Curah Hujan (mm)')
plt.ylabel('Frekuensi')
plt.title('Distribusi Curah Hujan')
plt.show()

# Visualisasi box plot per bulan
df['Month'] = df.index.month
plt.figure(figsize=(10, 6))
# Kita pilih data CHIRPS untuk diplot
sns.boxplot(x='Month', y='CHIRPS', data=df, palette='viridis')
plt.xlabel('Bulan')
plt.ylabel('Curah Hujan (mm)')
plt.title('Box Plot Curah Hujan per Bulan')
plt.show()
``

<h1>&#10003; Analisis hubungan debit-hujan  </h1>
Berikut ini tetap menggunakan data diatas, namun ditambahkan satu kolom tambahan yaitu data debit hipotetikal.

```(python)
import matplotlib.pyplot as plt

start_date = '2022-01-03'
end_date = '2022-01-17'
seldf = df.loc[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

# Mendefinisikan parameter untuk menghitung debit hipotetikal
debit_per_mm = 50  # Anggap setiap mm (data GPM) curah hujan menghasilkan 100 m^3/s debit

# Menghitung debit hipotetikal berdasarkan curah hujan
seldf['Discharge'] = seldf['GPM'] * debit_per_mm

# keluarkan index Date menjadi kolom Date biasa
seldf = seldf.reset_index()

# Menampilkan plot curah hujan dan debit hipotetikal dengan double axis
fig, ax1 = plt.subplots(figsize=(12, 6))

# Line plot untuk curah hujan
color = 'tab:blue'
ax1.set_xlabel('Tanggal')
ax1.set_ylabel('Curah Hujan (mm)', color=color)
ax1.bar(seldf['Date'], seldf['GSMAP'], color=color, alpha=0.5, width=0.5)
ax1.tick_params(axis='y', labelcolor=color)

# Membalik sumbu y
ax1.invert_yaxis()

# Axis kedua untuk bar plot debit (dibalik secara vertikal)
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Debit (m³/s)', color=color)
ax2.plot(seldf['Date'], seldf['Discharge'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Hubungan Debit-Hujan Hipotetikal')
plt.show()
```

<h1>&#10003; Perhitungan dasar metriks/indikator curah hujan rerata dan ekstrem  </h1>

