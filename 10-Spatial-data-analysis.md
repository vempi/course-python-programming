---
# Capaian pembelajaran Pertemuan-10
  1. Memahami struktur data spatial
  2. Membaca data spasial hujan
  3. Spatial analysis and visualization 
  4. Plotting and mapping
---

<h1>&#x2713; Memahami struktur data spatial </h1>
Kita bisa mendapatkan data curah hujan dari beberapa pos ukur hujan. Lalu kita dapat membuat plot isohyet (kontur) dari curah hujan tersebut. 
Untuk demonstrasi, pertama kita akan membuat lokasi (x, y) dan curah hujan untuk sepuluh stasiun menggunakan angka acak.

```{python}
import numpy as np
import matplotlib.pyplot as plt

#generate locations and rainfall
x = np.random.rand(10)
y = np.random.rand(10)
rain = 10*np.random.rand(10)

#plot the locations
plt.scatter(x,y)
plt.xlabel('X')
plt.ylabel('Y')
```
![image](https://github.com/vempi/course-python-programming/assets/34568583/9c15d6be-16bf-4f0b-8baa-a8d4808b76c0)
Sumber: Python in hydrology (Sat Kumar Tomer)

Pertama, kita perlu membuat grid dengan jarak reguler yang memiliki rentang yang sama dengan lokasi alat ukur hujan. 
Kemudian, dari data lokasi dan curah hujan yang diberikan, kita perlu menghitung data pada grid reguler menggunakan skema interpolasi tertentu (misal: cubic). 
Setelah itu, peta kontur dapat diperoleh. Fungsi griddata dari pustaka `scipy.interpolate` berguna untuk mendapatkan data grid. 

Lalu Kita gunakan fungsi meshgrid dari pustaka `numpy` untuk membuat grid dari vektor x dan y yang diberikan.

```{python}
from scipy.interpolate import griddata

# Generate the desired grid, where rainfall is to be interpolated
X, Y = np.meshgrid(np.linspace(min(x), max(x), 1000), np.linspace(min(y), max(y), 1000))
# min() max() digunakan untuk menentukan batasan interpolasinya

# Perform the gridding
grid_rain = griddata((x, y), rain, (X, Y), method='cubic')# Added method parameter for interpolation
#grid_rain = griddata((x, y), rain, (X, Y), method='linear')

```
Sekarang, kita dapat membuat plot kontur dari data bergrid dengan fungsi `plt.contourf()`. 
FYI, fungsi contourf membuat kontur terisi yang angka, sementara contour() menyediakan hanya kontur. 

Kita mulai dengan membersihkan gambar saat ini dengan menggunakan `plt.clf()` (karena mungkin ada beberapa gambar yang sudah ada di memori).
Kita juga dapat menambahkan lokasi pos  hujan menggunakan `plt.scatter()`. `s` dan `c` digunakan untuk menentukan ukuran dan warna penanda. 
`plt.xlim()` dan `plt.ylim()` juga dapat digunakan untuk membatasi rentang sumbu x dan y.

```{python}
# Plot the results
plt.clf()
plt.contourf(X, Y, grid_rain)
plt.scatter(x, y, s=30, c='r')  # Plot the scatter points on top
plt.colorbar()
plt.xlabel('X'); plt.ylabel('Y')
plt.show()
#plt.savefig('E:/Downloads/grid_rain.png')
```

<h1>&#x2713; Membaca data spasial hujan </h1>

<h2>&#x2713; a. Dari file XYZ format tabel (csv) </h2>

Siapkan masing-masing file:
1. ""
2. ""
3. ""

```{python}
# a. Real station data (DAS Bengawan Solo)
f = 'C:/Users/lenovo/OneDrive - UGM 365/Bahan Kuliah/15.Pemrograman-komputer/Data-demo/Spatial_Rain-Sta.csv'
df = pd.read_csv(f)

# b. Real satelite data (gridded) (DAS Ciujung)
f = 'C:/Users/lenovo/OneDrive - UGM 365/Bahan Kuliah/15.Pemrograman-komputer/Data-demo/Spatial_Rain-grid.csv'
df = pd.read_csv(f)

# membaca kolom sebagai sumbu x, y, dan nilai hujan itu sendiri
x = df['X'].values
y = df['Y'].values
rain = df['Rain'].values

```

Lakukan langkah pada poin pertama diatas.

<h2>&#x2713; b. Dari file GIS </h2>

```{python}
import geopandas as gpd

# Ubah path sesuai dengan lokasi file shapefile Anda
path_to_shapefile = 'path_to_your_shapefile.shp'
data = gpd.read_file(path_to_shapefile)

# Menampilkan data spasial hujan
data.plot()

# Analisis data: menghitung rata-rata curah hujan
mean_rainfall = data['rainfall'].mean()

print("Rata-rata curah hujan:", mean_rainfall)

```

<h1>&#x2713; Spatial analysis and visualization  </h1>

```{python}
import geopandas as gpd

# Analisis data: menghitung rata-rata curah hujan
mean_rainfall = data['rainfall'].mean()

print("Rata-rata curah hujan:", mean_rainfall)

# Menampilkan data spasial hujan
mean_rainfall.plot()

```

<h1>&#10003; Plotting and mapping </h1>

```{python}


```

---
# Check Pembelajaran Pertemuan-10 (Kuis singkat)
  1. Lakukan Filtering data hujan CHIRPS dari file "Data_hujan_multi_harian.csv" hanya pada tahun kelahiran anda. Lalu resample berdasarkan minggu. Di bulan dan minggu ke berapa hujan akumulasi paling besar terjadi?
  2. Visualisasi box plot per bulan berdasarkan data PERSIANN. Bulan apa yang memiliki nilai hujan bulanan tertinggi dan terendah?
  3. Plotkan grafik contoh hubungan hujan debit pada _range_ tanggal kelahiran anda (seminggu sebelum hingga seminggu setelah) berdasarkan data GPM!  
---

