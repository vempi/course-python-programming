---
# Capaian pembelajaran Pertemuan-14
  1. [Menyiapkan engine (fungsi inti)](#1-menyiapkan-engine)
  2. [Graphical User Interface dengan Tkinter](#2-gui-tkinter)
  3. [Web-based Interface dengan Streamlit](#3-web-interface-streamlit)
---

# 1. Menyiapkan Engine

Sebelum membuat antarmuka, kita perlu memiliki **engine** — yaitu fungsi Python yang melakukan perhitungan inti. Antarmuka hanya bertugas mengumpulkan input dari pengguna dan menampilkan output; seluruh logika perhitungan ada di engine.

Sebagai contoh, kita gunakan **Kalkulator Infiltrasi Horton** yang sudah dipelajari sebelumnya.

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ── ENGINE: fungsi inti perhitungan ───────────────────────────────────────────

def hitung_infiltrasi(f0, fc, k, dt=0.25, t_total=8.0):
    """
    Hitung laju dan kumulatif infiltrasi menggunakan Metode Horton.

    Parameters
    ----------
    f0      : laju infiltrasi awal (mm/jam)
    fc      : laju infiltrasi akhir (mm/jam)
    k       : konstanta deklinasi (1/jam)
    dt      : interval waktu (jam)
    t_total : durasi simulasi (jam)

    Returns
    -------
    df : DataFrame berisi waktu, laju infiltrasi f(t), dan kumulatif F(t)
    """
    t = np.arange(0, t_total + dt, dt)
    f = fc + (f0 - fc) * np.exp(-k * t)
    F = np.cumsum(f * dt)

    return pd.DataFrame({
        'Waktu (jam)'                : t,
        'Laju Infiltrasi f (mm/jam)' : f.round(3),
        'Kumulatif F (mm)'           : F.round(3)
    })


def plot_infiltrasi(df, f0, fc, k, simpan=False):
    """Buat grafik hasil simulasi infiltrasi."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(df['Waktu (jam)'], df['Laju Infiltrasi f (mm/jam)'],
             'steelblue', linewidth=2.5)
    ax1.axhline(fc, color='tomato', linestyle='--', label=f'fc = {fc} mm/jam')
    ax1.set_xlabel('Waktu (jam)')
    ax1.set_ylabel('Laju Infiltrasi (mm/jam)')
    ax1.set_title('Laju Infiltrasi f(t)')
    ax1.legend()

    ax2.fill_between(df['Waktu (jam)'], df['Kumulatif F (mm)'],
                     alpha=0.2, color='seagreen')
    ax2.plot(df['Waktu (jam)'], df['Kumulatif F (mm)'],
             'seagreen', linewidth=2.5)
    ax2.set_xlabel('Waktu (jam)')
    ax2.set_ylabel('Infiltrasi Kumulatif (mm)')
    ax2.set_title('Kumulatif F(t)')

    plt.suptitle(f'Metode Horton  |  f0={f0}, fc={fc}, k={k}', fontsize=12)
    plt.tight_layout()
    if simpan:
        plt.savefig('infiltrasi_hasil.png', dpi=150)
    plt.show()

# ── Uji engine secara langsung ────────────────────────────────────────────────
hasil = hitung_infiltrasi(f0=50, fc=10, k=2.0)
print(hasil.to_string(index=False))
plot_infiltrasi(hasil, f0=50, fc=10, k=2.0)
```

---

# 2. GUI Tkinter

**Tkinter** adalah library bawaan Python untuk membuat aplikasi desktop (GUI). Tidak perlu install tambahan.

Prinsip dasar:
- **Widget** = elemen UI (tombol, kotak teks, label)
- **Layout** = mengatur posisi widget di jendela (`pack`, `grid`, `place`)
- **Event binding** = menghubungkan aksi pengguna (klik tombol) dengan fungsi Python

## 2.1 Struktur Dasar Window

```python
import tkinter as tk

# Buat jendela utama
root = tk.Tk()
root.title("Aplikasi Hidrologi")
root.geometry("400x300")   # lebar x tinggi (pixel)

# Label
lbl = tk.Label(root, text="Selamat datang!", font=("Arial", 14))
lbl.pack(pady=20)

# Tombol keluar
btn = tk.Button(root, text="Keluar", command=root.destroy,
                bg="tomato", fg="white", width=10)
btn.pack()

root.mainloop()   # jalankan event loop
```

## 2.2 GUI Kalkulator Infiltrasi Horton

```python
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use('TkAgg')   # backend matplotlib untuk Tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Pastikan fungsi engine sudah didefinisikan (salin dari Bagian 1)

def jalankan_simulasi():
    """Dipanggil saat tombol 'Hitung' diklik."""
    try:
        f0 = float(entry_f0.get())
        fc = float(entry_fc.get())
        k  = float(entry_k.get())

        if fc >= f0:
            messagebox.showerror("Error", "f0 harus lebih besar dari fc!")
            return
        if k <= 0:
            messagebox.showerror("Error", "k harus bernilai positif!")
            return

        hasil = hitung_infiltrasi(f0=f0, fc=fc, k=k)

        # Update tabel
        for row in tabel.get_children():
            tabel.delete(row)
        for _, baris in hasil.iterrows():
            tabel.insert('', 'end', values=tuple(baris))

        # Update grafik
        ax.clear()
        ax.plot(hasil['Waktu (jam)'], hasil['Laju Infiltrasi f (mm/jam)'],
                'steelblue', linewidth=2, label='f(t)')
        ax.axhline(fc, color='tomato', linestyle='--', label=f'fc={fc}')
        ax.set_xlabel('Waktu (jam)')
        ax.set_ylabel('Laju Infiltrasi (mm/jam)')
        ax.set_title('Kurva Infiltrasi Horton')
        ax.legend()
        canvas.draw()

        label_status.config(text=f"Selesai! Total infiltrasi = {hasil['Kumulatif F (mm)'].iloc[-1]:.1f} mm",
                            fg="green")

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")


# ── Layout Utama ──────────────────────────────────────────────────────────────
root = tk.Tk()
root.title("Simulasi Infiltrasi – Metode Horton")
root.geometry("900x650")

frame_kiri  = tk.Frame(root, padx=15, pady=15)
frame_kanan = tk.Frame(root, padx=5,  pady=5)
frame_kiri.pack(side=tk.LEFT, fill=tk.Y)
frame_kanan.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# ── Panel Input (kiri) ────────────────────────────────────────────────────────
tk.Label(frame_kiri, text="Parameter Tanah", font=("Arial", 13, "bold")).grid(
    row=0, column=0, columnspan=2, pady=(0, 12))

params = [
    ("Laju awal f₀ (mm/jam):", "50"),
    ("Laju akhir fc (mm/jam):", "10"),
    ("Konstanta k (1/jam):",    "2.0"),
]
entries = []
for i, (label, default) in enumerate(params, start=1):
    tk.Label(frame_kiri, text=label, anchor='w').grid(row=i, column=0, sticky='w', pady=4)
    e = tk.Entry(frame_kiri, width=10)
    e.insert(0, default)
    e.grid(row=i, column=1, padx=8)
    entries.append(e)

entry_f0, entry_fc, entry_k = entries

tk.Button(frame_kiri, text="Hitung", command=jalankan_simulasi,
          bg="steelblue", fg="white", font=("Arial", 11), width=12).grid(
    row=5, column=0, columnspan=2, pady=15)

label_status = tk.Label(frame_kiri, text="", fg="green", wraplength=200)
label_status.grid(row=6, column=0, columnspan=2)

# Tabel hasil
tk.Label(frame_kiri, text="Hasil Perhitungan:", font=("Arial", 10, "bold")).grid(
    row=7, column=0, columnspan=2, pady=(10, 2))

cols = ('Waktu (jam)', 'f (mm/jam)', 'F (mm)')
tabel = ttk.Treeview(frame_kiri, columns=cols, show='headings', height=12)
for col in cols:
    tabel.heading(col, text=col)
    tabel.column(col, width=90, anchor='center')
tabel.grid(row=8, column=0, columnspan=2)

# ── Panel Grafik (kanan) ──────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5.5, 4.5))
canvas  = FigureCanvasTkAgg(fig, master=frame_kanan)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

root.mainloop()
```

> **Tips menjalankan:** Simpan kode di atas sebagai file `.py` dan jalankan dari terminal (`python nama_file.py`). Jika menggunakan Jupyter, jalankan dari terminal karena Tkinter memerlukan event loop tersendiri.

---

# 3. Web Interface – Streamlit

**Streamlit** adalah library Python yang memungkinkan pembuatan aplikasi web interaktif hanya dengan beberapa baris kode — tanpa perlu HTML/CSS/JavaScript.

Install sekali dengan:
```
pip install streamlit
```

## 3.1 Aplikasi Streamlit: Kalkulator Infiltrasi

Buat file baru `app_infiltrasi.py` dan isi dengan kode berikut:

```python
# app_infiltrasi.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ── Pastikan fungsi engine sudah ada di file ini ──────────────────────────────
def hitung_infiltrasi(f0, fc, k, dt=0.25, t_total=8.0):
    t = np.arange(0, t_total + dt, dt)
    f = fc + (f0 - fc) * np.exp(-k * t)
    F = np.cumsum(f * dt)
    return pd.DataFrame({
        'Waktu (jam)'               : t,
        'Laju Infiltrasi f (mm/jam)': f.round(3),
        'Kumulatif F (mm)'          : F.round(3)
    })

# ── Layout Streamlit ──────────────────────────────────────────────────────────
st.title("Simulasi Infiltrasi Tanah")
st.subheader("Metode Horton")

st.sidebar.header("Parameter Tanah")
f0      = st.sidebar.slider("Laju awal f₀ (mm/jam)", min_value=5,  max_value=200, value=50)
fc      = st.sidebar.slider("Laju akhir fc (mm/jam)", min_value=1,  max_value=50,  value=10)
k       = st.sidebar.slider("Konstanta k (1/jam)",    min_value=0.1, max_value=5.0, value=2.0, step=0.1)
t_total = st.sidebar.slider("Durasi simulasi (jam)",   min_value=1,  max_value=24,  value=8)

if fc >= f0:
    st.error("f₀ harus lebih besar dari fc!")
    st.stop()

hasil = hitung_infiltrasi(f0=f0, fc=fc, k=k, t_total=t_total)

# Grafik
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.plot(hasil['Waktu (jam)'], hasil['Laju Infiltrasi f (mm/jam)'], 'steelblue', lw=2.5)
ax1.axhline(fc, color='tomato', linestyle='--', label=f'fc = {fc}')
ax1.set(xlabel='Waktu (jam)', ylabel='Laju Infiltrasi (mm/jam)', title='f(t)')
ax1.legend()
ax2.fill_between(hasil['Waktu (jam)'], hasil['Kumulatif F (mm)'], alpha=0.2, color='seagreen')
ax2.plot(hasil['Waktu (jam)'], hasil['Kumulatif F (mm)'], 'seagreen', lw=2.5)
ax2.set(xlabel='Waktu (jam)', ylabel='Kumulatif (mm)', title='F(t)')
st.pyplot(fig)

# Metrik ringkasan
col1, col2, col3 = st.columns(3)
col1.metric("Total Infiltrasi", f"{hasil['Kumulatif F (mm)'].iloc[-1]:.1f} mm")
col2.metric("Laju Awal", f"{f0} mm/jam")
col3.metric("Laju Akhir (dicapai)", f"{hasil['Laju Infiltrasi f (mm/jam)'].iloc[-1]:.2f} mm/jam")

# Tabel hasil
with st.expander("Lihat tabel hasil lengkap"):
    st.dataframe(hasil, use_container_width=True)
```

Jalankan dari terminal:
```bash
streamlit run app_infiltrasi.py
```

Browser akan terbuka otomatis di `http://localhost:8501`. Setiap kali slider digeser, grafik dan tabel langsung diperbarui!

---
# Check Pembelajaran Pertemuan-14 (Kuis singkat)
  1. Modifikasi kode Tkinter di atas agar pengguna juga bisa mengubah **durasi simulasi** (t_total) dan **interval waktu** (dt) melalui kotak input.
  2. Tambahkan tombol **"Simpan CSV"** pada aplikasi Tkinter yang menyimpan tabel hasil ke file `infiltrasi_hasil.csv` menggunakan `pandas.DataFrame.to_csv()`.
  3. Modifikasi aplikasi Streamlit agar dapat mensimulasikan dan membandingkan **tiga jenis tanah** (pasir, lempung, gambut) sekaligus dalam satu grafik. Gunakan parameter yang berbeda untuk masing-masing jenis tanah.
---
