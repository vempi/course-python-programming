# Diagran Windrose

## A. Maksud dan Tujuan
Membuat grafik yang memvisualisasikan distribusi arah dan kekuatan angin serta
gelombang laut dalam suatu wilayah.

## B. Input
Data yang diinput pada program Pantai: Wind Rose dan Gelompang berupa tabel dengan
isian sebagai berikut :
1) Data kecepatan angin interval dalam satu interval waktu.
2) Data kecepatan gelombang interval dalam satu interval waktu.
3) Data arah angin dalam satu satuan interval waktu.
4) Data arah gelombang dalam satu satuan interval waktu.

## C. Output
Output dari program Pantai: Wind Rose dan Gelompang ini adalah sebagai berikut :
1) Grafik windrose dari kecepatan angin atau gelombang terhadap frekuensi
D. Batasan
1) Jumlah maksimal sudut arah angin = 360 derajat
2) Rotasi sudut searah jarum jam, jadi input sudut harus positif
3) dst

## E. Variabel
1) Arah angin
2) Kecepatan angin / Tinggi gelombang
3) Arah datang gelombang

## F. Cara Kerja Program
1) Input data berupa file excel yang memiliki kolom tahun, bulan, hari, arah datangnya
angin/gelombang, dan kecepatan.
2) Tentukan range dari tiap mata angin. Range ditentukan dengan cara membagi 360
derajat dengan jumlah mata angin.
Misalkan :
360 derajat/8 = 45 derajat
Distribusi pembagian arah mata angin menjadi :

![image](https://github.com/vempi/course-python-programming/assets/116259053/b7a86c82-f7bf-43b0-9e8c-1e1cda30a7d8)

4) Tentukan range kelas kecepatan
5) Kategorikan data angin yang kita punya sesuai dengan arah dan kelas kecepatannya.
6) Hitung persentase masing - masing kategori terhadap keseluruhan data.
7) Gambar windrose.
8) Hasil dari pembacaan excel akan di plot dalam diagram windrose menggunakan
matplotlib. Diagram ini akan membaca arah dan kecepatan dari data, menghitung
frekuensinya, dan kemudian membuat diagram windrose berdasarkan data tersebut.

## G. Persamaan dasar
Persamaan yang digunakan adalah Pantai: Wind Rose dan Gelompang :
● Persamaan untuk membagi arah mata angin :
f(θi) = 360/n
● Plot setiap data menjadi pasangan fungsi :
f(θ, s, freq) = fungsi yang terbentuk dari sudut, kecepatan angin, dan frekuensi.

![image](https://github.com/vempi/course-python-programming/assets/116259053/d47deb3b-98d6-4c45-838d-0d1ddcaf97a9)


