# -*- coding: utf-8 -*-
"""
Kumulatif Curah Hujan Harian per Tahun
Analisis tren musiman curah hujan antar-tahun

Data: Sintetik – dihasilkan langsung oleh program ini (pola monsunal tropis)
Untuk data asli: ganti blok 'Generate synthetic data' dengan membaca CSV Anda.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

np.random.seed(42)

# ── 1. Generate synthetic daily rainfall (10 years, tropical monsoon) ─────────
dates = pd.date_range(start='2014-01-01', end='2023-12-31', freq='D')
doy   = dates.dayofyear  # day-of-year 1..365

# Seasonal signal: peak ~day 30 (Jan) and ~day 340 (Dec), dry May–Sep
seasonal_base = 8 + 7 * np.cos(2 * np.pi * (doy - 30) / 365)
noise         = np.random.exponential(scale=np.abs(seasonal_base) * 0.6)
rainfall      = np.where(seasonal_base > 2, seasonal_base + noise, 0.0)

df = pd.DataFrame({'Date': dates, 'Rainfall': rainfall})
df.set_index('Date', inplace=True)

# ── Uncomment to use your own CSV instead ─────────────────────────────────────
# df = pd.read_csv('data/curah-hujan.csv')
# df['Date'] = pd.to_datetime(df['Date'])
# df.set_index('Date', inplace=True)
# df = df[['Rainfall']]
# ─────────────────────────────────────────────────────────────────────────────

# ── 2. Cumulative rainfall per year ───────────────────────────────────────────
df['year'] = df.index.year

cumrain = df.groupby('year')['Rainfall'].cumsum().reset_index()
cumrain.set_index('Date', inplace=True)
cumrain['year'] = cumrain.index.year
cumrain['DOY']  = cumrain.index.dayofyear

# Rank years wettest → driest
annual_totals = df.groupby('year')['Rainfall'].sum()
wettest = annual_totals.idxmax()
driest  = annual_totals.idxmin()

print(f"Curah hujan tahunan (mm):\n{annual_totals.round(0).to_string()}")
print(f"\n→ Tahun TERLEMBAB : {wettest}  ({annual_totals[wettest]:.0f} mm)")
print(f"→ Tahun TERKERING : {driest}  ({annual_totals[driest]:.0f} mm)")

# ── 3. Plot ────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 6))

years  = sorted(cumrain['year'].unique())
colors = cm.RdYlBu(np.linspace(0.15, 0.85, len(years)))

for i, year in enumerate(years):
    subset = cumrain[cumrain['year'] == year]
    if year == wettest:
        label, lw, ls = f"{year}  ← Terlembab", 2.5, '-'
    elif year == driest:
        label, lw, ls = f"{year}  ← Terkering", 2.5, '--'
    else:
        label, lw, ls = str(year), 1.2, '-'
    ax.plot(subset['DOY'], subset['Rainfall'], color=colors[i],
            linewidth=lw, linestyle=ls, label=label)

ax.set_xlabel('Hari ke- dalam Tahun (DOY)', fontsize=12)
ax.set_ylabel('Curah Hujan Kumulatif (mm)', fontsize=12)
ax.set_title('Curah Hujan Kumulatif Harian per Tahun\n(Pola Monsunal Tropis – Sintetik)',
             fontsize=13, fontweight='bold')
ax.legend(title='Tahun', bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=9)
ax.set_xlim(1, 365)
ax.grid(True, alpha=0.35)
plt.tight_layout()
plt.savefig('cumulative_rainfall.png', dpi=150, bbox_inches='tight')
plt.show()
