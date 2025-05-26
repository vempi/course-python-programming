---
# Capaian pembelajaran Pertemuan-13
  1. Menggabungkan multiple NetCDF files
  2. Melakukan modifikasi kordinat ruang dan waktu
  3. Visualisasi data hujan dari NetCDF dalam bentuk peta (contourf, pcolormesh) dan timeseries
  4. Menganalisis timeseries curah hujan 
  5. Menyimpan data hasil ekstraksi dalam format CSV atau GeoTIFF
     
---
<h2>&#10003; Menggabungkan multiple NetCDF files</h2> 
```python
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import os, glob

# ======================= 1. Membaca multiple file ncdf ====================== #

# Menentukan directory
os.chdir('E:/Downloads/IMERG')

# Memilih seluruh file dengan ekstensi nc 
lst  = glob.glob('*.nc4')

# Membaca seluruh file dan dicombine jadi satu file menggunakan xarray
d = xr.open_mfdataset(lst)

# Menghitung statistik along time dimension
d_sum = d.sum(dim='time')
d_mean = d.mean(dim='time')
d_max = d.max(dim='time')

# Lat lon ternyata masih tertukar
d_sum.precipitationCal.plot(robust=True)

# Melakukan transpose lat lon
t_sum = d_sum.transpose('lat', 'lon')

# Lat lon ternyata masih tertukar
t_sum.precipitationCal.plot(robust=True)
plt.savefig("coba.png")

```
<h2>&#10003; Melakukan modifikasi kordinat ruang dan waktu</h2>
```python
# ============================= 2. Mengeksplor dimensi ============================= #

os.chdir('C:/Users/lenovo/OneDrive - UGM 365/Bahan Kuliah/MTS_Hidroinformatika/Data-hujan-IMERG')

# Memilih seluruh file dengan ekstensi nc
lst  = glob.glob('*.nc4')

# Membaca seluruh file dan dicombine jadi satu file menggunakan xarray
d = xr.open_mfdataset(lst)

d_mean = d.mean(dim=['lat','lon'])

# Titik pos hujan BMKG
# Stasiun Meteorologi Sultan Syarif Kasim II
# Lintang : 0.45924. Bujur : 101.44743

dpoint = d.sel(lat=0.45924, lon=101.44743, method='nearest')

df = dpoint.to_dataframe()
df = df.iloc[:, :1]
df.columns = ['rain']
df.to_csv("GPM_Pekanbaru.csv")

```

```python
d = xr.open_dataset("E:/Downloads/3B-DAY.MS.MRG.3IMERG.20110101-S000000-E235959.V06.nc4 (1).nc4")
d.precipitationCal.plot()
data = d.transpose('time','lat', 'lon')
d.precipitationCal.plot()
arr = d.precipitationCal.values
arr.shape

rot_arr = np.rot90(arr, axes=(1, 2))
rot_arr = np.moveaxis(rot_arr, 0, -1)
plt.imshow(arr[0,:,:])

rot_arr.shape
rot_d = xr.DataArray(rot_arr, coords=[d.lat, d.lon, d.time], 
                     dims=['lat', 'lon', 'time'])

```

<h2>&#10003; Visualisasi data hujan dalam bentuk timeseries dan peta (pcolormesh/contour)</h2>
# ============================= 3. Membuat peta ============================= #
```python
data = t_sum

# Load shapefile landmask
land_mask = cfeature.NaturalEarthFeature('physical', 'land', '50m', edgecolor='face')

# plot
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

# Plot map
plot = data.precipitationCal.plot(ax=ax, transform=ccrs.PlateCarree(), cmap='rainbow', 
                                  robust=True, add_colorbar=False)

# Overlay landmask
#ax.add_feature(land_mask, facecolor='lightgray')

# Garis pantai
ax.coastlines()

# Add title and labels
ax.set_title('Total Rainfall in December 2011')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')


# Memberikan label tick coordinat 
ax.set_xticks(range(95,145,5), crs=ccrs.PlateCarree())
ax.set_yticks(range(-10,8,2), crs=ccrs.PlateCarree())

# Create a color bar with same height as the plot
cbar = plt.colorbar(plot,fraction=0.019, pad=0.04)
cbar.set_label('Rainfall (mm)')

# Show the plot
plt.show()

```
<h2>&#10003; Analisis tren curah hujan menggunakan Sen’s slope atau linear regression</h2>

```python
# ============================= 4. Analisis tren ============================= #
import numpy as np
from scipy.stats import linregress
import pandas as pd

# Data titik lokasi tertentu
dpoint = d.sel(lat=0.45924, lon=101.44743, method='nearest')

# Ambil array waktu dan data hujan
rain = dpoint.precipitationCal.values
time = pd.to_datetime(dpoint.time.values)

# Hitung tren dengan regresi linear
x = np.arange(len(time))
slope, intercept, r_value, p_value, std_err = linregress(x, rain)

print(f"Tren curah hujan: {slope:.4f} mm/hari per timestep")
print(f"R^2: {r_value**2:.4f}, p-value: {p_value:.4f}")

# Visualisasi tren
plt.figure(figsize=(10,4))
plt.plot(time, rain, label="Curah hujan")
plt.plot(time, intercept + slope*x, 'r', label="Tren linear")
plt.title("Tren Curah Hujan di Pekanbaru")
plt.ylabel("Curah Hujan (mm)")
plt.xlabel("Waktu")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

<h2>&#10003; Menyimpan hasil dalam bentuk CSV untuk analisis lanjutan</h2>
```python
============================= 5. Simpan sebagai CSV ============================= #
# Data series dari lokasi tertentu (sudah diambil sebelumnya: dpoint)
df = dpoint.to_dataframe().reset_index()
df = df[['time', 'precipitationCal']]
df.columns = ['time', 'rain']

# Simpan CSV
df.to_csv("rainfall_trend_pekanbaru.csv", index=False)

============================= 6. Simpan sebagai GeoTIFF =============================

import rioxarray

# Asumsikan kita ingin menyimpan data rata-rata
rain_mean = d.mean(dim='time')

# Simpan GeoTIFF
rain_mean.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
rain_mean.rio.write_crs("EPSG:4326", inplace=True) # WGS84
rain_mean['precipitationCal'].rio.to_raster("mean_rainfall_map.tif")
```
