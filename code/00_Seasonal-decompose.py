"""
Dekomposisi Musiman & Uji Stasioneritas Deret Waktu
Debit sungai bulanan — deteksi tren, musiman, dan stasioneritas

Data: Sintetik – dihasilkan langsung oleh program ini
Untuk data asli: ganti blok 'Generate synthetic data' dengan membaca CSV Anda.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller as ADF
from statsmodels.tsa.seasonal import seasonal_decompose

np.random.seed(7)

# ── 1. Generate synthetic monthly discharge (20 years, tropical monsoon) ──────
months    = pd.date_range(start='2004-01', periods=240, freq='ME')
month_num = np.arange(1, 241)

seasonal = 250 + 180 * np.sin(2 * np.pi * (month_num - 2) / 12)  # monsoon peak Jan-Mar
trend    = 0.8 * month_num                                          # slow upward trend
noise    = np.random.normal(0, 25, len(months))
discharge = np.maximum(5.0, seasonal + trend + noise)

resampled = pd.DataFrame({'Discharge': discharge}, index=months)

# ── Uncomment to use your own CSV instead ─────────────────────────────────────
# data = pd.read_csv("data/debit-bulanan.csv", index_col=0)
# data["Date"] = pd.to_datetime(data['Date'])
# resampled = data[["Date", "Discharge"]].resample('ME', on="Date").sum()
# ─────────────────────────────────────────────────────────────────────────────

# Shift to strictly positive before multiplicative decomposition
min_val = resampled['Discharge'].min()
if min_val <= 0:
    resampled['Discharge'] = resampled['Discharge'] - min_val + 10.0

# ── 2. Decompose into trend + seasonal + residual ─────────────────────────────
decom = seasonal_decompose(resampled['Discharge'], model='multiplicative', period=12)

fig, axes = plt.subplots(3, 1, sharex=True, figsize=(11, 8))

axes[0].plot(decom.observed, color='steelblue',  linewidth=1.2, label='Data Asli')
axes[1].plot(decom.seasonal, color='seagreen',   linewidth=1.2, label='Komponen Musiman')
axes[2].plot(decom.trend,    color='tomato',     linewidth=1.5, label='Tren')

labels = ['Deret Waktu Asli (m³/s)', 'Komponen Musiman', 'Tren']
for ax, lbl in zip(axes, labels):
    ax.set_ylabel(lbl, fontsize=10)
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(alpha=0.35)

axes[2].set_xlabel('Tahun', fontsize=11)
plt.suptitle('Dekomposisi Musiman – Debit Sungai Bulanan (Sintetik)',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('dekomposisi_musiman.png', dpi=150, bbox_inches='tight')
plt.show()

# ── 3. ADF Stationarity test ──────────────────────────────────────────────────
def stationarity_adf_test(series, label='', alpha=0.05):
    clean = series.dropna()
    result = ADF(clean, autolag='AIC')

    print(f"\n{'='*55}")
    print(f"  Uji Stasioneritas ADF  |  {label}")
    print(f"{'='*55}")
    print(f"  ADF Statistic  : {result[0]:>10.4f}")
    print(f"  p-value        : {result[1]:>10.4f}")
    for conf, val in result[4].items():
        print(f"  Critical ({conf:>3}) : {val:>10.4f}")

    if result[1] > alpha:
        print(f"\n  KESIMPULAN : TIDAK stasioner  (p = {result[1]:.4f} > α = {alpha})")
        print("  Saran      : coba differencing (df.diff()) atau transformasi log")
    else:
        print(f"\n  KESIMPULAN : STASIONER  (p = {result[1]:.4f} <= α = {alpha})")

stationarity_adf_test(resampled['Discharge'], label='Debit Asli')
stationarity_adf_test(decom.resid,            label='Komponen Residual')
