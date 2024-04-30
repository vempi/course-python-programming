<blockquote style="background-color: #f9f9f9; border-left: 5px solid #ccc; padding: 10px;">
This is a callout box. You can use it to highlight important information or provide additional context.
</blockquote>

# Hidraulika Saluran Terbuka 1D (Manning-Strickler Formula)
## Persamaan Manning
Persamaan ini adalah rumus empiris dalam hidraulika saluran terbuka yang mendeskripsikan hubungan antara kecepatan di dalam saluran (V) dan geometri lebar dan kedalaman saluran (B,h), kemiringan (S), dan koefisien gesekan yang dinyatakan sebagai koefisien Manning n.

![image](https://github.com/vempi/course-python-programming/assets/108465312/2d958b63-3612-49df-bce8-caccdf799f96)




---
Contoh mengolah perhitungan kedalaman saluran menggunakan Python
---

```{python}
import numpy as np
import matplotlib.pyplot as plt

# fungsi perhitungan kedalaman saluran dengan meetode iterasi
def kedalaman(Q,n,S,B,hi,ndata,toleransi,iterasi):
    ht = np.zeros(ndata)
    k=0
    while k < ndata:
        ht[k] = ((Q[k]*n[k]*((B[k]+2*hi[k])**(2/3))/(S[k]**0.5))**(3/5))/B[k]
        if abs(ht[k]-hi[k]) > toleransi:
                hi[k] = ht[k]
        else:
                break
        k = k+1   
    return ht

# Membuka file data input berupa txt 
with open('Channel_data.txt','r') as file:
    next (file)
    
    data_saluran = np.array([line.strip().split() for line in file], dtype = float)

# membaca tabel dari data input sebagai variabel
Ch = data_saluran[:,0]    
Q = data_saluran[:,1]
ndata = len(Q)
S0 = data_saluran[:,2]
nm = data_saluran[:,3]
B = data_saluran[:,4]

hi = np.zeros(ndata)
toleransi = 0.001
iterasi = 1000

# call function
ht = kedalaman(Q,nm,S0,B,hi,ndata,toleransi,iterasi)
print(Ch,Q,S0,nm,B,ht)

# Menyimpan file ouput berupa tabel dalam bentuk txt
output = np.transpose(np.array([Ch,Q,S0,nm,B,ht]))
header = "Saluran\tQ\tS\tnm\tB\tht"
underline ='---'*len(header)
np.savetxt('Output.txt', output, fmt = '%.2f', delimiter = '\t', header = f"{header}\n{underline}", comments='')
