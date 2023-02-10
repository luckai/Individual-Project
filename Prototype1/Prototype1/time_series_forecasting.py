import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv
from datetime import datetime
from IPython.display import display
import seaborn as sb
from numpy import array
from statsmodels.tsa.stattools import adfuller 
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima_model import ARIMA

class TimeSeries():

    def basic():

        path = 'D:\IndividualProject\Prototype\DATA.csv'
        crime = pd.read_csv(path, on_bad_lines='skip', low_memory=False, nrows=200)
        crime.head()

        crime['Date'] = pd.to_datetime(crime['Date'], infer_datetime_format=True)
        crimeindex = crime.set_index('Year', inplace=False)
        crimeindex['Index'] = crimeindex['Date'].dt.strftime('%m')
        crimeindex.groupby('Index').count()
        crimeindex.sort_values(by='Index',ascending=True)
        crimecount = crimeindex.groupby('Date').count()#['Month'].to_frame()
        Count = crime.groupby('Date').count()
        crimeindex = crime[["Date"]]
        plt.ylabel('Year')
        plt.xlabel('No. of Crime')
        plt.plot(crimeindex)
        plt.show()
        #Graph = plt.plot(crimeindex)
        #crime = crime.groupby('Date').count()['Type'].to_frame()
        #crime.columns = ['DATE', 'No of Crimes']
        #crime.head()

    def basictext():
        path = 'D:\IndividualProject\Prototype\DATA.csv'
        crime = pd.read_csv(path, on_bad_lines='skip', low_memory=False, nrows=1000)
        crime.head()
        print(crime)
        message = crime.head()
        print(message)

    def testing(timeseries):
        Average = timeseries.rolling(window=12)
        StanDev = timeseries.rolling(window=12)
        crimeindex = TimeSeries.basic()

        plt.plot(timeseries, color='blue', label='Original')
        plt.plot(Average, color='red', label='Rolling Mean')
        plt.plot(StanDev, color='black', label='Rolling StanDev')
        plt.legend(loc='best')
        plt.title('Rolling Mean & Standard Deviation')
        plt.show(block=False)

        print('Results of Dickey Fuller Test:')
        testing = adfuller(timeseries, autolag='AIC')
        crimeoutput = pd.Series(testing[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
        for key,value in testing[4].items():
            crimeoutput['Critical Value (%s)'%key] = value
            print(crimeoutput)
        

#crimeindex

#built = crime['Date'].value_counts().sort_index()
#fig, ax = plt.subplots(1, 1, figsize=(18, 5))

#ax.plot(built.index, built, color="#a7b688")

#for s in ['top', 'right']:
    #ax.spines[s].set_visible(False)

#ax.grid()
#Graph = plt.show()



