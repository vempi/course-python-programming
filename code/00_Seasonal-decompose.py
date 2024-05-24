"""
Program to check for stationarity of a
time series signal and decompose it
into trend and seasonal components
"""

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller as ADF
from statsmodels.tsa.seasonal import seasonal_decompose

# Read data
data = pd.read_csv("E:/Downloads/Pamarayan-debit-hujan.csv",index_col=0)
data["Date"] = pd.to_datetime(data['Date'])

df = data[["Date", "Discharge"]]

# Downsample the time series
resampled = df.resample('M', on="Date").sum()

#Transform the data
def transform(x):
    x = x - minx + 10.0
    return x

def inverse_transform(x):
    x = x - 10.0 + minx
    return x

#Transform data
minx = resampled.min()
resampled = transform(resampled)

#Decompose a signal (multiplicative/additive)
decom = seasonal_decompose(resampled, model="multiplicative")

fig, ax = plt.subplots(nrows=3, ncols=1, sharex=True,figsize=(8, 6))
ax[0].plot(decom.observed, label='Time series')
ax[1].plot(decom.seasonal, label='Seasonal')
ax[2].plot(decom.trend, label='Trend')
ax[0].set_ylabel('Series')
ax[1].set_ylabel('Seasonal')
ax[2].set_ylabel('Trend')
ax[2].set_xlabel('Year')
ax[0].grid(ls='--')
ax[1].grid(ls='--')
ax[2].grid(ls='--')
plt.tight_layout()
#plt.savefig('seasonal.pdf', dpi=300)


# Stationarity check
def stationarity_adf_test(x, alpha=0.05):
    adftest_res = ADF(x, autolag="AIC")
    dfout = pd.Series(adftest_res[0:4], index=["ADF statistic", "ADF p-value",
                                               "ADF lags used", "ADF number of obs used"])
    for key, value in adftest_res[4].items():
        dfout[" Critical Value (%s)" % key] = value
        print(dfout)
        if dfout["ADF p-value"] > alpha:
            print(" Result: Non-stationary time series", "\n")
        else:
            print(" Result: Stationary time series", "\n")
        print("\nChecking stationarity:")
        
stationarity_adf_test(resampled)