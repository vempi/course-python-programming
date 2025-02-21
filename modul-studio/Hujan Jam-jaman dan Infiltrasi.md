# A. Maksud dan Tujuan  
Curah hujan jam-jaman merujuk pada pola distribusi waktu dan spasial dari curah hujan dalam suatu wilayah tertentu selama rentang waktu satu jam. Pemahaman tentang curah hujan jam-jaman bertujuan untuk mengevaluasi risiko banjir, merencanakan infrastruktur air, dan mengelola sumber daya air.  

# B. Input  
Data yang diinput pada program Curah Hujan Jam - Jam dan Infiltrasi berupa tabel dengan isian sebagai berikut:  
- **Curah Hujan Kala Ulang** (n Tahun)  
- **Kala Ulang** (Tahun)  
- **Kedalaman Runoff** (limpasan)  
- **Luas DAS**  
- **CN**  

# C. Output  
Output dari program curah hujan jam-jaman ini adalah sebagai berikut:  
- **Hyetograph Hujan** (mm)  
- **Indeks Infiltrasi**  

# D. Batasan  
- Kedalaman runoff harus positif  

# E. Variabel  
- **Curah Hujan** (mm)  
- **Kedalaman Runoff** (mm)  

# F. Cara Kerja Program  
1. Input data berupa curah hujan harian maksimum untuk kala ulang *n* tahun.  
2. Cari waktu konsentrasi dengan *Australian Rainfall-Runoff*.  
3. Cari intensitas hujan dengan durasi jam-jaman menggunakan Mononobe dan buat *hyetograph* dengan ABM atau menggunakan metode Huff.  
4. Cari indeks infiltrasi dengan mencari hujan efektif SCS - CN.  
5. Didapat indeks infiltrasi (*phi-index*).  

# G. Persamaan Dasar  

## 1. Mencari Konsentrasi Waktu (*tc*)  
### Rumus Kirpich  
\[
tc  = 0.0663 \times L^{0.77} \times S^{-0.385}
\]  
### Australian Rainfall-Runoff  
\[
tc = 0.76 \times A^{0.38}
\]  

## 2. Mencari Intensitas Hujan (mm/jam)  
### Mononobe  
Metode ini berfokus pada analisis data hujan yang diukur dalam interval jam-jaman (misalnya setiap jam) untuk menemukan pola atau tren dalam distribusi curah hujan.  

\[
I = \frac{R_{24}}{24} \times \left(\frac{24}{t}\right)^{\frac{2}{3}}
\]  

Keterangan:  
- \( R_{24} \) = Intensitas hujan harian maksimum (mm)  
- \( I \) = Intensitas hujan pada durasi *t* dengan kala ulang *T* tahun  
- \( t \) = Durasi hujan (jam)  

## 3. Sebaran Hujan Jam-Jaman  

### **Alternating Block Method (ABM)**  
1. Cari **kedalaman kumulatif**:  
   \[
   P = I \times Td
   \]  
   - \( P \) = Kedalaman hujan kumulatif (mm)  
   - \( I \) = Intensitas hujan pada durasi *t* dengan kala ulang *T* tahun  
   - \( Td \) = Durasi hujan (jam)  
2. Tentukan **incremental depth** (\( P_i - P_{i-1} \)).  
3. Urutkan dengan nilai incremental depth terbesar berada di tengah.  

### **Metode Huff**  
- **Pendekatan distribusi hujan** berdasarkan probabilitas kejadian intensitas hujan tertinggi dalam suatu periode waktu tertentu.  

## 4. Mencari *Phi-Index*  
- *Phi-index* dihitung berdasarkan hujan efektif dengan metode **SCS-CN**.  

# H. Output  
- **Hyetograph Hujan** (mm)  
- **Indeks Infiltrasi**  
