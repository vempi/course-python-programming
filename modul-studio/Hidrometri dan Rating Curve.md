Soal Praktik Studio Pemrograman Komputer  Program Hidrometri dan Rating Curve Tahun 2024

A.	Maksud dan Tujuan

Mahasiswa mampu menyusun program python yang dapat menghasilkan grafik rating curve yang menunjukkan hubungan antara ketinggian air dan debit pada sungai yang ditinjau sehingga didapatkan persamaan rating curve yang dapat digunakan untuk perhitungan hidrologi lainnya.

B.	Input

Data yang diinput pada program Hidrometri dan Rating Curve adalah sebagai berikut :
1)	Koordinat profil sungai (m)
2)	Lebar sungai (m)
3)	Kecepatan aliran sungai (m/s)

C.	Output

Output dari program Hidrometri dan Rating Curve ini adalah sebagai berikut :
1)	Grafik rating curve
2)	Persamaan rating curve

D.	Batasan
1)	Beda tinggi iterasi = 0,1 m
2)	Kecepatan aliran di sepanjang penampang dianggap konstan
3)	Input berupa file excel berisi data kedalaman air pada tiap pias bernilai bebas

E.	Variabel
1)	Tinggi Air (h) 
2)	Beda tinggi (dh)
3)	Kecepatan air (v)
4)	Debit (Q)
5)	Jumlah pias (n)
6)	Lebar Pias (B)

F.	Cara Kerja Program

Alur kerja program adalah sebagai berikut:
1)	Input data seperti pada sub bab B
2)	Mencari debit air dengan metode Mid Section Method untuk tiap kenaikan 0,1 m dari air
3)	Menuliskan semua nilai hubungan H dan Q yang didapat
4)	Mencari regresi linear dari nilai H dan Q yang didapat
5)	Membuat persamaan rating curve
6)	Membuat grafik plotting nilai H dan Q dan hasil plotting persamaan rating curve yang didapat

G.	Persamaan dasar 
-	Persamaan Mid Section Method :
  
 ![image](https://github.com/vempi/course-python-programming/assets/107161599/b9d43fc0-df8f-4fa3-a7f9-a3b530245884)

dengan:

qi = Debit pada pias (m3/s)

Vi = Kecepatan aliran air pada pias (m/s)

di = Kedalaman air pada pias (m)

Δwi = Lebar pias (m)

Q = Debit total (m3/s)

-	Persamaan untuk regresi linear rating curve:
  
  ![image](https://github.com/vempi/course-python-programming/assets/107161599/f0d8b831-105f-4000-871e-0febbfdeae30)

Dengan:

Q = debit (m3/s)

H = tinggi air (m)

H.	Contoh Output Program

  ![image](https://github.com/vempi/course-python-programming/assets/107161599/f7dc1bf0-abe5-4147-9e1a-9b4966b73a3a)

  ![image](https://github.com/vempi/course-python-programming/assets/107161599/082b9eeb-681d-4490-94be-844b1ef01215)
