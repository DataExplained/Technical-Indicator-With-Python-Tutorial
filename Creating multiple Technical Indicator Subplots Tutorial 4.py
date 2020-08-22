# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 11:19:11 2020

@author: User
"""

from itertools import count
import pandas as pd
import talib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as ticker
import seaborn as sns
sns.set()

#Provide the formatting for the axes
def xy_ticks(axes,x_name,y_name):
    axes.tick_params(labelsize=8, rotation=45) 
    axes.set(xlabel=x_name, ylabel=y_name)
    
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

    axes.xaxis.set_major_locator(ticker.AutoLocator())
    
    axes.set_facecolor("#e1ddbf") #Change the Axes Background Color
    return

index=count()
fig, (ax1,ax2) = plt.subplots( 2,1)
# .set_facecolor(colors[i])


#Define MOM14 and RSI14 and how it will be updated.
def animate(i):
     #Use for Moving average Crossover
    data = pd.read_csv(r'C:\Users\User\Desktop\Price_csv_Updater\MSFT.csv')

    Price= data['Price']

    data['MOM14'] = talib.MOM(Price, timeperiod=14)
    data['RSI14']=talib.RSI(Price, timeperiod=14)
  
    plt.cla() #Clearing the axis 

    Date= data.iloc[-30:,0] #Take the latest 30 rows 
    
    ax1.plot_date(Date,data['MOM14'][-30:],linestyle='solid',color="b")  
    xy_ticks(ax1,'date','MOM14') 
    ax1.set_title('Momentum')

    ax2.plot_date(Date, data['RSI14'][-30:],linestyle='solid',color="g")
    xy_ticks(ax2,'date','RSI')
    ax2.set_title('Relative Strength Index')
    
ani = animation.FuncAnimation(fig, animate,  interval=1000 )


    