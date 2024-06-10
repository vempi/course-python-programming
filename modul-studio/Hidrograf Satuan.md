# Soal Praktik Studio Pemrograman Komputer Analisa Debit Aliran Menggunakan Hidrograf Satuan Tahun 2024



## A. Maksud dan Tujuan

Mahasiswa mampu menyusun program komputer yang dapat menghitung debit aliran dari hujan menggunakan metode hidrograf satuan dan hidrograf satuan sitentis metode Nakayasu.

## B. Input

Data yang diinput pada program analisa debit aliran adalah sebagai berikut: 
#### a.	Hidrograf satuan 
1.	Debit (m3/d) 
2.	Hujan (mm) 
3.	Waktu (Jam)
4.	Luas DAS

#### b.	Hidrograf Satuan Metode Nakayasu
1.	Luas DAS (m2)
2.	Panjang Sungai (m)
3.	Curah Hujan Satuan (mm)
4.	Koefisien Debit Puncak
5.	Waktu puncak (Jam)
6.	Koefisien Karakteristik DAS


## C. Output

Output dari program ini adalah:
Grafik Hidrograf Satuan dan Grafik HSS Metode Nakayasu

## D. Batasan

1.	Interaksi antara hujan dan banjir tidak terikat oleh waktu kejadiannya
2.	Baseflow dianggap konstan
3.	Input berupa file excel berisi data input 

## E. Variabel

#### a.	Hidrograf satuan 
1.	Debit (m3/d) 
2.	Hujan (mm) 
3.	Waktu (Jam)
4.	Luas DAS (m2)

#### b.	Hidrograf Satuan Metode Nakayasu
1.	Debit puncak banjir (m3/d)
2.	Panjang Sungai (m)
3.	Waktu puncak (s)
4.	Luas DAS (m2)
5.	Curah hujan efektif (mm)
6.	Waktu permulaan banjir sampai puncak hidrograf (Jam)
7.	Waktu dari puncak banjir sampai 0,3 kali debit puncak (Jam)
8.	Waktu konsentrasi (Jam)
9.	Satuan waktu dari curah hujan (Jam)
10.	Koefisien Karakteristik DAS


## F. Cara Kerja Program

#### 1.	Hidrograf satuan 
a.	Input nilai yang ada di poin (b)
b.	Cari volume limpasan (VLL)
c.	Cari kedalaman aliran (h)
d.	Cari Hidrograf Satuan (m3/d)
e.	Buat grafik Hidrograf Satuan 

#### 2.	HSS Metode Nakayasu
a.	Input nilai yang ada di poin (b)
b.	Cari waktu konsentrasi hujan (Tg)
c.	Cari satuan waktu dari curah hujan (tr)
d.	Cari waktu puncak (Tp)
e.	Cari waktu 30% dari debit puncak (T0,3)
f.	Cari Debit Puncak (Qp)
g.	Cari Baseflow (m3/d)

## G. Persamaan dasar 

### 1. Hidrograf Satuan 
#### a. Total Direct Runoff Volume

![image](https://github.com/vempi/course-python-programming/assets/109814117/27bb68bd-c524-4a56-acb1-b5fe2e53c8b1)


Keterangan :

ΣQ = Total Debit

Δt   = Range Waktu 

#### b. Direct Runoff Depth 

![image](https://github.com/vempi/course-python-programming/assets/109814117/9d041937-242e-4442-b546-93c8f3734a4f)

Keterangan :

VLL = Volume Limpasan Langsung

A   = Luas Area 

### 2. HSS Metode Nakayasu
#### a. Debit Puncak

![image](https://github.com/vempi/course-python-programming/assets/109814117/4f0231fd-b245-46af-88a9-f6fda769b18d)


Keterangan : 

C 	= Koefisien Debit Puncak

A 	= Luas Area 

R 	= Curah Hujan Satuan 

Tp 	= Waktu Puncak 

#### b. Time Lag

![image](https://github.com/vempi/course-python-programming/assets/109814117/b13c73f1-854c-4aba-81ac-00713f8931d6)


Keterangan : 

L = Panjang Sungai 

#### c. Waktu Puncak 

![image](https://github.com/vempi/course-python-programming/assets/109814117/f8fbb7bd-5e9a-43c7-be07-664629fccf3a)


Keterangan :

Tg = Waktu konsentrasi hujan

Tp = Waktu Puncak 

#### d. Bentuk Kurva

![image](https://github.com/vempi/course-python-programming/assets/109814117/8f84fb54-8436-4f5f-94d5-9dc5aa4e35ac)


Keterangan :

Qp = Debit Puncak

Tg = Waktu konsentrasi hujan

Tp = Waktu Puncak 

T0,3= Waktu 30% dari debit puncak


## Referensi

Natakusumah, D. K., Hatmoko, W., & Harlan, D. (2011). Prosedur umum perhitungan hidrograf satuan sintetis dengan Cara ITB dan Beberapa Contoh Penerapannya. Jurnal Teknik Sipil, 18(3), 251-291.

Triatmodjo, B. (2008). Hidrologi Terapan Yogyakarta: Beta Offset
