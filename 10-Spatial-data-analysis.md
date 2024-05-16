---
# Capaian pembelajaran Pertemuan-10
  1. Memahami struktur data spatial
  2. Membaca data spasial hujan
  3. Spatial analysis (interpolasi) and visualization 
  4. Plotting and mapping
---

<h1>&#x2713; Memahami struktur data spatial </h1>
Kita dapat mendapatkan data curah hujan dari beberapa pos ukur hujan. Lalu kita dapat membuat plot isohyet (kontur) dari curah hujan tersebut. 
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
Setelah itu, peta kontur dapat diperoleh. Fungsi griddata dari pustaka `scipy.interpolate` berguna untuk mendapatkan data bergrid (data pada grid reguler). 
Lalu Kita gunakan fungsi meshgrid dari pustaka numpy, untuk membuat grid dari vektor x dan y yang diberikan.

```{python}
from scipy.interpolate import griddata
# Generate the desired grid, where rainfall is to be interpolated
X, Y = np.meshgrid(np.linspace(min(x), max(x), 1000), np.linspace(min(y), max(y), 1000))

# Perform the gridding
grid_rain = griddata((x, y), rain, (X, Y), method='cubic')# Added method parameter for interpolation
#grid_rain = griddata((x, y), rain, (X, Y), method='linear')# Added method parameter for interpolation

```
Sekarang, kita dapat membuat plot kontur dari data bergrid, yang dibuat oleh fungsi `plt.contourf()`. 
Fungsi contourf membuat kontur terisi yang angka, sementara contour() menyediakan kontur sederhana. 

Kita mulai dengan membersihkan gambar saat ini dengan menggunakan plt.clf(), karena mungkin ada beberapa gambar yang sudah ada di memori.
Kita juga menambahkan lokasi pos  hujan menggunakan `plt.scatter()`. s dan c digunakan untuk menentukan ukuran dan warna penanda. 
`plt.xlim()` dan `plt.ylim()` membatasi rentang sumbu x dan y secara berturut-turut.

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

<h1>&#x2713; Spatial analysis (interpolasi) and visualization  </h1>

<h1>&#10003; Plotting and mapping </h1>

```{python}


```

---
# Check Pembelajaran Pertemuan-10 (Kuis singkat)
  1. Lakukan Filtering data hujan CHIRPS dari file "Data_hujan_multi_harian.csv" hanya pada tahun kelahiran anda. Lalu resample berdasarkan minggu. Di bulan dan minggu ke berapa hujan akumulasi paling besar terjadi?
  2. Visualisasi box plot per bulan berdasarkan data PERSIANN. Bulan apa yang memiliki nilai hujan bulanan tertinggi dan terendah?
  3. Plotkan grafik contoh hubungan hujan debit pada _range_ tanggal kelahiran anda (seminggu sebelum hingga seminggu setelah) berdasarkan data GPM!  
---

