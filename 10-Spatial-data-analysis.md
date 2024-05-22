---
# Capaian pembelajaran Pertemuan-10
  1. Memahami struktur data spatial
  2. Membaca data spasial hujan
  3. Ekstraksi data Spatial (data vektor)
  4. Visualization
---

# 1. Memahami struktur data spatial 
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

Berikut hasil plot dari code diatas:
![image](https://github.com/vempi/course-python-programming/assets/34568583/ee142615-1fcf-4064-9a05-7c735d15b2b4)

2. Membaca data spasial hujan

<h2> a. Dari file XYZ format tabel (csv) </h2>

Siapkan masing-masing file berikut ini yang dapat diunduh pada:
https://vempi.staff.ugm.ac.id/dataset/ -> 9. Python-GIS: Titik stasiun dan hujan

1. "Spatial_Rain-Sta.csv"
2. "Spatial_Rain-grid.csv"

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

<h2> b. Dari file GIS </h2>
Untuk ini kita perlu menginstall terlebih dahulu library `Geopandas`.

```{python}
conda install geopandas
```

Setelah sukses terinstall lakukan langkah berikut. 
Namun pertama-tama sediakan terlebih dahulu file GIS (Shapefile).

```{python}
import geopandas as gpd

# Read Data stasiun penakar hujan
f1 = 'C:/Users/lenovo/OneDrive - UGM 365/Bahan Kuliah/15.Pemrograman-komputer/Data-demo/pch_bbws.shp'
d = gpd.read_file(f1)

# Read data boundary DAS
f2 = 'C:/Users/lenovo/OneDrive - UGM 365/Bahan Kuliah/15.Pemrograman-komputer/Data-demo/das_citarum.shp'
das = gpd.read_file(f2)
```


# 3. Ekstraksi data Spatial (data vektor)
Data `Geopandas` bersifat seperti Dataframe Pandas. Operasi perintah sebagian besar mirip dengan Pandas.

```{python}
# Menampilkan nama column isi data Vektor stasiun hujan
d.columns

# Mengubah salah satu value kolom menjadi numeric
d['Categories'] = pd.to_numeric(d['Categories'], errors='coerce')

# Dapat dilakukan operasi hitungan seperti pada Pandas
m = d['Categories'].mean()

#plotkan data
d.plot(column='Categories', legend=True, cmap='OrRd', edgecolor='black')

```

Data dari Shapefile dapat dibaca sebagai Array.
Berikut contoh mengambil data dari Shapefile dan dikonversi menjadi data tabel (CSV)

```{python}
# Extract coordinates
coord = np.array([(geom.x, geom.y) for geom in d.geometry])

# Extract values
val = d['Categories'].values 
name = d['Name'].values 

data = {'Name':name,'x': coord[:, 0],'y': coord[:, 1],'Value': val}
df = pd.DataFrame(data)
```
Anda dapat mengulangi metode interpolasi dengan menggunakan data diatas.


# 4. Visualization (prinsip GIS)
Python dapat melakukan tugas layaknya software GIS (misal: QGIS).
Code dibawah ini mendemonstrasikan plotting dengan sumbu X dan Y berbasis spasial (koordinat).

```{python}
fig, ax = plt.subplots(1, 1, figsize=(10, 10))

# Plot one of the data (kolom "Categories")
d.plot(column='Categories', ax=ax, legend=True, cmap='OrRd', edgecolor='black')

# Overlay the additional shapefile
das.boundary.plot(ax=ax, edgecolor='blue')

# Customize the plot
plt.title('Lokasi Pos Penakar Hujan WS Citarum')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Show the plot
plt.show()

```


---
# Check Pembelajaran Pertemuan-10 (Kuis singkat)
  1. Lakukan interpolasi menggunakan Langkah 1 namun menggunakan data Pos Curah Hujan (PCH citarum) dengan kolom data "Categories". Lalu plotkan!
Lampirkan plot gambar pada attachment jawaban.
  2. Download file "Station-coordinate_Solo.csv" pada [website] (https://vempi.staff.ugm.ac.id/dataset/) untuk file nomor 8 "GIS: Titik Stasiun Hujan Bengawan Solo". Disitu terdapat tiga kolo (nama, kordinat x dan y). Tambahkan satu kolom lagi dengan nama "Rainfall" dan isi kolom tersebut dengan bilangan random dengan besaran hujan pada umumnya (misal: hujan harian 300 mm per hari tidak akan lazim). 
Lalu screenshot 10 baris awal di attachment jawaban.
  3. Interpolasikan hasil nomor 2 sebagaimana langkah interpolasi pada soal nomor 1. Lalu plotkan peta interpolasi dan overlay dengan peta DAS Bengawan Solo. 

Hint Nomor 3:
```{python}
f = 'E:/Downloads/Station-coordinate_Solo.csv'
df = pd.read_csv(f)

#[Anda lengkapi sendiri bagian ini]

# open a catchment basemap
f = 'C:/Users/lenovo/OneDrive - UGM 365/Projects-riset/Data/0.Demo-kuliah/Demo kuliah/DAS-Indonesia-4326.shp'
das = gpd.read_file(f)
das.nama_das # print nama-nama das didalam file SHP ini

# mencari nomor index yang "nama_das" nya ada kata "BENGAWAN" 
sel= das[das['nama_das'].str.contains('BENGAWAN', na=False)].index[0]
# Pilih hanya DAS Bengawan Solo saja
bs = das.iloc[[sel]]

# Create a simple map using Matplotlib
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ax.contourf(X, Y, grid_rain)
ax.scatter(x, y, s=30, c='r')  # Plot the scatter points on top
bs.geometry.plot(ax=ax, facecolor='none', edgecolor='black')
plt.show()






#df['Rainfall'] = np.random.gamma(2, 5, len(df))
#x = df['x'].values; y = df['y'].values
#rain = df['Rainfall'].values
#X, Y = np.meshgrid(np.linspace(min(x), max(x), 1000), np.linspace(min(y), max(y), 1000))
#grid_rain = griddata((x, y), rain, (X, Y), method='cubic')

```
---

