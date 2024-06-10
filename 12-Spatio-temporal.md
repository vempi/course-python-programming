---
# Capaian pembelajaran Pertemuan-12
  1. Membaca netCDF data menggunakan xarray library
  2. Filtering and grouping temporal series
  3. Satellite / remote sensing data analysis
  4. Spatiotemporal operation

---

# Membaca netCDF data menggunakan xarray library
NetCDF (Network Common Data Form) adalah format file yang umum digunakan untuk menyimpan data ilmiah multidimensi, seperti variabel yang berubah seiring waktu. `xarray` adalah pustaka Python yang memudahkan manipulasi dan analisis data multidimensi seperti NetCDF.

## Instalasi
Pastikan `xarray` dan pustaka lain yang dibutuhkan sudah terinstal:

`conda install -c conda-forge xarray dask netCDF4 bottleneck`

## Download file contoh netCDF dari PERSIANN website 
Download file [https://chrsdata.eng.uci.edu/](https://chrsdata.eng.uci.edu/).

Download data dengan memilih contoh spesifikasi berikut:
![image](https://github.com/vempi/course-python-programming/assets/34568583/20627b72-eca1-44e1-9a7c-32c4a2bf3116)

Pastikan saat memilih `Domain: Country` click pada salah satu bagian Indonesia (didalam garis kuning) pada peta. 

Silahkan didownload, lalu extract file didalam ZIP tersebut dan temukan file netCDF adalah file yang berekstensi `.nc`

## Baca file netCDF

```{python}
import xarray as xr
import matplotlib.pyplot as plt

# Membaca file NetCDF
f = "E:/Downloads/PERSIANN_Indonesia_2024-06-10102444am/PERSIANN_Indonesia_2024-06-10102444am.nc"
data = xr.open_dataset(f)
print(data)

# Menampilkan semua variabel dalam dataset
print(data.precip)

# Mengakses variabel tertentu
prec = data['precip']
print(prec)

# Membuat plot data hujan
prec.isel(datetime=0).plot()
plt.show()

```

<h1>&#x2713; Filtering and grouping temporal series  </h1>

<h1>&#10003; Satellite / remote sensing data analysis </h1>

<h1>&#10003; Spatiotemporal operation </h1>
