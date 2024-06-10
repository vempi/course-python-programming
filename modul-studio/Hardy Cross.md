Soal Praktik Studio Pemrograman Komputer
Analisa Jaringan Pipa Menggunakan Hardy Cross
Tahun 2024


A. Maksud dan Tujuan
Mahasiswa mampu menyusun program komputer yang dapat mempresentasikan teori
analisa jaringan pipa menggunakan metode Hardy Cross.

B. Input
Data yang diinput pada program perhitungan Analisa Jaringan Pipa adalah sebagai berikut:  
1. Panjang pipa
2. Diameter pipa 
3. Darcy friction factor
4. Debit masuk/keluar

C. Output
Output dari program perhitungan Analisa Jaringan Pipa adalah sebagai berikut : 
1. Debit dan arah aliran tiap pipa
2. Gambar konfigurasi pipa di matplotlib, serta debit dan arah alirannya

D. Batasan
Pipa memiliki 2 loop pipa dengan konfigurasi sebagai berikut :


![image](https://github.com/vempi/course-python-programming/assets/109814117/770054f9-2643-462a-b70f-a893619fc63c)


E. Variabel
1. Headloss (m)
2. Diameter (m)
3. Panjang (m)
4. Debit (m3/s)

F. Cara Kerja Program
1. Input nilai panjang dan diameter pipa (dalam satuan m)
2. Input nilai Darcy friction factor
3. Input nilai debit masuk/keluar di setiap titik (dalam satuan m^3/s)
4. Gambar konfigurasi pipa dengan debit keluar dan masuknya
5. Hitung nilai friction coefficient (K’) setiap pipa dengan rumus K' = 2.916 x f x L / D^5
6. Masukkan nilai dan arah debit ke setiap pipa (dapat digunakan asumsi)
7. Kelompokkan pipa dalam 2 loop pipa
8. Cek arah pipa apakah searah jarum atau tidak
9. Jika searah jarum jam maka aliran bernilai positif dan negatif bila sebaliknya
10. Hitung nilai -ΣkQ^2 dan Σr2kQ untuk setiap loop pipa
11. Hitung nilai delta = kQ^2/2kQ untuk setiap loop pipa
12. Jumlahkan semua nilai debit pipa dengan delta sesua loop pipa
13. Lakukan iterasi sampai delta = 0
14. Didapat nilai debit tiap pipa dalam satuan m^3/s
15. Tambahkan keterangan nilai debit dan arahnya pada gambar

G. Persamaan dasar 
Persamaan yang digunakan adalah:
1. Persamaan Kontinuitas 

a. Aliran dalam pipa harus memenuhi hukum-hukum gesekan ppa untuk aliran dalam pipa tunggal : 

![image](https://github.com/vempi/course-python-programming/assets/109814117/9d8f4640-cfea-4440-9187-0551232a9330)

Keterangan : 

hf = head loss (energy loss due to friction)

f 	= Darcy-Weisbach friction factor

L	= Panjang pipa

D	= Diameter pipa

Q	= Debit pipa

b. Aliran masuk ke dalam tiap-tiap titik simpul harus sama dengan aliran yang keluar.

![image](https://github.com/vempi/course-python-programming/assets/109814117/8e88cd43-8cc5-4e4f-8cde-c01ad1c33487)

c. Jumlah aljabar dari kehilangan tenaga dalam satu jaringan tertutup harus sama dengan nol

![image](https://github.com/vempi/course-python-programming/assets/109814117/e28d3285-d61b-4dfa-aff1-dee926d4223b)

2. Persamaan Energi

a. Hubungan antara kehilangan tenaga dan debit 

![image](https://github.com/vempi/course-python-programming/assets/109814117/2694e0ac-da37-4c6c-af3c-ffd1230b3a93)

Keterangan : 
Q 	= Debit pipa
k dan m 	= Tergantung karakteristik dan rumus gesekan pipa

b. Koreksi Debit ΔQ

![image](https://github.com/vempi/course-python-programming/assets/109814117/7625184d-95e9-4457-8255-d7ff2a30e44f)

Referensi
Triatmodjo, B. (2020). Hidraulika II. Yogyakarta: Beta Offset.
Triatmodjo, B. (2020). Soal dan Penyelesaian Hidraulika II. Yogyakarta: Beta Offset.
Lindeburg, M. R. (1999). Civil Engineering Reference Manual for the PE exam. Professional
Publications.
C. E. A. (2015, January 2). Water Resources - Solve for Flow in a Pipe Network using Hardy Cross
Method. YouTube. https://www.youtube.com/watch?v=OwZuT-LwPFw
C. E. F. (2022, January 18). Hardy cross method for pipe network. YouTube.
https://www.youtube.com/watch?v=7aBS_QLUJ6U
