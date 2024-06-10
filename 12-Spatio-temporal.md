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
'conda install -c conda-forge xarray dask netCDF4 bottleneck'

## Download file contoh NetCDF dari PERSIANN website 

```{python}
import xarray as xr
import matplotlib.pyplot as plt

# Membaca file NetCDF
data = xr.open_dataset('path/to/your/file.nc')
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
