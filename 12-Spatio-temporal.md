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
![image](https://github.com/vempi/course-python-programming/assets/34568583/bdff0068-594e-4a04-b73f-0d2cac0a26fd)


# Filtering and grouping temporal series

Anda dapat mengelompokkan data berdasarkan waktu, misalnya per bulan atau per tahun. Misalnya, untuk menghitung rata-rata tahunan dari data hujan:
```
ann_prec = precip.resample(time='1M').mean()
print(ann_prec)
```
Anda dapat mereratakan data hujan untuk semua nilai lat dan lon, sehingga tersisa dimensi waktu saja.
```
# Mereratakan data hujan berdasarkan dimensi lat dan lon
id_prec = prec.mean(dim=['lat', 'lon'])
print(id_prec)

# plot data hujan rata-rata seindonesia
# Grafik hanya akan menampikan garis plot nilai hujan secara timeseries)
id_prec.plot()
plt.show()

```

![image](https://github.com/vempi/course-python-programming/assets/34568583/688932bf-180c-4fe1-9649-c4a818991c8d)


<h1>&#10003; Satellite / remote sensing data analysis </h1>

<h1>&#10003; Spatiotemporal operation </h1>

---
# Check Pembelajaran Pertemuan-12 (Kuis singkat)
Soal 1. 
Download data DAS Barito dari website `https://vempi.staff.ugm.ac.id/dataset/` untuk nomor `7. GIS: SHP DAS se-Indonesia`. 

Download netCDF hujan bulanan PERSIANN untuk area DAS tersebut. 

Soal 2. 

Buat grafik (timeseries) bulanan rerata DAS. Kapan masingmasing puncak musim kering dan basah terjadi?  

Soal 3. 

Buat peta hujan rerata DAS masing-masing untuk bulan Okt-Mar dan Apr-Sep.

---
