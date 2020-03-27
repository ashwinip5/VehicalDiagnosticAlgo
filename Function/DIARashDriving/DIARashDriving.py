# Rash Driving detection
import pandas as pd
import numpy as np
def detect_rash_driving(lat_long_time, pos_d, pos_e, Threshold):
    x=[]
    y=[]
    z=[]
    lat=lat_long_time[' Latitude']
    long=lat_long_time[' Longitude']
    Time=lat_long_time['Trip Time(Since journey start)(s)']
    pos_d1 = pd.to_numeric(pos_d)
    pos_e1 = pd.to_numeric(pos_e)
    #print(pos_d1)
    pos_d1=np.diff((pos_d1))/np.diff((Time))
    #print(pos_d1)
    pos_e1 = np.diff(pos_e1)/np.diff(Time)
    for i in range(0, len(pos_d1)):
        if (float(pos_d1[i]) > Threshold) and (float(pos_e1[i]) > Threshold / 2):
            x.append(lat[i])
            y.append(long[i])
            z.append(i)
    d = {'Latitude': x, 'Longitude': y, 'Index': z}
    df = pd.DataFrame(data=d)
    return df;
