#%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pandas import DataFrame
from itertools import count
import pandas as pd
import talib

index=count()

def animate(i):
    
    data = pd.read_csv(r'C:\Users\User\Desktop\Price_csv_Updater\MSFT.csv')
    
    Price= data['Price']

    data['MA100'] = talib.MA(Price, timeperiod=100)
    data['MA14'] = talib.MA(Price, timeperiod=14)
    
    
    
    plt.cla() #Clearing the axis 
    
    Date= data.iloc[-30:,0] #Take the latest 30 rows
    
    #Date= data.iloc[-100:,0]
 
    plt.plot_date(Date,data['MA14'][-30:],label='MA14',linestyle='solid')
    plt.plot_date(Date,data['MA100'][-30:], label="MA100",linestyle='solid') 
    
    plt.gcf().autofmt_xdate() #Provide better alignment of the date
    
    plt.yticks(fontsize = 5) #Changing the font size
    plt.xticks(fontsize = 5) #Changing the font size
    
    plt.legend(loc='upper left') 
    plt.tight_layout()
    
    
    
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.show()
