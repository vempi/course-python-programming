# Soal Praktik Studio Pemrograman Komputer Tahun 2024
# Program Desain Mercu Bendung

## A.	Maksud dan Tujuan

Mahasiswa mampu menyusun program python yang dapat menghitung dimensi dan menghasilkan gambar desain mercu bendung dan kolam olak dari hasil perhitungan mercu bendung dan kolam olak tersebut.

## B.	Input

Data yang diinput pada program Desain Mercu Bendung adalah sebagai berikut :
1)	Elevasi mercu (m)
2)	Elevasi dasar sungai (m)
3)	Jumlah pilar
4)	Lebar sungai (m)
5)	Debit (m3/s)
6)	Slope atau kemiringan dasar sungai
7)	Koefisien Debit
8)	Angka Manning
9)	Kemiringan lereng sungai

## C.	Output

Output dari program Desain Mercu Bendung ini adalah sebagai berikut :
1)	Gambar desain mercu bendung
2)	Dimensi bagian mercu bendung

## D.	Batasan
1)	Koefisien kontraksi pilar yang digunakan adalah untuk pilar bulat = 0,01
2)	Koefisien kontraksi pangkal bendung (Untuk pangkal tembok segi empat dengan hulu pada 90o ke arah aliran) = 0,02

## E.	Variabel
1)	Elevasi mercu (m)
2)	Elevasi dasar sungai (m)
3)	Jumlah pilar
4)	Lebar sungai (m)
5)	Debit (m3/s)
6)	Kemiringan dasar sungai
7)	Koefisien debit
8)	Koefisien manning
9)	Kemiringan lereng saluran

## F.	Cara Kerja Program

Alur kerja program adalah sebagai berikut:
1)	Input data seperti pada sub bab B
2)	Mencari tinggi energi di atas mercu
3)	Mencari tinggi air di hilir
4)	Mencari dimensi kolam olak
5)	Menggambar desain mercu bendung sesuai dengan ukuran hasil perhitungan

## G.	Persamaan dasar 
-	Parameter Perancangan Mercu

![image](https://github.com/vempi/course-python-programming/assets/34568583/32a9c009-a00f-4311-a717-50327773a40a)

   R = (0,3-0,7)H1
   untuk tugas, digunakan 0,5H1
-	Debit di atas Bendung:
  
 ![image](https://github.com/vempi/course-python-programming/assets/107161599/6baf1440-69dc-4355-abed-c68e26303b4b)

  dengan:

  Q = Debit (m3/s)

  Cd = Koefisien Debit (umumnya 1,33)

  b = Lebar Efektif Bendung (m)

  H1 = Tinggi Energi di atas Bendung (m) = H + k

  H = Tinggi air (m)

  k = Gradien kehilangan energi (m) = v2 / 2g

-	Lebar Efektif Bendung:
  
  dengan:

  Be = Lebar Efektif (m)

  n = Jumlah pilar

  Kp = Koefisien Kontraksi Pilar

  Ka = Koefisien Kontraksi Pangkal Bendung

-	Rumus Vlugter:

![image](https://github.com/vempi/course-python-programming/assets/107161599/339cb177-1918-4421-bed1-8847d6bd3915)

  dengan:
  
 ![image](https://github.com/vempi/course-python-programming/assets/107161599/d1e58548-5648-47f6-97b5-bf10dc138f11)

  Keterangan:
  hc = Tinggi air kritis (m)
  
  H = tinggi air (m)
  
  k = Gradien kehilangan energi (m)

## H.	Contoh Perhitungan

a)	Debit

  ![image](https://github.com/vempi/course-python-programming/assets/107161599/0191b5a3-03e7-4c0b-b5ff-4cf90a9de08c)
  
  ![image](https://github.com/vempi/course-python-programming/assets/107161599/df42f382-458d-4665-976b-1a13be329a23)

b)	Lebar Efektif

 ![image](https://github.com/vempi/course-python-programming/assets/107161599/3349c931-a3cf-47d1-af77-64201136064f)
 
 ![image](https://github.com/vempi/course-python-programming/assets/107161599/f35f8f6e-fbb7-4c6e-a596-bb94f208e9b7)

 
c)	Rumus Vlugter

 ![image](https://github.com/vempi/course-python-programming/assets/107161599/8a4466a7-23d5-41f6-be5d-8f736ac34bfa)


