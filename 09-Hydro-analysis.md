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

<h1>&#x2713; Filtering and grouping seri waktu </h1>


<h1>&#10003; Analisis historis curah hujan/debit dan visualisasi </h1>

<h1>&#10003; Analisis hubungan debit-hujan  </h1>

<h1>&#10003; Perhitungan dasar metriks/indikator curah hujan rerata dan ekstrem  </h1>

